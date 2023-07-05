#This is the AFM data analysis module
import pySPM
import matplotlib.pyplot as plt
import numpy as np
def importBrukerAFMData(filename):
    '''
    Simple function to import .spm AFM files from a Bruker AFM using pySPM package.
    '''
    scan = pySPM.Bruker(filename)
    topo = scan.get_channel('Height Sensor')
    return scan, topo
def showHeightSensor(topo):
    '''
    This function shows the height sensor scan from a Bruker AFM Image.
    '''
    fig, ax = plt.subplots()
    topo.show(ax=ax)
    plt.show()

def showHeightSensorCorrected(topo, scanSize, scanSizeLabel):
    '''
    This function takes the topographical data from the Height Sensor and corrects the plane, then shows the data with a colorbar.
    '''
    pixels = topo.correct_plane().pixels
    im = plt.imshow(pixels, cmap='afmhot')

    # Generate the labels for x and y axis
    conversion_factor = scanSize / 512  # conversion factor
    labels = np.arange(0, pixels.shape[0]+1, 100)  # generate labels every 100 pixels
    labels_corrected = np.round(labels * conversion_factor)  # convert pixel labels to micrometer

    # Apply the labels to the x and y axis
    plt.xticks(ticks=labels, labels=labels_corrected)
    plt.yticks(ticks=labels, labels=labels_corrected)

    # Set x and y labels
    plt.xlabel(scanSizeLabel)
    plt.ylabel(scanSizeLabel)

    # Create colorbar and set its ticks
    cbar = plt.colorbar(im)
    cbar.set_label('Nanometers (nm)')
    cbar.set_ticks([np.min(pixels), np.max(pixels)])  # set ticks at min and max of pixel values

    plt.show()

def afmDataShape(topo,scanSize):
    pixels = topo.correct_plane().pixels
    conversion_factor = scanSize / 512  # conversion factor

    print("Shape of the data:", pixels.shape)

    # Convert height statistics to micrometers
    print("Min height (um):", np.min(pixels) * conversion_factor)
    print("Max height (um):", np.max(pixels) * conversion_factor)
    print("Mean height (um):", np.mean(pixels) * conversion_factor)
