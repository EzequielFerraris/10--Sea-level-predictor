import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def draw_plot():
    # Read data from file
    dataset = pd.read_csv('epa-sea-level.csv', delimiter=',', parse_dates=True, skip_blank_lines=True, infer_datetime_format=True) 

    df = pd.DataFrame(dataset)
  
    df1 = df.copy()
  
  # Create scatter plot
  # Add labels and title
    sns.set_style('dark')
    fig, ax = figsize=(14, 6)
    sns.scatterplot(x='Year', y='CSIRO Adjusted Sea Level', data=df1).set(title='Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Create first line of best fit
    reg = stats.linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])#creates an array with core data about the dispersion: 0 the slope(pendiente), intercept (intercepción con el eje y)
    
  
    x_fit = np.linspace(np.min(df1['Year']), 2050, 171).astype(int) #creates de x domain
    
  
    y_fit = np.around(x_fit * reg[0] + reg[1], 7)
    
    
#creates de y image
  # Fit a model and predict future dates
    plt.plot(x_fit, y_fit, 'r')
#print
  
    # Create second line of best fit
    slice1 = df1[(df1['Year'] >= 2000)]
  
    reg2 = stats.linregress(slice1['Year'], slice1['CSIRO Adjusted Sea Level'])
  
    x_fit2 = np.linspace(2000, 2050, 51).astype(int) #creates de x domain
  
    y_fit2 = x_fit2 * reg2[0] + reg2[1] 
#creates de y image
  # Fit a model and predict future dates
    plt.plot(x_fit2, y_fit2, 'g')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
