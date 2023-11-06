class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    def __init__(self, root:int):
        self.root = root

    def pre_order_traversal(self, root):
        if root is None:
            return
        # operation to be done
        print(root.data)
        # recursive call
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    solve = Solution(root)
    solve.pre_order_traversal(root)