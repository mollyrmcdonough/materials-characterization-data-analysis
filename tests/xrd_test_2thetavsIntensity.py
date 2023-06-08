import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Parse XML file
tree = ET.parse('data/example_data/xrd/XRD4_MBE1-230331A-MS_Gonio Pixcel.xrdml')
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
df = pd.DataFrame({
    '2Theta': tw_thetas,
    'Intensity': intensities
})

# Plot the data
plt.figure()
plt.plot(df['2Theta'], df['Intensity'])
plt.xlabel('2Theta (degrees)')
plt.ylabel('Intensity (arb. units)')
plt.grid(True)
plt.show()

# Save to CSV
df.to_csv('2Theta_Intensity_Data.csv', index=False)
