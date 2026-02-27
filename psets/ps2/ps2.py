class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size: # that node has left_size elements less than it
            return self
        if left_size > ind and self.left is not None:
            #print(f'too small moving left from {self.key} to {self.left.key}')
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            # self.right already has left_size+1 things smaller than it
            # so now when we move to the self.right branch, we just want to find the node that has ind-left_size-1 things smaller than it 
            #print('want bigger')
            #print(f'from {self.key} went to {self.right.key}')
            return self.right.select(ind-left_size-1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        self.calculate_sizes()
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if child_side == "L":
            x = self.left
        elif child_side=="R":
            x = self.right
        else:
            print('error bad child_side')

        if direction == "L":
            y = x.right
        elif direction == 'R':
            y = x.left

        if direction == "L":
            A = x.left
            B = y.left
            C = y.right
            # replace x with y
            if child_side == "L":
                self.left = y
            if child_side == "R":
                self.right = y
            y.left = x
            x.right = B
            # fix sizes
            Asize= A.size if A else 0
            Bsize= B.size if B else 0
            Csize= C.size if C else 0
            x.size = Asize+Bsize+1
            y.size = x.size+Csize+1
        if direction == "R":
            A = y.left
            B = y.right
            C = x.right
            # replace x with y
            if child_side == "L":
                self.left = y
            if child_side == "R":
                self.right = y
            y.right = x
            x.left = B
            # fix sizes
            Asize= A.size if A else 0
            Bsize= B.size if B else 0
            Csize= C.size if C else 0
            x.size = Bsize+Csize+1
            y.size = x.size+Asize+1

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self
    def printb(self):
        if self.left is not None:
            print(f'{self.key} has left child: {self.left.key} with size {self.left.size}')
            self.left.printb()
        if self.right is not None:
            print(f'{self.key} has right child: {self.right.key} with size {self.right.size}')
            self.right.printb()
        return self