def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # returnList = []

    # for item in lst:
    #     if item == True:
    #         returnList.append(item)

    # return returnList

    return [val for val in lst if val]


    