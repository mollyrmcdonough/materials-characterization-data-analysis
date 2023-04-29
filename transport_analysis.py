import pandas as pd
import matplotlib.pyplot as plt

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

def plot_Rxx_vs_H(temp_k_RvsH,bfield_T_RvsH,rxy_RvsH):
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

