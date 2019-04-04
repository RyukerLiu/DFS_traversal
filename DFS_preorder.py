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
def preOrder_iterative(root):
    # Set current to root of binary tree
    current = root
    s = [root]  # initialze stack

    while (len(s) > 0):
        current = s.pop()
        print(current.val)
        if current.right is not None:
            s.append(current.right)

        if current.left is not None:
            s.append(current.left)
print('Iterative:')
preOrder_iterative(root)

# Iterative function for inorder tree traversal
def preOrder_recursive(root):
    if root:
        print(root.val)
        preOrder_recursive(root.left)
        preOrder_recursive(root.right)
print('Recursive:')
preOrder_recursive(root)


