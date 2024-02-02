import mat73
import numpy as np
variables=mat73.loadmat('variables.mat')
ut=variables['tot'].astype(np.float32)
x=variables['x'].astype(np.float32)
t=variables['t'].astype(np.float32)
ut=np.transpose(ut)
np.save('ut.npy',ut)
np.save('x.npy',x)
np.save('t.npy',t)