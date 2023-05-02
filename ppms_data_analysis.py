import transport_analysis as ppms
# Define the file path
file_path_RvsT = "materials-characterization-data-analysis\Example Data\Transport Data\TRP4_MBE1-230323A-MS_RT_300_2K_data.csv"
file_path_RvsH = "materials-characterization-data-analysis\Example Data\Transport Data\TRP4_MBE1-230323A-MS_RvsH_20K_data_T=20K.csv"

[temp_k_RvsT, rxx_RvsT, rxy_RvsT] = ppms.get_R_vs_T(file_path_RvsT)
[temp_k_RvsH, bfield_T_RvsH, rxx_RvsH, rxy_RvsH] = ppms.get_R_vs_H(file_path_RvsH)

ppms.plot_Rxx_vs_T(temp_k_RvsT,rxx_RvsT)
ppms.plot_Rxy_vs_T(temp_k_RvsT,rxy_RvsT)
ppms.plot_Rxx_vs_H(temp_k_RvsH,bfield_T_RvsH,rxx_RvsH)
ppms.plot_Rxx_vs_H(temp_k_RvsH,bfield_T_RvsH,rxy_RvsH)