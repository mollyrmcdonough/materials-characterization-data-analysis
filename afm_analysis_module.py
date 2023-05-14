import pySPM
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from IPython import display

filenameB = "Example Data/AFM Data/AFM2_MBE1-230404A-MS_23-414_Bi2Se3 on Al2O3 Se cap/MBE1-230404A-MS.0_00000.spm"
ScanB = pySPM.Bruker(filenameB)
ScanB.list_channels()
topoB = ScanB.get_channel()

fig1, ax1 = plt.subplots()
img1 = ax1.imshow(topoB.pixels, cmap='afmhot', extent=[0, topoB.size['real']['x'], 0, topoB.size['real']['y']])
cbar1 = plt.colorbar(img1, ax=ax1)
cbar1.set_label('Height (nm)')
ax1.set_xlabel('X (µm)')
ax1.set_ylabel('Y (µm)')
plt.show()

filenameA= "Example Data/AFM Data/AFM2_MBE1-230404A-MS_23-414_Bi2Se3 on Al2O3 Se cap/MBE1-230404A-MS.0_00001.spm"
ScanA = pySPM.Bruker(filenameA)
ScanA.list_channels()
topoA = ScanA.get_channel()

fig2, ax2 = plt.subplots()
img2 = ax2.imshow(topoA.pixels, cmap='afmhot', extent=[0, topoA.size['real']['x'], 0, topoA.size['real']['y']])
cbar2 = plt.colorbar(img2, ax=ax2)
cbar2.set_label('Height (nm)')
ax2.set_xlabel('X (µm)')
ax2.set_ylabel('Y (µm)')
plt.show()
