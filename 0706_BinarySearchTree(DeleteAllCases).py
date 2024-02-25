class BSTNode:
    def __init__(self, data) -> None:
        self.data = int(data)
        self.left = None
        self.right = None
 
    def set_data(self, data):
        self.data = int(data)
 
    def set_left(self, left_node):
        self.left = left_node
 
    def set_right(self, right_node):
        self.right = right_node
 
    def get_data(self):
        return self.data
 
    def get_left(self):
        return self.left
 
    def get_right(self):
        return self.right
 
class BST:
    def __init__(self) -> None:
        self.root = None
 
    def get_root(self):
        return self.root
 
    def set_root(self, root):
        self.root = root
 
    def insert(self, data):
        self.root = self._insert(self.root, data)
 
    def _insert(self, root, data):
        if root is None:
            return BSTNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root
 
    def preorder(self) -> None:
        start = self.get_root()
        def recursion(start):
            if start != None:
                print('->', start.get_data(), end=' ')
                recursion(start.get_left())
                recursion(start.get_right())
        recursion(start)
        print()
 
    def is_empty(self):
        return self.root is None
 
    def inorder(self) -> None:
        def recursion(start):
            if start != None:
                recursion(start.get_left())
                print('->', start.get_data(), end=' ')
                recursion(start.get_right())
        recursion(self.get_root())
        print()
 
    def postorder(self) -> None:
        def recursion(start):
            if start != None:
                recursion(start.get_left())
                recursion(start.get_right())
                print('->', start.get_data(), end=' ')
        recursion(self.get_root())
        print()
 
    def traverse(self):
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('Inorder: ', end='')
        self.inorder()
        print('Postorder: ', end='')
        self.postorder()
 
    def _find_min(self, root):
        if self.is_empty():
            return None
        cur = root
        while cur.left:
            cur = cur.left
        return cur.data
 
    def find_min(self):
        return self._find_min(self.root)
 
    def find_max(self):
        return self._find_max(self.root)
 
    def _find_max(self, root):
        if self.is_empty():
            return None
        cur = root
        while cur.right:
            cur = cur.right
        return cur.data
 
    def delete(self, data):
        self.root = self._delete(self.root, data)
 
    def _delete(self, root, data):
        if root is None:
            print("Delete Error, %s is not found in Binary Search Tree." % data)
            return None
 
        if data < root.get_data():
            root.set_left(self._delete(root.get_left(), data))
        elif data > root.get_data():
            root.set_right(self._delete(root.get_right(), data))
        else:
            if root.get_left() is None:
                return root.get_right()
            elif root.get_right() is None:
                return root.get_left()
 
            root.set_data(self._find_max(root.get_left()))
            root.set_left(self._delete(root.get_left(), root.get_data()))
 
        return root
 
def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
 
main()