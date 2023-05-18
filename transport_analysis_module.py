import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import csv

def get_R_vs_T(filename):
    """
    Retrieves R vs T data from a csv file and puts it into a pandas dataframes. 
    This function returns dataframes for Temperature, R_xx, and R_xy
    """
    #Read data from CSV
    df_RvsT = pd.read_csv(filename)
    #Extract columns
    temp_k_RvsT = df_RvsT['Temp_K']
    rxx_RvsT = df_RvsT['Rxx']
    rxy_RvsT = df_RvsT['Rxy']
    return temp_k_RvsT, rxx_RvsT, rxy_RvsT 

def get_R_vs_H(filename):
    """
    Retrieves R vs B-Field from a csv file and puts it into a pandas dataframe.
    This function returns dataframes for B-field, R_xx, and R_xy. It also returns an
    average of the temperature as a string to be used as a label for the data. 
    """
    df_RvsH = pd.read_csv(filename)
    temp_k_RvsH = str(round(df_RvsH['Temp_K'].mean())) + ' K'
    bfield_T_RvsH = df_RvsH['B_T']
    rxx_RvsH = df_RvsH['Rxx']
    rxy_RvsH = df_RvsH['Rxy']
    return temp_k_RvsH, bfield_T_RvsH, rxx_RvsH, rxy_RvsH

def plot_Rxx_vs_T(temp_k_RvsT,rxx_RvsT):
    """
    Creates a plot of Temperature vs Rxx.
    """
    plt.figure()
    plt.plot(temp_k_RvsT, rxx_RvsT)
    plt.xlabel('Temperature (K)')
    plt.ylabel('$R_{xx} (\Omega)$')
    plt.title('Temperature vs $R_{xx}$')
    plt.grid(True)
    plt.savefig('temp_k_vs_rxx.png')
    plt.show()

def plot_Rxy_vs_T(temp_k_RvsT,rxy_RvsT):
    """
    Creates a plot of Temperature vs Rxy.
    """
    plt.figure()
    plt.plot(temp_k_RvsT, rxy_RvsT)
    plt.xlabel('Temperature (K)')
    plt.ylabel('$R_{xy} (\Omega)$')
    plt.title('Temperature vs $R_{xy}$')
    plt.grid(True)
    plt.savefig('temp_k_vs_rxy.png')
    plt.show()

def plot_Rxx_vs_H(temp_k_RvsH,bfield_T_RvsH,rxx_RvsH):
    """
    Creates a plot of B-Field vs Rxx. Also adds the temperature as a label on the plot. 
    """
    plt.figure()
    plt.plot(bfield_T_RvsH, rxx_RvsH,label=temp_k_RvsH)
    plt.xlabel('B (T)')
    plt.ylabel('$R_{xx} (\Omega)$')
    plt.title('B-field vs $R_{xx}$')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig('b_field_vs_rxx.png')
    plt.show()

def plot_Rxy_vs_H(temp_k_RvsH,bfield_T_RvsH,rxy_RvsH):
    """
    Creates a plot of B-Field vs Rxy. Also adds the temperature as a label on the plot. 
    """
    plt.figure()
    plt.plot(bfield_T_RvsH, rxy_RvsH,label=temp_k_RvsH)
    plt.xlabel('B (T)')
    plt.ylabel('$R_{xy} (\Omega)$')
    plt.title('B-field vs $R_{xy}$')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig('b_field_vs_rxx.png')
    plt.show()

# Define the quadratic function
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Define the derivative of the quadratic function
def linear(x, a, b):
    return 2 * a * x + b

def calculate_slope(bfield_T_RvsH, rxy_RvsH):
    """
    Calculates the slope of the best-fit quadratic line to the Rxy vs B-field data at each B-field value.
    Returns an array of the same length as bfield_T_RvsH and rxy_RvsH, with the slope at each B-field value.
    """
    # Fit the quadratic function to the data
    popt, pcov = curve_fit(quadratic, bfield_T_RvsH, rxy_RvsH)

    # Calculate the slope at each B-field value
    slopes = linear(bfield_T_RvsH, popt[0], popt[1])

    return slopes

def calculate_hall_coefficient(bfield_T_RvsH, slopes):
    """
    Calculates the Hall coefficient from the B-field and slope data.
    """
    # The Hall coefficient is the average of the slopes divided by the average of the B-field values
    R_H = np.mean(slopes) / np.mean(bfield_T_RvsH)
    return R_H

def calculate_carrier_density(R_H):
    """
    Calculates the carrier density from the Hall coefficient.
    """
    e = 1.6e-19  # charge of an electron
    n = 1 / (e * R_H)
    return n

def calculate_mobility(rxx_RvsH, n):
    """
    Calculates the mobility from the Rxx and carrier density data.
    """
    rho = np.mean(rxx_RvsH)  # resistivity is the average of the Rxx values
    mu = 1 / (rho * n)
    return mu

def calculate_resistivity(rxx_RvsH, width, length):
    """
    Calculates the resistivity from the Rxx data and the dimensions of the device.
    """
    R = np.mean(rxx_RvsH)  # Resistance is the average of the Rxx values
    A = width * length  # Cross-sectional area
    rho = R * (A / length)  # Resistivity
    return rho

def calculate_conductivity(rho):
    """
    Calculates the conductivity from the resistivity.
    """
    sigma = 1 / rho
    return sigma

def RvsH_dat_file_import(filename):
    '''
    This function takes in a .dat file from the DynaCool PPMS System at Penn State. 
    This code assumes you use Bridge 1 for Rxx (Logitudinal) and Bridge 2 for Rxy (Hall) Resistance. 
    If you do not use this set up, you can modify the data to your needs.
    '''
    def remove_duplicates(df, column_name):
        # This inner function removes duplicate rows based on the same field value
        df_no_duplicates = df.drop_duplicates(subset=[column_name], keep='first')
        return df_no_duplicates

    with open(filename, 'r') as dat_file:
        lines = dat_file.readlines()
        columns = lines[30].strip().split(',')
        data_lines = list(csv.reader(lines[31:], delimiter=','))
        df = pd.DataFrame(data_lines, columns=columns)
    temp_df = df[['Temperature (K)']].astype('float')
    temperature = str(int(np.mean(temp_df)))
    # Convert magnetic field from Oe to T
    df['Magnetic Field (Oe)'] = df['Magnetic Field (Oe)'].astype('float') / 10000
    # Rename the column to 'Magnetic Field (T)'
    df = df.rename(columns={'Magnetic Field (Oe)': 'Magnetic Field (T)'})
    df = remove_duplicates(df, 'Magnetic Field (T)')
    magnetic_field_df = df[['Magnetic Field (T)']] #Magnetic Field (T)
    bridge1_resistance_df = df[['Bridge 1 Resistance (Ohms)']].astype('float') #Rxx or Longitudinal Resistance (Ohms)
    bridge2_resistance_df = df[['Bridge 2 Resistance (Ohms)']].astype('float') #Rxy or Hall Resistance (Ohms)
    return temperature, magnetic_field_df, bridge1_resistance_df, bridge2_resistance_df

def get_RvsH_down_and_up(magnetic_field_df,bridge1_resistance_df,bridge2_resistance_df,min_field):
    '''
    This function takes a magnetic field data frame, bridge 1 resistance, bridge2 resistance, and the minimum field of your measurement
    to generate data frames for the up sweep and the down sweep of the field. 
    For example, if you sweep from 5 Tesla to -5 Tesla and -5 Tesla to 5 Tesla, your min_field should be input as -5.
    '''
    split_index = (magnetic_field_df['Magnetic Field (T)'].round(4) == min_field).idxmax()

    magnetic_field_down = magnetic_field_df.loc[:split_index]
    magnetic_field_up = magnetic_field_df.loc[split_index:]

    bridge1_resistance_down = bridge1_resistance_df.loc[:split_index]
    bridge1_resistance_up = bridge1_resistance_df.loc[split_index:]

    bridge2_resistance_down = bridge2_resistance_df.loc[:split_index]
    bridge2_resistance_up = bridge2_resistance_df.loc[split_index:]

    fielddown = magnetic_field_down['Magnetic Field (T)'].values
    resistancedown = bridge1_resistance_down['Bridge 1 Resistance (Ohms)'].values
    Hall_resistancedown = bridge2_resistance_down['Bridge 2 Resistance (Ohms)'].values

    fieldup = magnetic_field_up['Magnetic Field (T)'].values
    resistanceup = bridge1_resistance_up['Bridge 1 Resistance (Ohms)'].values
    Hall_resistanceup = bridge2_resistance_up['Bridge 2 Resistance (Ohms)'].values
    return fielddown, resistancedown, Hall_resistancedown, fieldup, resistanceup, Hall_resistanceup

from scipy.interpolate import interp1d

def interpolate_and_symmetrize(fielddown, resistancedown, Hall_resistancedown, fieldup, resistanceup, Hall_resistanceup):
    '''
    This function interpolates and symmetrizes the PPMS data. 
    '''
    FieldVals = np.arange(-5, 5+0.0005, 0.0005)
    FixedField = FieldVals
    
    interp_down_resistance = interp1d(fielddown, resistancedown, kind='linear', fill_value="extrapolate")
    InterpRxxDown = interp_down_resistance(FixedField)
    
    interp_down_Hall_resistance = interp1d(fielddown, Hall_resistancedown, kind='linear', fill_value="extrapolate")
    InterpRxyDown = interp_down_Hall_resistance(FixedField)
    
    interp_up_resistance = interp1d(fieldup, resistanceup, kind='linear', fill_value="extrapolate")
    InterpRxxUp = interp_up_resistance(FixedField)
    
    interp_up_Hall_resistance = interp1d(fieldup, Hall_resistanceup, kind='linear', fill_value="extrapolate")
    InterpRxyUp = interp_up_Hall_resistance(FixedField)

    # Symmetrize Rxx and antisymmetrize Rxy
    RxxAvg = (InterpRxxDown + np.flip(InterpRxxUp)) / 2
    FinalRxx = np.column_stack((FixedField, RxxAvg))
    
    RxyAvg = (InterpRxyDown - np.flip(InterpRxyUp)) / 2
    FinalRxy = np.column_stack((FixedField, RxyAvg))
    
    return FixedField, RxxAvg, FinalRxx, RxyAvg, FinalRxy

def Field_vs_Rxx_down_and_up(FieldVals,RxxAvg,temperature,filename):
    '''
    This function plots Field vs Rxx and saves it as a .png.
    '''
    plt.figure()
    plt.plot(FieldVals, RxxAvg, linewidth=2)
    plt.xlabel('Magnetic Field (T)')
    plt.ylabel('Longitudinal Resistance (Ω)')
    plt.plot(-FieldVals, RxxAvg, linewidth=2)
    plt.legend(['Up sweep', 'Down Sweep'])
    plt.title('Magnetic Field v.s. Logitudinal Resistance at ' + temperature +'K')
    plt.savefig(filename + '_Field_vs_Rxx.png')
    plt.show()

def Field_vs_Rxy_down_and_up(FieldVals,RxyAvg,temperature,filename):
    '''
    This function plots Field vs R_xy and saves the figure as a .png.
    '''
    plt.figure()
    plt.plot(FieldVals, RxyAvg, linewidth=2)
    plt.xlabel('Magnetic Field (T)')
    plt.ylabel('Hall Resistance (Ω)')
    plt.plot(-FieldVals, -RxyAvg, linewidth=2)
    plt.legend(['Up sweep', 'Down Sweep'])
    plt.title('Magnetic Field v.s. Hall Resistance at ' + temperature + 'K')
    plt.savefig( filename + '_Field_vs_Rxy.png')
    plt.show()

def updown_data_writer(fieldup, resistanceup, Hall_resistanceup, fielddown, resistancedown, Hall_resistancedown,filename):
    '''
    This function will save your up data and down data as seperate .csv files with a filename you define. 
    '''
    # Convert the arrays to DataFrames
    df_up = pd.DataFrame({
        'Field Up': fieldup,
        'Resistance Up': resistanceup,
        'Hall Resistance Up': Hall_resistanceup,
    })

    df_down = pd.DataFrame({
        'Field Down': fielddown,
        'Resistance Down': resistancedown,
        'Hall Resistance Down': Hall_resistancedown,
    })

    # Write to .csv files
    df_up.to_csv(filename + '_up.csv', index=False)
    df_down.to_csv(filename + '_down.csv', index=False)
