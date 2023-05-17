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

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Load data for resistance and Hall resistance as a function of magnetic field
# datadown = pd.read_csv('file_path_RvsH') # Assuming that the data is in csv format
# fielddown = datadown.iloc[:, 0].values
# resistancedown = datadown.iloc[:, 1].values
# Hall_resistancedown = datadown.iloc[:, 2].values

# dataup = pd.read_csv('RH300Kup.csv') # Assuming that the data is in csv format
# fieldup = dataup.iloc[:, 0].values
# resistanceup = dataup.iloc[:, 1].values
# Hall_resistanceup = dataup.iloc[:, 2].values

# # Interpolating resistances to uniform field values
# FieldVals = np.arange(-50000, 50000+1, 50)
# InterpRxxDown = np.interp(FieldVals, fielddown, resistancedown)
# InterpRxyDown = np.interp(FieldVals, fielddown, Hall_resistancedown)
# InterpRxxUp = np.interp(FieldVals, fieldup, resistanceup)
# InterpRxyUp = np.interp(FieldVals, fieldup, Hall_resistanceup)

# # Symmetrize Rxx and antisymmetrize Rxy
# RxxAvg = (InterpRxxDown + np.flip(InterpRxxUp)) / 2
# FinalRxx = np.column_stack((FieldVals, RxxAvg))
# RxyAvg = (InterpRxyDown - np.flip(InterpRxyUp)) / 2
# FinalRxy = np.column_stack((FieldVals, RxyAvg))

# # Plot symmetrized longitudinal resistance
# plt.figure()
# plt.plot(FieldVals, RxxAvg, linewidth=2)
# plt.xlabel('Magnetic Field (T)')
# plt.ylabel('Longitudinal Resistance (Ω)')
# plt.plot(-FieldVals, RxxAvg, linewidth=2)
# plt.legend(['Up sweep', 'Down Sweep'])
# plt.show()

# # Plot antisymmetrized Hall resistance
# plt.figure()
# plt.plot(FieldVals, RxyAvg, linewidth=2)
# plt.xlabel('Magnetic Field (T)')
# plt.ylabel('Hall Resistance (Ω)')
# plt.plot(-FieldVals, -RxyAvg, linewidth=2)
# plt.legend(['Up sweep', 'Down Sweep'])
# plt.show()

# # Save the data
# MR = pd.DataFrame(np.column_stack((FieldVals, -FieldVals, RxxAvg, RxyAvg, -RxyAvg)), 
#                   columns=["Up field","Down field","Rxx","+Rxy","-Rxy"])
# MR.to_csv('230417B_300_K_MR.txt', index=False)
