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

def total_registered_cases(data,cnt_name):
    """
    Calculate the total registered COVID-19 cases for a specified country.
    
    Parameters:
    data (dict): A dictionary where keys are country names and values are lists of case numbers.
    cnt_name (str): The name of the country for which to calculate the total cases.
    
    Returns:
    int: The total number of cases for the specified country. If country is not in the list specific text will printed.
    """
    # Check for first input's data type
    if not isinstance(data, dict):
        raise TypeError("The provided data should be in shape of dictionary.")
    
    # Check for second input's data type
    if not isinstance(cnt_name,str):
        raise TypeError("The provided country name should be in format of string.")
    
    # If someone gives a country name input in different cases (camel, snake or etc) function will still match it
    cnt_name_lower=cnt_name.lower()
    data_lower={country.lower(): numbers for country, numbers in data.items()}
    
    # Check if the specified country exists in the normalized dictionary
    if cnt_name_lower not in data_lower:
        return "This country is not in the list"
    
    return sum(data_lower[cnt_name_lower])

# Calculate and return the total number of registered cases for the specified country
print(total_registered_cases({'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6]},"sPAIN"))


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

    This function takes a dictionary where keys are country names and values are either 
    lists of integers (representing weekly registered cases) or single integers. It returns 
    a new dictionary where each key is a country name and each value is the total number 
    of registered cases for that country.

    Parameters:
    data (dict): A dictionary with country names as keys and either lists of integers or single integers as values representing the number of cases.

    Returns:
    dict: A dictionary where each key is a country name and each value is the total number of cases registered for that country.

    Raises:
    TypeError: If the provided data is not a dictionary.
    ValueError: If any value in the dictionary is neither a list of integers nor a single integer.
    """
    # Check for first input's data type
    if not isinstance(data, dict):
        raise TypeError("The provided data should be in shape of dictionary.")
    
    # Creating loop that will run through all countries and save their total numbers of cases in new dictionary
    final_dict={}
    
    # Checking data types of dictionary values. It should be either list or int
    for cnt_name,n_of_cases in data.items():
        if isinstance(n_of_cases,list):
            final_dict[cnt_name]=sum(n_of_cases)
        elif isinstance(n_of_cases,int):
            final_dict[cnt_name]=n_of_cases
        else:
            raise ValueError ("In data number of cases either should be provided as a list or integers")
        
    return final_dict

print(total_registered_cases_per_country({'Spain': 5, 'France': [2, 3, 6]}))

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

    This function takes a dictionary where keys are country names and values are either 
    lists of integers (representing weekly registered cases) or single integers. It 
    calculates the total number of cases for each country and returns the name of the 
    country with the highest total.

    Parameters:
    data (dict): A dictionary with country names as keys and either lists of integers or single integers as values representing the number of cases.

    Returns:
    str or None: The name of the country with the highest total number of registered cases. If no valid data is provided, it will return None.

    Raises:
    TypeError: If the provided data is not a dictionary.
    ValueError: If any value in the dictionary is neither a list of integers nor a single integer.
    """
    # Check for first input's data type
    if not isinstance(data, dict):
        raise TypeError("The provided data should be in shape of dictionary.")
    
    # Create variables that will save information when using a loop
    saved_highest_val=0
    fin_cnt=None
    
    # With the help of loop validate the type of values in dictionary
    # Sum up the total N of cases by each country
    for cnt_name,n_of_cases in data.items():
        if isinstance(n_of_cases,list):
            total_cases=sum(n_of_cases)
        elif isinstance(n_of_cases,int):
            total_cases=n_of_cases
        else:
            raise ValueError ("In data number of cases either should be provided as a list or integers")
        
        # Using logic to save the highest number of cases
        
        if total_cases>saved_highest_val:
            saved_highest_val=total_cases
            fin_cnt=cnt_name
    # Finally return the country that had the highest N of cases    
    return fin_cnt

print(country_with_most_cases({'Spain': 5, 'France': [2, 3, 6],'Georgia':250}))