from scipy import signal
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import Image
from skimage.feature import match_template

im = Image.open("outfb31_render31-hw-broken.bmp").convert("L")
data = np.array(im.getdata())
data = data.reshape(im.size[1], im.size[0])

#data = misc.lena()

lena = data
#lena -= lena.mean()
#l_normed = lena / float(lena.max())
template = np.copy(lena[0:4, 34:40]) # right eye
#template = np.copy(lena[235:295, 310:370]) # right eye
#template = np.copy(lena[35:73, 191:240]) # right eye
#template -= template.mean()
#t_normed = template / float(template.max())
#lena = lena + np.random.randn(*lena.shape) * 50 # add noise
#corr = match_template(lena, template)
#lena = (lena - lena.mean()) / (lena.std() * len(lena))
#template = (template - template.mean()) / (template.std())
corr = match_template(lena, template)
y, x = np.unravel_index(np.argmax(corr), corr.shape) # find the match
print "location", x, y

corrscaled = corr.flatten() * 256.0
im = Image.new("L", (320, 240))
im.putdata(corrscaled)
im.save("corr.bmp")            


fig, (ax_orig, ax_template, ax_corr) = plt.subplots(1, 3)
ax_orig.imshow(lena, cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()
ax_template.imshow(template, cmap='gray')
ax_template.set_title('Template')
ax_template.set_axis_off()
ax_corr.imshow(corr, cmap='gray')
ax_corr.set_title('Cross-correlation')
ax_corr.set_axis_off()
ax_orig.plot(x, y, 'ro')
fig.show()
