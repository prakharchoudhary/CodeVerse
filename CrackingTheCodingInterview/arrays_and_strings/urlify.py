def urilfy(string, n):
    '''
    Replace all spaces with '%20' in the given string.
    '''
    chars = list(string)
    count = 0
    for idx, item in enumerate(chars):
        # iterate only for given length
        if count >= n:
            break
        # replace each space with '%20'
        if item == ' ':
            chars[idx] = '%20'
    # join characters to return a string
    return ''.join(chars[:n])

if __name__ == '__main__':
    assert urilfy("Mr John Smith     ", 13) == "Mr%20John%20Smith"
    assert urilfy("Cool   Whip", 11) == "Cool%20%20%20Whip"