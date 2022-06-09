def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # return phrase[::-1]
    # return "".join(reversed(phrase))
    result = ""
    for char in phrase:
        result = char + result
    return result 

    # must be moved back out 4 spaces otherwise it only completes one loop 
