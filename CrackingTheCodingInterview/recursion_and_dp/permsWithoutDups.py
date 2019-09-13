def permutations(curr):
    # base case
    if len(curr) == 0:
        return ''
    if len(curr) == 1:
        return [curr[0]]

    # if more than 2 character the pull the first character,
    # and form permutations by placing elem in all possible positions,
    # of all permutations of remaining string.
   
    # Recurence Relations: T(n) = T(n-1) + O(n^2)
    # Time complexity: O(n^3)
    elem = curr[0]
    rem = permutations(curr[1:])
    res = []
    for item in rem:
        for rdx in range(len(item)):
            res.append(item[:rdx] + elem + item[rdx:])
        res.append(item+elem)
    return res

import unittest
class Test(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(len(permutations("abc")), 6)
        self.assertEqual(len(permutations("bcde")), 24)
        self.assertEqual(len(permutations("pqrts")), 120)
        self.assertEqual(len(permutations("wxyzab")), 720)

if __name__ == '__main__':
    unittest.main()