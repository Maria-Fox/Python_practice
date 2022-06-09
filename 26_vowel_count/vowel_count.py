def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    vowels = set("aeiou")
    counter = {}        
    count = 0

    for char in phrase:
        if char in vowels:
            counter[char] = counter.get(char, 0) +1

    return counter

            # read as counter of char- counter - an integer cariable with an initial value of 0. Set of vowels gives you the keys

        
# To count several different objects at once, you can use a Python dictionary. The dictionary keys will store the objects you want to count. The dictionary values will hold the number of repetitions of a given object, or the object’s count.