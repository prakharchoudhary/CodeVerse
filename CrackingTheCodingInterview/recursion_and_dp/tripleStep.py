def numStairWays(n):
    nums = [0 for _ in range(n+1)]
    nums[0] = 1
    nums[1] = 1
    nums[2] = 2
    if n < 3:
        return nums[n]
    for i in range(3, n+1):
        nums[i] = nums[i-1] + nums[i-2] + nums[i-3]
    return nums[n]

import unittest

class Test(unittest.TestCase):
  def test_numStairWays(self):
    self.assertEqual(numStairWays(3), 4)
    self.assertEqual(numStairWays(7), 44)

if __name__ == "__main__":
  unittest.main()