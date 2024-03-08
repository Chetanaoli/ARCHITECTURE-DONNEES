from activity2.activity22 import BinaryTreeNode, perform_preorder_traversal

def test_pre_order_traversal(capsys):
    # Create a binary tree:      1
    #                          /   \
    #                         2     3
    #                        / \   / \
    #                       4   5 6   7

    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    perform_preorder_traversal(root)

    captured = capsys.readouterr()
    assert captured.out == '1 '
