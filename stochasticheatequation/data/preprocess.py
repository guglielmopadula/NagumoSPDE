import mat73
import numpy as np
import skimage.measure
variables=mat73.loadmat('variables.mat')
ut=variables['tot'].astype(np.float32)
ut=np.transpose(ut)
ut=skimage.measure.block_reduce(ut, (1, 16,16), np.mean)
x=variables['x'].astype(np.float32)
t=variables['t'].astype(np.float32)
x=skimage.measure.block_reduce(x, (16), np.mean)
t=skimage.measure.block_reduce(t, (16), np.mean)
np.save('ut.npy',ut)
np.save('x.npy',x)
np.save('t.npy',t)
