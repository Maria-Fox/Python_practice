def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0

    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0
    # teetering between 0 and a number. If count == 0 it means there's full sets