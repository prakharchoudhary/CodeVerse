from pprint import pprint
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def wavelist_list(first, second, wave, prefix):
    '''
    Merge the two lists in all possible ways while keeping the individual order
    intact.
    '''
    fl = sl = 0
    if first:
       fl = len(first)
    if second:       
        sl = len(second)

    if fl == 0 or sl == 0:
       tmp = list()
       tmp.extend(prefix)
       if first:
          tmp.extend(first)
       if second:   
          tmp.extend(second)
       wave.append(tmp)
       return

    if fl:
        fitem = first.pop(0)
        prefix.append(fitem)
        wavelist_list(first, second, wave, prefix)
        prefix.pop()
        first.insert(0, fitem)

    if sl:
        fitem = second.pop(0)
        prefix.append(fitem)
        wavelist_list(first, second, wave, prefix)
        prefix.pop()
        second.insert(0, fitem) 

def allSequences(node):
    results = []
    if not node:
        results.append([])
        return results
    prefix = []
    prefix.append(node.val)
    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)
    for left in leftSeq:
        for right in rightSeq:
            weaved = []
            wavelist_list(left, right, weaved, prefix)
            results += weaved
    return results

if __name__ == '__main__':
    # tree = Node(5, 
    #     left=Node(3, 
    #             left=Node(1), 
    #             right=Node(4)
    #             ), 
    #     right=Node(9, 
    #             left=Node(7, left=Node(6)),  
    #             right=Node(11, left=Node(10), right=Node(12))
    #             )
    #     )
    tree = Node(2, left=Node(1), right=Node(3))
    pprint(allSequences(tree))
