# Write a Python function to convert string to url ?
# Md Abdul Aouwal to md-abdul-aouwal

"""
convert it to lower case
replace blank space with -(dash)
convert it to function
"""


def urlify(string):
    """
    This function will convert the string to url
    :param string: 
    :return: Url
    """
    stripped_string = string.strip()
    lower_case = stripped_string.lower()
    url = lower_case.replace(' ','-')
    return url


print(urlify('Md Abdul Aouwal '))

print(urlify.__doc__)



