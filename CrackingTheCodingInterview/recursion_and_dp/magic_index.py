def findMagicIndex(arr, start, end):
    if start == end:
        return None
    mid = (start + end) // 2
    if mid == arr[mid]:
        return mid
    elif mid < arr[mid]:
        return findMagicIndex(arr, start, mid)
    else:
        return findMagicIndex(arr, mid + 1, end)

def magic_index_distinct(arr):
    if len(arr) == 0 or arr[0] > 0 or arr[-1] < len(arr) - 1:
        return None
    return findMagicIndex(arr, 0, len(arr))

def magic_index(arr):
    index = 0
    while index < len(arr):
        if index == arr[index]:
            return index
        index = max(arr[index], index + 1)
    return None

import unittest
class Test(unittest.TestCase):  
    def test_magic_index_distinct(self):
        self.assertEqual(magic_index_distinct([3,4,5]), None)
        self.assertEqual(magic_index_distinct([-2,-1,0,2]), None)
        self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,6,20]), None)
        self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,7,20]), 7)
        self.assertEqual(magic_index_distinct([-20,1,2,3,4,5,6,20]), 4)

    def test_magic_index(self):
        self.assertEqual(magic_index([3,4,5]), None)
        self.assertEqual(magic_index([-2,-1,0,2]), None)
        self.assertEqual(magic_index([-20,0,1,2,3,4,5,6,20]), None)
        self.assertEqual(magic_index([-20,0,1,2,3,4,5,7,20]), 7)
        self.assertEqual(magic_index([-20,1,2,3,4,5,6,20]), 1)
        self.assertEqual(magic_index([-20,5,5,5,5,5,6,20]), 5)

if __name__ == "__main__":
  unittest.main()