def isPalindromePerm(string1, string2):
    '''
    Check if given strings are palindromes and permutations.
    '''
    string1 = stripSpaces(string1)
    string2 = stripSpaces(string2)
    if isPalindrome(string1) and isPalindrome(string2):
        if isPermutation(string1, string2):
            return True
    return False

def stripSpaces(string):
    '''
    Remove all the spaces in a string.
    '''
    chars = list(string)
    count = 0
    for idx, item in enumerate(chars):
        if item == ' ':
            chars[idx] = ''
    return ''.join(chars)

def isPalindrome(string):
    '''
    Check if given string is a palindrome.
    Time Complexity: O(N)
    '''
    # check is string is identical to its reverse.
    if string == string[::-1]:
        return True
    return False

def isPermutation(string1, string2):
    '''
    Given two strings, check if they are permutations.
    Time Complexity: O(N)
    Space Complexity: O(N)
    '''
    char_map = [0 for i in range(26)]
    for i in string1:
        char_map[ord(i) - 97] += 1
    
    for i in string2:
        char_map[ord(i) - 97] -= 1

    for i in char_map:
        if i != 0:
            return False

    return True

if __name__ == '__main__':
    assert isPalindromePerm("taco cat", "atco cta") is True