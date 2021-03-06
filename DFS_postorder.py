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


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


# A iterative function to do postorder traversal of
# a given binary tree
def postOrder_iterative(root):
    # Check for empty tree
    if root is None:
        return

    stack = []

    while (True):

        while (root):
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            # Set root as root's left child
            root = root.left

            # Pop an item from stack and set it as root
        root = stack.pop()

        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
                peek(stack) == root.right):
            stack.pop()  # Remove right child from stack
            stack.append(root)  # Push root back to stack
            root = root.right  # change root so that the
            # righ childis processed next

        # Else print root's data and set root as None
        else:
            print(root.val)
            root = None

        if (len(stack) <= 0):
            break

print('Iterative:')
postOrder_iterative(root)

# Iterative function for inorder tree traversal
def postOrder_recursive(root):
    if root:
        postOrder_recursive(root.left)
        postOrder_recursive(root.right)
        print(root.val)
print('Recursive:')
postOrder_recursive(root)


