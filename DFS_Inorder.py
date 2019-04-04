class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

""" Constructed binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Iterative function for inorder tree traversal
def inOrder_iterative(root):
    # Set current to root of binary tree
    current = root
    s = []  # initialze stack
    done = 0

    while (not done):

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            s.append(current)

            current = current.left

            # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        else:
            if (len(s) > 0):
                current = s.pop()
                print(current.val)

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                done = 1
print('Iterative:')
inOrder_iterative(root)

# Iterative function for inorder tree traversal
def inOrder_recursive(root):
    if root:
        inOrder_recursive(root.left)
        print(root.val)
        inOrder_recursive(root.right)
print('Recursive:')
inOrder_recursive(root)


