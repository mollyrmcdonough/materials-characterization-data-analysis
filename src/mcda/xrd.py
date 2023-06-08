import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def parsexrdml_OmegavsIntensity(filename):
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Define namespace dictionary
    namespaces = {'ns': 'http://www.xrdml.com/XRDMeasurement/2.1'}

    # Extract Omega data
    omegas_start = float(root.find('.//ns:positions[@axis="Omega"]/ns:startPosition', namespaces).text)
    omegas_end = float(root.find('.//ns:positions[@axis="Omega"]/ns:endPosition', namespaces).text)

    # Extract Intensity data
    intensities = [int(count) for count in root.find('.//ns:counts', namespaces).text.split()]

    # Generate an array of Omega values assuming a linear spacing
    omegas = np.linspace(omegas_start, omegas_end, num=len(intensities))

    # Create a single dataframe for omegas and intensities
    df = pd.DataFrame({'Omega': omegas, 'Intensity': intensities})
    return df

def plotOmegavsIntensity(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Omega'], df['Intensity']/100)
    plt.xlabel('Omega')
    plt.ylabel('Intensity')
    plt.title('Omega vs Intensity')
    plt.grid(True)
    plt.show()
