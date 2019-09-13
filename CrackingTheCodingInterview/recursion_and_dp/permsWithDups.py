def permutations(string):
  return substring_permutations("", sorted(string))

def substring_permutations(substring, letters):
    if len(letters) == 0:
        return [substring]
    permutations = []
    prev_letter = None
    for i, letter in enumerate(letters):
        if letter == prev_letter:
            continue
        next_part = substring + letter
        next_letters = letters[:i] + letters[(i+1):]
        permutations += substring_permutations(next_part, next_letters)
        prev_letter = letter
    return permutations

import unittest

class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutations("abca"), ["aabc", "aacb", "abac", "abca",
        "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])

if __name__ == "__main__":
  unittest.main()
