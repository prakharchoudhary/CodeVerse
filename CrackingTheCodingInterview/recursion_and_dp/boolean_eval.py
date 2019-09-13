def strToBool(s):
    if s == '1':
        return True
    elif s == '0':
        return False

def count_eval(string, result):
    if len(string) == 0:
        return 0
    if len(string) == 1:
        if strToBool(string) == result:
            return 1
        return 0
    
    ways = 0
    for i in range(1, len(string), 2):
        c = string[i]
        left = string[:i]
        right = string[i+1:]

        leftTrue = count_eval(left, True)
        leftFalse = count_eval(left, False)
        rightTrue = count_eval(right, True)
        rightFalse = count_eval(right, False)

        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

        totalTrue = 0
        if c == '^':
            totalTrue =leftTrue * rightFalse + leftFalse * rightTrue
        elif c == '&':
            totalTrue = leftTrue * rightTrue
        elif c == '|':
            totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse

        if result:
            subWays = totalTrue
        else:
            subWays = total - totalTrue
        ways += subWays
    return ways

def count_eval_dp(string, result, hashmap):
    if len(string) == 0:
        return 0
    if len(string) == 1:
        if strToBool(string) == result:
            return 1
        return 0
    key = string + '-' + str(result)
    res = hashmap.get(key, None)
    if res:
        return res

    ways = 0
    for i in range(1, len(string), 2):
        c = string[i]
        left = string[:i]
        right = string[i+1:]

        leftTrue = count_eval_dp(left, True, hashmap)
        leftFalse = count_eval_dp(left, False, hashmap)
        rightTrue = count_eval_dp(right, True, hashmap)
        rightFalse = count_eval_dp(right, False, hashmap)

        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

        totalTrue = 0
        if c == '^':
            totalTrue =leftTrue * rightFalse + leftFalse * rightTrue
        elif c == '&':
            totalTrue = leftTrue * rightTrue
        elif c == '|':
            totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse

        if result:
            subWays = totalTrue
        else:
            subWays = total - totalTrue
        ways += subWays
    
    hashmap[key] = ways
    return ways

import unittest

class Test(unittest.TestCase):
    def test_count_eval(self):
        self.assertEqual(count_eval("1^0|0|1", False), 2)
        self.assertEqual(count_eval("0&0&0&1^1|0", True), 10)

    def test_count_eval_dp(self):
        self.assertEqual(count_eval_dp("1^0|0|1", False, {}), 2)
        self.assertEqual(count_eval_dp("0&0&0&1^1|0", True, {}), 10)

if __name__ == '__main__':
    unittest.main()