import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import peak_widths
import numpy as np

# Parse XML file
tree = ET.parse('Example Data/XRD Data/XRD4_MBE1-230331A-MS_33.9475 Omega.xrdml')
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

# Create dataframes for omegas and intensities
df_omegas = pd.DataFrame(omegas, columns=['Omega'])
df_intensities = pd.DataFrame(intensities, columns=['Intensity'])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df_omegas, df_intensities/100)
plt.xlabel('Omega (degrees)')
plt.ylabel('Intensity (arb. units)')
plt.grid(True)
plt.show()

# already defined:
# omegas, intensities

peak_index = np.argmax(intensities)
peak_omega = omegas[peak_index]
peak_intensity = intensities[peak_index]

width_results = peak_widths(intensities, [peak_index], rel_height=0.5)
fwhm = width_results[0][0] * np.diff(omegas)[0]  # multiply by step size to get actual width

# assuming K-Alpha 1 wavelength for Cu in Angstroms
wavelength = 1.5405980
theta = np.deg2rad(peak_omega / 2)  # convert to radians and divide by 2
d_space = wavelength / (2 * np.sin(theta))

print(f"Center (Omega): {peak_omega}")
print(f"Peak (Intensity): {peak_intensity}")
print(f"FWHM: {fwhm}")
print(f"d-space: {d_space}")


# assuming omegas and intensities are your lists
df = pd.DataFrame({
    'Omega': omegas,
    'Intensity': intensities
})

df.to_csv('OmegavsIntensity.csv', index=False)

import numpy as np
from scipy.optimize import curve_fit

# Define the Gaussian function
def gaussian(x, a, x0, sigma):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

# Set the wavelength of the X-ray (in Angstroms)
wavelength = 1.5406

# Get the index of the peak
peak_index = np.argmax(intensities)
peak = intensities[peak_index]

# Calculate the center
center = omegas[peak_index]

#Change intensities to numpy array
intensities = np.array(intensities)
# Find indices of half maxima
half_max = peak / 2.
indices_less = np.where(intensities < half_max)[0]
indices_greater = np.where(indices_less > peak_index)[0]
fwhm_indices = indices_less[indices_greater]
if len(fwhm_indices) >= 2:
    fwhm = np.abs(omegas[fwhm_indices[-1]] - omegas[fwhm_indices[0]])
else:
    fwhm = None

# Calculate d-spacing
dspace = wavelength / (2 * np.sin(np.deg2rad(center)))

# Calculate R squared error
popt, pcov = curve_fit(gaussian, omegas, intensities, p0=[peak, center, fwhm/2.355])
fitted = gaussian(omegas, *popt)
residuals = intensities - fitted
ss_res = np.sum(residuals**2)
ss_tot = np.sum((intensities - np.mean(intensities))**2)
rsq_error = 1 - (ss_res / ss_tot)

# Save to CSV
df = pd.DataFrame({
    'Center': [center],
    'Peak': [peak],
    'FWHM': [fwhm],
    'd-space': [dspace],
    'RSQ Error': [rsq_error]
})
df.to_csv('calculated_values.csv', index=False)
