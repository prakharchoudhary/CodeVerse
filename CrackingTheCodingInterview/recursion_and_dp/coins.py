def makeChangeHelper(money, coins, index):
    '''
    Recursive approach.
    '''
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    amountWithCoin = 0
    ways = 0
    while amountWithCoin <= money:
        remaining = money - amountWithCoin
        ways += makeChangeHelper(remaining, coins, index+1)
        amountWithCoin += coins[index]
    return ways

def makeChangeHelperDP(money, coins, index, hashmap):
    '''
    Dynamic Programming based approach.
    '''
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    key = str(money) + '-' + str(index)
    ways = hashmap.get(key, None)
    if ways:
        return ways
    amountWithCoin = 0
    ways = 0
    while amountWithCoin <= money:
        remaining = money - amountWithCoin
        ways += makeChangeHelperDP(remaining, coins, index+1, hashmap)
        amountWithCoin += coins[index]
    hashmap[key] = ways
    return ways

def makeChange(money):
    # return makeChangeHelper(money, [25,10,5,1], 0)
    return makeChangeHelperDP(money, [25,10,5,1], 0, {})

if __name__ == '__main__':
    assert makeChange(0) == 1
    assert makeChange(1) == 1
    assert makeChange(5) == 2
    assert makeChange(10) == 4
