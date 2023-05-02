import xrdtools as xrd

data = xrd.read_xrdml("Example Data\XRD Data\XRD4_MBE1-230331A-MS_33.9475 Omega.xrdml")

x = data['x']
y = data['data']

from matplotlib import pyplot as plt

plt.plot(x, y)
plt.show()
