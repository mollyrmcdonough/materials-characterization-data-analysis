import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = 'Example Data/Transport Data/TRP4_MBE1-230327A-MS_RvsH_50K.dat'

with open(filename, 'r') as dat_file:
    lines = dat_file.readlines()
    columns = lines[30].strip().split(',')
    data_lines = list(csv.reader(lines[31:], delimiter=','))
    df = pd.DataFrame(data_lines, columns=columns)

temp_df = df[['Temperature (K)']].astype('float')
average_temp = round(temp_df.mean())
print(average_temp)

# Convert magnetic field from Oe to T
df['Magnetic Field (Oe)'] = df['Magnetic Field (Oe)'].astype('float') / 10000

# Rename the column to 'Magnetic Field (T)'
df = df.rename(columns={'Magnetic Field (Oe)': 'Magnetic Field (T)'})

magnetic_field_df = df[['Magnetic Field (T)']]
bridge1_resistance_df = df[['Bridge 1 Resistance (Ohms)']].astype('float')
bridge2_resistance_df = df[['Bridge 2 Resistance (Ohms)']].astype('float')

split_index = (magnetic_field_df['Magnetic Field (T)'].round(4) == -5).idxmax()

magnetic_field_down = magnetic_field_df.loc[:split_index]
magnetic_field_up = magnetic_field_df.loc[split_index+1:]

bridge1_resistance_down = bridge1_resistance_df.loc[:split_index]
bridge1_resistance_up = bridge1_resistance_df.loc[split_index+1:]

bridge2_resistance_down = bridge2_resistance_df.loc[:split_index]
bridge2_resistance_up = bridge2_resistance_df.loc[split_index+1:]

fielddown = magnetic_field_down['Magnetic Field (T)'].values
resistancedown = bridge1_resistance_down['Bridge 1 Resistance (Ohms)'].values
Hall_resistancedown = bridge2_resistance_down['Bridge 2 Resistance (Ohms)'].values

fieldup = magnetic_field_up['Magnetic Field (T)'].values
resistanceup = bridge1_resistance_up['Bridge 1 Resistance (Ohms)'].values
Hall_resistanceup = bridge2_resistance_up['Bridge 2 Resistance (Ohms)'].values

FieldVals = np.arange(-5, 5+0.0001, 0.00005)
InterpRxxDown = np.interp(FieldVals, fielddown, resistancedown)
InterpRxyDown = np.interp(FieldVals, fielddown, Hall_resistancedown)
InterpRxxUp = np.interp(FieldVals, fieldup, resistanceup)
InterpRxyUp = np.interp(FieldVals, fieldup, Hall_resistanceup)

RxxAvg = (InterpRxxDown + np.flip(InterpRxxUp)) / 2
FinalRxx = np.column_stack((FieldVals, RxxAvg))
RxyAvg = (InterpRxyDown - np.flip(InterpRxyUp)) / 2
FinalRxy = np.column_stack((FieldVals, RxyAvg))

plt.figure()
plt.plot(FieldVals, RxxAvg, linewidth=2)
plt.xlabel('Magnetic Field (T)')
plt.ylabel('Longitudinal Resistance (Ω)')
plt.plot(-FieldVals, RxxAvg, linewidth=2)
plt.legend(['Up sweep', 'Down Sweep'])
plt.show()

plt.figure()
plt.plot(FieldVals, RxyAvg, linewidth=2)
plt.xlabel('Magnetic Field (T)')
plt.ylabel('Hall Resistance (Ω)')
plt.plot(-FieldVals, -RxyAvg, linewidth=2)
plt.legend(['Up sweep', 'Down Sweep'])
plt.show()

MR = pd.DataFrame(np.column_stack((FieldVals, -FieldVals, RxxAvg, RxyAvg, -RxyAvg)), 
                  columns=["Up field","Down field","Rxx","+Rxy","-Rxy"])
MR.to_csv('230417B_300_K_MR.txt', index=False)
