def isUnique(string):
    '''
    Check if all character in the string are unique.
    '''

    # use a char array to store occurrences of each character
    char_map = [0 for i in range(26)]
    for item in string:
        # for each element check if it already exists then not unique.
        charVal = ord(item) - 97
        if char_map[charVal] == 1:
            return False
        char_map[charVal] += 1
    return True

if __name__ == '__main__':
    assert isUnique('abxde') is True
    assert isUnique('abbaac') is False
    assert isUnique('') is True
    assert isUnique('abcdea') is True
