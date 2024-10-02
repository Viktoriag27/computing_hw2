# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(data, cnt_name):
    """
    Calculate the total registered COVID-19 cases for a specified country.
    
    Parameters:
    data (dict): A dictionary where keys are country names and values are lists of case numbers.
    cnt_name (str): The name of the country for which to calculate the total cases.
    
    Returns:
    int: The total number of cases for the specified country. If country is not in the list it will raise an error.
    """
    # Check for first input's data type
    if not isinstance(data, dict):
        raise TypeError("The provided data should be in shape of dictionary.")
    
    # Check for second input's data type
    if not isinstance(cnt_name, str):
        raise TypeError("The provided country name should be in format of string.")
    
    # If someone gives a country name input in different cases (camel, snake or etc) function will still match it
    cnt_name_lower = cnt_name.lower()
    data_lower = {country.lower(): numbers for country, numbers in data.items()}
    
    # Check if the specified country exists in the normalized dictionary
    if cnt_name_lower not in data_lower:
        raise ValueError ('This country is not in the list')
    
    return sum(data_lower[cnt_name_lower])

# Test
print(total_registered_cases({'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6]},"sPain"))
#print(total_registered_cases({'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6]},"Italy"))


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(data):
    """
    Calculate the total registered COVID-19 cases for each country.

    This function takes a dictionary where keys are country names and values are in list. It returns 
    a new dictionary where each key is a country name and each value is the total number 
    of registered cases for that country. This function uses my previously defined function to sum up 
    total cases of Covid.

    Parameters:
    data (dict): A dictionary with country names as keys and lists as values representing the number of cases.

    Returns:
    dict: A dictionary where each key is a country name and each value is the total number of cases registered for that country.
    """

    final_dict = {}
    for country in data.keys():
        final_dict[country]=total_registered_cases(data,country)
    return final_dict

# Test
print(total_registered_cases_per_country({'Spain': [5], 'France': [2, 3, 6]}))




# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data):
    """
    Determine the country with the most registered COVID-19 cases.

    This function takes a dictionary where keys are country names and values are in list. It 
    calculates the total number of cases for each country and returns the name of the 
    country with the highest total. This function uses my previously defined functions to sum up 
    total cases of Covid and then get the country with highest records out of it.

    Parameters:
    data (dict): A dictionary with country names as keys and either lists of integers or single integers as values representing the number of cases.

    Returns:
    str or None: The name of the country with the highest total number of registered cases. If no valid data is provided, it will return None.
    """

    saved_highest_val = 0
    fin_cnt = None
    sum_all_countries = total_registered_cases_per_country(data)
    for country, number in sum_all_countries.items():
        if number > saved_highest_val:
            saved_highest_val = number
            fin_cnt = country
    return fin_cnt

# Test
print(country_with_most_cases({'Spain': [5], 'France': [2, 3, 6],'Georgia':[250]}))