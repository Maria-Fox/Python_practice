def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # you need to identify the number and the frequency
    def freq_counter(passed):
        '''Return the frequency of passed in arguement'''

        counts = {}

        for num in passed:
            counts[num] = counts.get(num,0) +1
            # this is assigning the key value based on the key

        return counts

    return freq_counter(str(num1)) == freq_counter(str(num2))
    # returns true/ false after stringifying the num1/ num2 of freq_counter w/ num1/ num2 passed in
