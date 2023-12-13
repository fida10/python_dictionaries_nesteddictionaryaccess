""" 
Practice Question 3: Nested Dictionary Access

Task:

Implement a function get_nested_value that takes a nested dictionary 
and a list of keys. The function should return the value located by 
following the sequence of keys in the nested dictionary. 
If any key is not found at any level, return None.
"""

def get_nested_value(dict, list):
    if len(list) == 0:
        return None
    try:
        for indiv_element in list:
            dict = dict[indiv_element]
        return dict
    except KeyError:
        return None
