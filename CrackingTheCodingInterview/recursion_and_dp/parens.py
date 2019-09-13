def parens(n):
    if n == 0:
        return None
    if n == 1:
        return ['()']
    res = parens(n-1)
    results = set()
    for elem in res:
        results.add('(' + elem + ')')
        results.add('()' + elem)
        results.add(elem + '()')
    return results

def printSet(sett):
    print(' '.join(sett))

if __name__ == '__main__':
    printSet(parens(2))
    printSet(parens(3))
    printSet(parens(4))