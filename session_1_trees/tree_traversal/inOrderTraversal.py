class Node:
  def __init__(self, data:int):
    self.data = data
    self.left = None
    self.right = None

class Solution:
    def __init__(self, root:Node):
        self.root = root
    
    def in_order_traversal(self, root):
      if root is None:
        return
      self.in_order_traversal(root.left)
      # operations on current node
      print(root.data, end = " ")
      self.in_order_traversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    solve = Solution(root)
    solve.in_order_traversal(root)
  
