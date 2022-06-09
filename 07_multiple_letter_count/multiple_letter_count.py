def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    finalDict = {}

    for letter in phrase:
        finalDict[letter] = finalDict.get(letter), 0) + 1)

    return finalDict
    
    # This is based off the solution page- I do not see it return a dict containing key/values after the first iteration
