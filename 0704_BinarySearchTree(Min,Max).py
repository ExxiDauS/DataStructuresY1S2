"""code"""
class BSTNode:
    """code"""
    def __init__(self, data) -> None:
        """code"""
        self.data = int(data)
        self.left = None
        self.right = None
  
    def set_data(self, data):
        """code"""
        self.data = int(data)
  
    def set_left(self, left_node):
        """code"""
        self.left = left_node
  
    def set_right(self, right_node):
        """code"""
        self.right = right_node
  
    def get_data(self):
        """code"""
        return self.data
  
    def get_left(self):
        """code"""
        return self.left
  
    def get_right(self):
        """code"""
        return self.right
  
class BST:
    """code"""
    def __init__(self) -> None:
        """code"""
        self.root = None
  
    def get_root(self):
        """code"""
        return self.root
  
    def set_root(self, root):
        """code"""
        self.root = root
  
    def insert(self, data):
        """code"""
        self.root = self._insert(self.root, data)
  
    def _insert(self, root, data):
        """code"""
        if root is None:
            return BSTNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root
  
    def preorder(self):
        """code"""
        self._preorder(self.root)
        print()
  
    def _preorder(self, root):
        """code"""
        if root:
            print("->", root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)
  
    def is_empty(self):
        """code"""
        return self.root is None
  
    def inorder(self):
        """code"""
        self._inorder(self.root)
        print()
  
    def _inorder(self, root):
        """code"""
        if root:
            self._inorder(root.left)
            print("->", root.data, end=" ")
   
            self._inorder(root.right)
  
    def postorder(self):
        """code"""
        self._postorder(self.root)
        print()
  
    def _postorder(self, root):
        """code"""
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print("->", root.data, end=" ")
  
    def traverse(self):
        """code"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('Inorder: ', end='')
        self.inorder()
        print('Postorder: ', end='')
        self.postorder()
  
    def _find_min(self, root):
        """code"""
        if self.is_empty():
            return None
        cur = root
        while cur.left:
            cur = cur.left
        return cur.data
  
    def find_min(self):
        """code"""
        return self._find_min(self.root)
  
    def find_max(self):
        """code"""
        return self._find_max(self.root)
  
    def _find_max(self, root):
        """code"""
        if self.is_empty():
            return None
        cur = root
        while cur.right:
            cur = cur.right
        return cur.data
  
def main():
    """code"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())
  
main()