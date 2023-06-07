#This is the AFM data analysis module
import pySPM
import matplotlib.pyplot as plt
import numpy as np
def importBrukerAFMData(filename):
    '''
    Simple function to import .spm AFM files from a Bruker AFM using pySPM package.
    '''
    scan = pySPM.Bruker(filename)
    return scan
def showHeightSensor(scan):
    '''
    This function shows the height sensor scan from a Bruker AFM Image.
    '''
    topo = scan.get_channel('Height Sensor')
    fig, ax = plt.subplots()
    scan.get_channel('Height Sensor').show(ax=ax)
    plt.show()

def showHeightSensorCorrected(topo):
    '''
    This function takes the topographical data from the Height Sensor and corrects the plane, then shows the data with a colorbar.
    '''
    pixels = topo.correct_plane().pixels
    im = plt.imshow(pixels, cmap='afmhot')
    plt.colorbar(im) 
    plt.show()

def afmDataShape(topo):
    pixels = topo.correct_plane().pixels
    print("Shape of the data:", pixels.shape)
    print("Min height:", np.min(pixels))
    print("Max height:", np.max(pixels))
    print("Mean height:", np.mean(pixels))