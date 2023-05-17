import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

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
