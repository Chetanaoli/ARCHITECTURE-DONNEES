class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def perform_preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        perform_preorder_traversal(node.left_child)
        perform_preorder_traversal(node.right_child)
