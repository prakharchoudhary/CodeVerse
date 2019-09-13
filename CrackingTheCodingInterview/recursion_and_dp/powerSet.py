def powerSet(str1, index, curr):
    n = len(str1)
    
    # base case
    if (index == n):
        return

    # add current string to subsets
    subsets = [curr]
    
    # for each element in the remaining sliced array after current elem,
    # add to current , recursively call powerSet, append results to subsets list,
    # remove the the last elem from curr.
    # the add and remove allows combinations like:
    # curr: "a", iter1: "ab", iter2: "ac", etc.
    for i in range(index + 1, n):
        curr += str1[i]
        subsets.extend(powerSet(str1, i, curr))
        curr = curr[:-1]
    return subsets

import unittest

class Test(unittest.TestCase):
    def test_powerSet(self):
        output = ['', 'a', 'ab', 'abc', 'abcd', 'abd', 
        'ac', 'acd', 'ad', 'b', 'bc', 'bcd', 'bd', 'c', 'cd', 'd']
        self.assertEqual(powerSet("abcd", -1, ""), output)

if __name__ == '__main__':
    unittest.main()