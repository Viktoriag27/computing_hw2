
###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
import pandas as pd
import numpy as np

# Import and check first rows of data
covid_data = pd.read_csv('/Users/macbookpro/Desktop/DSDM/computing_ds/hw/hw2/computing_hw2/covid.csv')
print(covid_data.head())

# Drop rows where Country is NaN and fill other NaNs with 0 
covid_data = covid_data.dropna(subset=['Country'])
covid_data=covid_data.fillna(0)

# Check if countries are duplicated
country_counts = (covid_data['Country'].value_counts())
print(country_counts[country_counts > 1])


def countries_over_x_active_cases(data, threshold):
    """Returns a list of countries with more than the specified number of active cases."""
    # Sum up the active cases by countries
    active_cases = data.groupby('Country')['Active'].sum()
    
    # Filter countries with over-threshold active cases and save them in a list
    active_cases = active_cases[active_cases > threshold].index.tolist()
    
    return active_cases


def total_avg_death_conf(data, top):
    """Calculates the average deaths and confirmed cases for countries with more than a specified number of active cases."""
    # Call previous function to have over-threshold countries
    cnt_list = countries_over_x_active_cases(data, top)
    
    if not cnt_list: # Check if list is empty
        return(0,0) # In that case return 0 averages
    # Calculate average death and confirmed cases for those filtered countries
    new_data = data[data["Country"].isin(cnt_list)]
    stats_d = new_data['Deaths'].mean()
    stats_c = new_data['Confirmed'].mean()
    return(stats_d,stats_c)

# Calculate and print the averages for thresholds provided in the problem outline
thresholds = [500, 1000, 5000]
for threshold in thresholds:
    # Unpacking averages from previous formula
    avg_deaths, avg_confirmed = total_avg_death_conf(covid_data, threshold)
    print(f"Average deaths and confirmed cases for countries with more than {threshold} active cases:")
    print(f"Average Deaths: {avg_deaths:.2f}, Average Confirmed: {avg_confirmed:.2f}\n")
