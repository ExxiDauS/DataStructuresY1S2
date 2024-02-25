class BSTNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
    
    def BSTNode(self):
        data = int(input())
        self.set_data(data)
    def get_data(self):
        return self.__data
    
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_data(self, data):
        data = int(input())
        self.__data = data
    
    def set_left(self, left):
        self.__left = left
    
    def set_right(self, right):
        self.__right = right

s1 = BSTNode(int(input()))
print(s1.get_data())
print(s1.get_left())
print(s1.get_right())