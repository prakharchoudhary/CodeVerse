def checkPermutationUsingSort(string1, string2):
    '''
    Given two strings, check if they are permutations.
    Time Complexity: O(N log N)
    Space Complexity: O(1)
    '''
    # Sort both strings and compare to see if they are identical.
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 != string2:
        return False
    return True

def checkPermutation(string1, string2):
    '''
    Given two strings, check if they are permutations.
    Time Complexity: O(N)
    Space Complexity: O(N)
    '''
    # store occurences of each character.
    char_map = [0 for i in range(26)]

    # for each charcter increase its value by one.
    for i in string1:
        char_map[ord(i) - 97] += 1
    
    # for each character decrease its value by one. 
    for i in string2:
        char_map[ord(i) - 97] -= 1

    # if any non zero value exists in char array, then return False.
    for i in char_map:
        if i != 0:
            return False

    return True

if __name__ == '__main__':
    assert checkPermutation('raman', 'aamnr') is True
    assert checkPermutation('ninja', 'ganja') is False
    assert checkPermutation('', '') is True
    assert checkPermutation('aaaaa', 'aaaa') is False
    assert checkPermutation('able', 'cable') is False

    assert checkPermutationUsingSort('raman', 'aamnr') is True
    assert checkPermutationUsingSort('ninja', 'ganja') is False
    assert checkPermutationUsingSort('', '') is True
    assert checkPermutationUsingSort('aaaaa', 'aaaa') is False
    assert checkPermutationUsingSort('able', 'cable') is False 