from scipy import signal
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import Image
from skimage.feature import match_template
from scipy.ndimage import generic_filter

im = Image.open("outfb31_render31-hw-broken.bmp").convert("L")
data = np.array(im.getdata(), dtype='float32')
data = data.reshape(im.size[1], im.size[0])

#data = misc.lena()

lena = data
#template = np.copy(lena[0:4, 34:40]) # right eye
#template = np.copy(lena[235:295, 310:370]) # right eye
template = np.copy(lena[35:73, 191:240]) # right eye
#lena = lena + np.random.randn(*lena.shape) * 50 # add noise

#def fn(i, t):
#	i_normed = i - i.mean()
#	i_normed = i_normed / np.sqrt((i_normed.dot(i_normed)))
#
#	t = t.flatten()
#	t_normed = t - t.mean()
#	t_normed = t_normed / np.sqrt((t_normed.dot(t_normed)))
#	return i_normed.dot(t_normed)

def fn(i, t):
	i = i - i.mean()
	i_norm = np.sqrt((i.dot(i)))
	if i_norm == 0:
		return 0
	i_normalized = i / i_norm

	t = t.flatten()
	t = t - t.mean()
	t_norm = np.sqrt((t.dot(t)))
	if t_norm == 0:
		return 0
	t_normalized = t / t_norm

	return i_normalized.dot(t_normalized)


#def fn(i, t):
#	t = t.flatten()
#	i = (i - i.mean()) / (i.std() * len(i))
#	t = (t - t.mean()) / (t.std())
#	return i.dot(t)

#def fn(f, t):
#	t = t.flatten()
#	f_std = f.std()
#	f_mean = f.mean()
#	t_std = t.std()
#	t_mean = t.mean()
#	r = [((float(f[i]) - f_mean) * (float(t[i]) - t_mean)) / (f_std * t_std) for i in range(len(f))]
#	r = sum(r) / float(len(f))
#	return r
	

def ncc(i, t):
	return generic_filter(i, fn, t.shape, mode='constant', extra_keywords={'t': t})

#corr = match_template(lena, template)
#lena = (lena - lena.mean()) / (lena.std() * len(lena))
#template = (template - template.mean()) / (template.std())
#corr = signal.convolve2d(l_normed, t_normed, mode='same')
corr = ncc(lena, template)
y, x = np.unravel_index(np.argmax(corr), corr.shape) # find the match
print "location", x, y

corrscaled = 128 + 127 * corr.flatten()
im = Image.new("L", (corr.shape[1], corr.shape[0]))
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
