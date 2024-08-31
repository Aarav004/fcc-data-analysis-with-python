import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


# Read data from file
df = pd.read_csv('sea_level.csv')


# Create scatter plot
plt.scatter(x= 'Year', y ='CSIRO Adjusted Sea Level', data = df)


# Create first line of best fit
result = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
slope1 = result[0]
intercept1 = result[1]
years_extended = range(1880, 2051)
line1 = [slope1 * year + intercept1 for year in years_extended]
plt.plot(years_extended, line1)



# Create second line of best fit
df_r = df[df['Year'] >= 2000]
slope2, intercept2, _,_,_  = linregress(x = df_r['Year'], y = df_r['CSIRO Adjusted Sea Level'])
years_recent = range(2000, 2051)
line2 = [slope2 * year + intercept2 for year in years_recent]
plt.plot(years_recent, line2)




# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])


# Save plot and return data for testing (DO NOT MODIFY)
 plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Create first line of best fit
slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = range(1880, 2051)
line1 = [slope1 * year + intercept1 for year in years_extended]
plt.plot(years_extended, line1, color='red', label='Fit Line 1')

# Create second line of best fit
df_recent = df[df['Year'] >= 2000]
slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent = range(2000, 2051)
line2 = [slope2 * year + intercept2 for year in years_recent]
plt.plot(years_recent, line2, color='green', label='Fit Line 2')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Customize the ticks on the x-axis
plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

# Add a legend
plt.legend()
