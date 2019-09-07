class GNode:
    def __init__(self, val, adjacent=[]):
        self.val = val
        self.marked = False
        self.adjacent = adjacent

def getQ(queue):
    return ([(item.val) for item in queue])

def routeExists(s, t):
    '''
    Algorithm to search if a route exists between the given two nodes.
    '''
    queue = []
    s.marked = True
    queue.append(s)

    while len(queue) != 0:
        n = queue.pop(0)
        if n.val == t.val:
            return True
        n.marked = True
        for node in n.adjacent:
            if not node.marked:
                queue.append(node)
    return False

if __name__ == '__main__':
    a = GNode('a')
    b = GNode('b')
    c = GNode('c')
    d = GNode('d')
    e = GNode('e')
    f = GNode('f')
    g = GNode('g')

    a.adjacent = [b, e]
    b.adjacent = [a, d]
    c.adjacent = [d, e, f]
    d.adjacent = [b, c]
    e.adjacent = [a, c]
    f.adjacent = [c]

    elems = [a,b,c,d,e,f,g]
    for elem in elems:
        print("Adjacent to %s:" % (elem.val), [item.val for item in elem.adjacent])
    print("Route exits between a and f:", routeExists(a, f))