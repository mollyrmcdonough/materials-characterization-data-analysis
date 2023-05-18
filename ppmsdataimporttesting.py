import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = 'Example Data/Transport Data/TRP4_MBE1-230327A-MS_RvsH_50K.dat'

with open(filename, 'r') as dat_file:
    lines = dat_file.readlines()
    # Line 30 with [Data] is index 29 in zero-based index, so line 31 is index 30
    columns = lines[30].strip().split(',')

    # Read data
    data_lines = list(csv.reader(lines[31:], delimiter=','))  # Assuming comma-separated data

    # Convert to DataFrame
    df = pd.DataFrame(data_lines, columns=columns)

# Separate into individual dataframes
temp_df = df[['Temperature (K)']].astype('float')
average_temp = round(temp_df.mean())
print(average_temp)
magnetic_field_df = df[['Magnetic Field (Oe)']].astype('float')
bridge1_resistance_df = df[['Bridge 1 Resistance (Ohms)']].astype('float')
bridge2_resistance_df = df[['Bridge 2 Resistance (Ohms)']].astype('float')

# Find the first index where the magnetic field is -50000 (rounded down)
split_index = (magnetic_field_df['Magnetic Field (Oe)'].round() == -50000).idxmax()

# Split the dataframes
magnetic_field_down = magnetic_field_df.loc[:split_index]
magnetic_field_up = magnetic_field_df.loc[split_index+1:]

bridge1_resistance_down = bridge1_resistance_df.loc[:split_index]
bridge1_resistance_up = bridge1_resistance_df.loc[split_index+1:]

bridge2_resistance_down = bridge2_resistance_df.loc[:split_index]
bridge2_resistance_up = bridge2_resistance_df.loc[split_index+1:]

# Assuming you've done the splits and stored the data in the appropriate DataFrames already
fielddown = magnetic_field_down['Magnetic Field (Oe)'].values
resistancedown = bridge1_resistance_down['Bridge 1 Resistance (Ohms)'].values
Hall_resistancedown = bridge2_resistance_down['Bridge 2 Resistance (Ohms)'].values

fieldup = magnetic_field_up['Magnetic Field (Oe)'].values
resistanceup = bridge1_resistance_up['Bridge 1 Resistance (Ohms)'].values
Hall_resistanceup = bridge2_resistance_up['Bridge 2 Resistance (Ohms)'].values

# Interpolating resistances to uniform field values
FieldVals = np.arange(-50000, 50000+1, 50)
InterpRxxDown = np.interp(FieldVals, fielddown, resistancedown)
InterpRxyDown = np.interp(FieldVals, fielddown, Hall_resistancedown)
InterpRxxUp = np.interp(FieldVals, fieldup, resistanceup)
InterpRxyUp = np.interp(FieldVals, fieldup, Hall_resistanceup)

# Symmetrize Rxx and antisymmetrize Rxy
RxxAvg = (InterpRxxDown + np.flip(InterpRxxUp)) / 2
FinalRxx = np.column_stack((FieldVals, RxxAvg))
RxyAvg = (InterpRxyDown - np.flip(InterpRxyUp)) / 2
FinalRxy = np.column_stack((FieldVals, RxyAvg))

# Plot symmetrized longitudinal resistance
plt.figure()
plt.plot(FieldVals, RxxAvg, linewidth=2)
plt.xlabel('Magnetic Field (T)')
plt.ylabel('Longitudinal Resistance (Ω)')
plt.plot(-FieldVals, RxxAvg, linewidth=2)
plt.legend(['Up sweep', 'Down Sweep'])
plt.show()

# Plot antisymmetrized Hall resistance
plt.figure()
plt.plot(FieldVals, RxyAvg, linewidth=2)
plt.xlabel('Magnetic Field (T)')
plt.ylabel('Hall Resistance (Ω)')
plt.plot(-FieldVals, -RxyAvg, linewidth=2)
plt.legend(['Up sweep', 'Down Sweep'])
plt.show()

# Save the data
MR = pd.DataFrame(np.column_stack((FieldVals, -FieldVals, RxxAvg, RxyAvg, -RxyAvg)), 
                  columns=["Up field","Down field","Rxx","+Rxy","-Rxy"])
MR.to_csv('230417B_300_K_MR.txt', index=False)
