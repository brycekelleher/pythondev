#!/usr/bin/python
import sys, os, re
import curses
from subprocess import call,check_output,Popen, PIPE

p4g_version = '2013.11'
cmd = 'p4c'
FNULL = open(os.devnull, 'w')

# Fucntions for curses based selection
# {{ draw all entries on screen with cursor at index
def drawall(stdscr, entries, index, my,mx, multi, valueName='value', selectedName='selected'):
        stdscr.move(0,0)
        for i,item in enumerate(entries):
                # handle lists longer than size of terminal
                if i >= (index/my)*my and i < (index/my)*my+my:
                        attr = 0
                        string = "  " 
                        # highlight current index
                        if i == index:
                                attr = curses.A_REVERSE
                        # mark up selected
                        if item[selectedName]:
                                string = "+ "
                        if multi: 
                                stdscr.addstr(string,0)
                        stdscr.addstr(item[valueName] + '\n', attr)
        # help text at bottom
        stdscr.move(my,0)
        if multi:
                string = 'ENTER: return; SPACE: select;'
        else:
                string = 'ENTER: select and return'
        stdscr.addstr(string, curses.A_REVERSE)
# }}
# {{ curses select function
def select(entries, multi=False, valueName='value', selectedName='selected'):
        # start curses
        stdscr = curses.initscr()
         
        # curses settings
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        stdscr.keypad(1)
        
        # get width of window
        (my,mx) = stdscr.getmaxyx()
        my = my - 1      # take into account info bar

        # set index to 0 and draw initial screen
        index = 0
        drawall(stdscr, entries, index, my,mx,  multi, valueName, selectedName)
        rtn=""
        
        # user input
        while 1:
                c = stdscr.getch() 
                # exit loop
                if c == curses.KEY_ENTER or c == 10:
                        if not multi: 
                                entries[index][selectedName] = not entries[index][selectedName]
                        break
                # multi select
                if c == ord(" ") and multi:
                        entries[index][selectedName] = not entries[index][selectedName]
                # move up
                elif c == curses.KEY_UP: 
                        if index > 0:
                                index = index-1
                # move down
                elif c == curses.KEY_DOWN: 
                        if index < len(entries)-1:
                                index = index+1
                                if index % my == 0:
                                        stdscr.clear()
                # update screen
                drawall(stdscr, entries, index, my,mx, multi, valueName, selectedName)
        
        # end curses
        curses.echo()
        curses.endwin()
        
        return entries
# }}

# Basc/Early functions
# {{ p4g_login
def p4g_login():
        loggedIn = not call(['p4', 'login', '-s'], stdout=FNULL)
        if not loggedIn:
                call(['p4', 'login'])
# }}
# {{ p4g_help
def p4g_help():
        print "    Version: " + p4g_version + '\n'
        print "    "+cmd+" is a graphical extension to p4 for additional ease of use."
        print "    It includes automatic login prompt, smart P4CLIENT detection and"
        print "    modified commands. Perforce help, and other unmodified commands"
        print "    can be used through this tool and still get automatic login.\n"
        print "    Perforce Graphical modified commands:\n"
        print "\tadd        add files to a changelist selected from the command line"
        print "\tedit       edit files in a changelist selected from the command line"
        print "\tsubmit     submit a changelist selected from the command line"
        print "\tchange     display/edit a changelist selected from the command line"
        #print "\tshelve     shelve files selected from the command line in a changelist selected from the command line"
        #print "\tunshelve   unshelve files selected from the command line in a changelist selected from the command line"
        print "\n    Perforce Graphical additional commands:\n"
        print "\tpending    show all pending changelists for current user, current client"
        #print "\tsaveclient save current client to $P4CONFIG in current directory"
        print "\topened     show all open and shelved files for a changelist selected from the command line"
        print "\txhelp      show this help screen"
        print ""
# }}

# Helper functions
# {{ get_user
def get_user():
        return os.environ['P4USER']
# }}
# {{ get_client
def get_client():
        shout = check_output(['p4', 'client', '-o'])
        reout = re.search("\nClient:\s*([\.\w]*)", shout)
        return reout.group(1)
# }}        
# {{ get_pending
def get_pending():
        client = get_client()
        user = get_user()
        entries = []

        # get a list of changesets
        shout = check_output(['p4', 'changes', 
                                '-u', user,
                                '-c', client,
                                '-s', 'pending',
                                '-l'])
        # create entries in selection list
        for item in re.findall("Change ([0-9]*) on.*\n\n\s*([^\n]*)\n\n", shout):
                entries.append({'key': item[0], 'value': item[0] + ": " + item[1], 'selected': False})
        
        return entries
# }}
# {{ select_changelist
def select_changelist(new = False):
        entries = []
        
        # get pending entries
        entries = get_pending()

        # if new was input as True, then add this to the selection list
        if new:
                entries.insert(0,{'key': 'new', 'value': '==== Create New Changeset ====', 'selected': False})

        # find the selected value
        for item in select(entries):
                if item['selected']:
                        change = item['key']

        # create new changeset when requested
        if change == 'new':
                # get description
                description = raw_input("Enter Description: ")
                # grab template change
                shout = check_output(['p4', 'change', '-o'])
                # populate the description
                p = Popen(['sed', 's/<enter description here>/'+description+'/'], stdout=PIPE, stdin=PIPE)
                shout = p.communicate(input=shout)[0]
                # submit the new changelist
                p = Popen(['p4', 'change', '-i'], stdout=PIPE, stdin=PIPE)
                shout = p.communicate(input=shout)[0]
                # extract the changelist number
                reout = re.search("Change ([0-9]*) created", shout)
                change = reout.group(1)

        # return the changeset number
        return change
# }}

# P4 functionality
# {{ p4g_withChange: add/edit/submit
def p4g_withChange(new = False):
        change = select_changelist(new)
        call(['p4', argv[1], '-c', change] + argv[2:])
# }}
# {{ p4g_change
def p4g_change():
        change = select_changelist()

        call(['p4'] + argv[1:] + [change])
# }}
# {{ p4g_pending
def p4g_pending():
        entries = get_pending()
        for item in entries:
                print item['value']
# }}
# {{ p4g_opened
def p4g_opened():
        change = select_changelist()
        
        # get shelved files
        shout = check_output(['p4', 'files', '@=' + change], stderr=FNULL)
        shelved = re.findall("(//[^#]*)#[0-9]*\s-\s(\w*)", shout)
        
        # get opened files (not shelved)
        shout = check_output(['p4', 'change', '-o', change])
        opened = re.findall("\n\s*(//[^\s]*)\s*# (.*)", shout)

        # print output
        print 'Open Files (' + change + '):'
        for item in opened:
                print item[1]+'\t- '+item[0]
        print 'Shelved Files (@=' + change + '):'
        for item in shelved:
                print item[1]+'\t- '+item[0]
        
#}}

# ######################
# look at user input
# ######################
argv = sys.argv
# no need to login etc for help, so check first
if len(argv) == 1 or argv[1] == "xhelp":
        # p4g specific help
        p4g_help()
elif argv[1] == "help":
        # p4 help pass through
        p4argv = argv
        p4argv[0] = 'p4'
        call(p4argv)
        print "    For "+cmd+" help, type '"+cmd+" xhelp'\n"
elif argv[1] == "fix":
        # fix curses problem
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        stdscr.keypad(1)
        curses.echo()
        curses.endwin()
else:
        # safe login
        p4g_login()

        # main command detection
        if   argv[1] in ("add", "edit"):
                p4g_withChange(True)
        elif argv[1] == "submit":
                p4g_withChange()
        elif argv[1] == "pending":
                p4g_pending()
        elif argv[1] == "opened":
                p4g_opened()
        elif argv[1] == "change":
                p4g_change()
        else:
                p4argv = argv
                p4argv[0] = 'p4'
                call(p4argv)
