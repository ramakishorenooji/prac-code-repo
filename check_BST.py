""" Program to check if a given Binary
Tree is balanced like a Red-Black Tree """

# Helper function that allocates a new
# node with the given data and None
# left and right poers.
class node:

    # Construct to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns true if given tree is BST.
def isBST(root, l=None, r=None):

    # Base condition
    if root == None:
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if l != None and root.data <= l.data:
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if r != None and root.data >= r.data:
        return False

    # check recursively for every node.
    return isBST(root.left, l, root) and isBST(root.right, root, r)


# Driver Code
# if __name__ == '__main__':
# root = Node(3)
# root.left = Node(2)
# root.left.left = Node(1)
# root.left.right = Node(4)
# root.right = Node(5)
# root.right.left = Node(4)
# root.right.right = Node(6)
root = node(4)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(5)
root.right.right = node(7)

# root.right.left.left = newNode(40)
if isBST(root, None, None):
    print("Yes")
else:
    print("No")
