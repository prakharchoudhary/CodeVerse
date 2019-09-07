class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def listOfDepths(root):
    current_level = [root]
    hash_map = {}
    depth = 0
    while current_level:
        curr_level_elems = [str(node) for node in current_level]
        hash_map[depth] = curr_level_elems
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level
        depth += 1
    return hash_map

if __name__ == '__main__':
    tree = Node(5, 
        left=Node(3, left=Node(1), right=Node(8)), 
        right=Node(2, left=Node(4, 
                            left=Node(6), right=Node(9)), 
                        right=Node(7)))
    list_of_depths = listOfDepths(tree)
    for key, val in list_of_depths.items():
        print("Depth", key, ":", val)