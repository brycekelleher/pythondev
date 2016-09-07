def gen_substrings(s):
    if len(s) == 1:
        return [s]

    # generate the substrings
    ss = []
    for i in range(1, len(s) + 1):
        ss.append(s[:i])

    return ss + gen_substrings(s[1:])

print gen_substrings("abcd")

def gen_subsets(s):
    if s == "":
        return [s]

    f = s[:1]
    r = s[1:]
    subsets = gen_subsets(r)
    l = []
    for i in subsets:
        l.append(f + i)
    return subsets + l 

print gen_subsets("abcd")
