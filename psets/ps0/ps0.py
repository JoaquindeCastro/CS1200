#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # In the case where we reach a leaf at the bottom of the tree it should just return 1
    if v.left == None:
        left = 0
    else:
        left = calculate_sizes(v.left)
    if v.right == None:
        right = 0
    else:
        right = calculate_sizes(v.right)
    # The size of a subtree rooted at any vertex is the sum of the size of the two subtrees rooted at its children plus 1 for itself
    v.size = left + right + 1
    return v.size



#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 2t+1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t-1 (inclusive)
# Runtime: O(h) 

def FindDescendantOfSize(t, v):
    calculate_sizes(v)
    # Your code goes here 
    if (v.size>=t) and (v.size<=2*t-1):
        return v
    if v.left is None and v.right is None:
        return v
    elif v.left is None:
        return FindDescendantOfSize(t,v.right)
    elif v.right is None:
        return FindDescendantOfSize(t,v.left)
    else:
        if v.right.size >= t:
            return FindDescendantOfSize(t,v.right)
        else:
            return FindDescendantOfSize(t,v.left)