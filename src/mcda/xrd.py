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

def parsexrdml_2ThetavsIntensity(filename):
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Define namespace dictionary
    namespaces = {'ns': 'http://www.xrdml.com/XRDMeasurement/2.1'}

    # Extract 2Theta data
    tw_theta_start = float(root.find('.//ns:positions[@axis="2Theta"]/ns:startPosition', namespaces).text)
    tw_theta_end = float(root.find('.//ns:positions[@axis="2Theta"]/ns:endPosition', namespaces).text)

    # Extract Intensity data
    intensities = [int(count) for count in root.find('.//ns:counts', namespaces).text.split()]

    # Generate an array of 2Theta values assuming a linear spacing
    tw_thetas = np.linspace(tw_theta_start, tw_theta_end, num=len(intensities))

    # Create a dataframe for 2Theta and intensities
    df = pd.DataFrame({'2Theta': tw_thetas,'Intensity': intensities})
    return df

def plot2ThetavsIntensity(df):
    # Plot the data
    plt.figure()
    plt.plot(df['2Theta'], df['Intensity'])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.xlabel('2Theta (degrees)')
    plt.ylabel('Intensity (arb. units)')
    plt.grid(True)
    plt.show()
