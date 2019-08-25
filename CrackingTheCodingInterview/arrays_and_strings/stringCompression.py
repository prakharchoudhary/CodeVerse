def stringCompression(string):
    '''
    Compress the given string such that each continuous sequence,
    is reduced to the form "<character><frequency>"
    Eg: "aabcccccaaa" -> "a2b1c5a3"
    '''
    active_elem = string[0]
    result = []
    count = 0
    for item in string:
        if item == active_elem:
            count += 1
        else:
            result.extend((active_elem, str(count)))
            active_elem = item
            count = 1
    result.extend((active_elem, str(count)))          
    return ''.join(result)

if __name__ == '__main__':
    assert stringCompression("aabcccccaaa") == "a2b1c5a3"