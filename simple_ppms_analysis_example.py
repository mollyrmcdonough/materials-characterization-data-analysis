import transport_analysis_module as ppms
# Define the file path
file_path_RvsT = "Example Data/Transport Data/TRP4_MBE1-230323A-MS_RT_300_2K_data.csv"
file_path_RvsH = "Example Data/Transport Data/TRP4_MBE1-230323A-MS_RvsH_20K_data_T=20K.csv"

[temp_k_RvsT, rxx_RvsT, rxy_RvsT] = ppms.get_R_vs_T(file_path_RvsT)
[temp_k_RvsH, bfield_T_RvsH, rxx_RvsH, rxy_RvsH] = ppms.get_R_vs_H(file_path_RvsH)

ppms.plot_Rxx_vs_T(temp_k_RvsT,rxx_RvsT)
ppms.plot_Rxy_vs_T(temp_k_RvsT,rxy_RvsT)
ppms.plot_Rxx_vs_H(temp_k_RvsH,bfield_T_RvsH,rxx_RvsH)
ppms.plot_Rxy_vs_H(temp_k_RvsH,bfield_T_RvsH,rxy_RvsH)

# Calculate the slope of the best-fit quadratic line to the Rxy vs B-field data
slopes = ppms.calculate_slope(bfield_T_RvsH, rxy_RvsH)

# Calculate the Hall coefficient
R_H = ppms.calculate_hall_coefficient(bfield_T_RvsH, slopes)

# Calculate the carrier density
n = ppms.calculate_carrier_density(R_H)

# Calculate the mobility
mu = ppms.calculate_mobility(rxx_RvsH, n)

print(f'Hall coefficient = {R_H}')
print(f'Carrier density = {n}')
print(f'Mobility = {mu}')

# Add these lines to your script where you call the functions
width = 500e-6  # width in meters
length = 1000e-6  # length in meters

rho = ppms.calculate_resistivity(rxx_RvsH, width, length)
sigma = ppms.calculate_conductivity(rho)

print(f'Resistivity = {rho}')
print(f'Conductivity = {sigma}')
