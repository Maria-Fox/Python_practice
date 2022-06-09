def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
final_dict = {}

    for idx, val in enumerate(keys):
        # the above gives you the index and value in each key item 
        final_dict[val] = values[idx] if idx < len(values) else None
        #  the above gives you the values by index

    return final_dict

    # enumerate adds counter for an interable and returns it in a form of enumerating object. Default = 0. Syntax: enumerate(iterable, start)