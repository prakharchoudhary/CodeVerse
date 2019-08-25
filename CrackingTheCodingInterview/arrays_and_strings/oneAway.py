def oneAway(str1, str2):
    '''
    Possible actions:
    - Remove a character.
    - Insert a character.
    - Replace a character.

    If only one of the above action on either string, 
    results in identical strings, return True, else return False.
    '''
    non_zero_count = 0
    # non zero count of 1 means either an insertion or deletion.
    # non zero count of 2 means replacing.
    # non zero count is greater than 2, then more than one action is required.
    char_map = [0 for i in range(26)]
    
    for i in str1:
        char_map[ord(i) - 97] += 1
    
    for i in str2:
        char_map[ord(i) - 97] -= 1

    for i in char_map:
        if i != 0:
            non_zero_count += 1
    if non_zero_count > 2:
        return False

    return True

if __name__ == '__main__':
    assert oneAway('pale', 'ple') is True
    assert oneAway('pales', 'pale') is True
    assert oneAway('pales', 'bale') is False
    assert oneAway('palse', 'pale') is True
    assert oneAway('pale', 'bale') is True
    assert oneAway('pale', 'bake') is False
