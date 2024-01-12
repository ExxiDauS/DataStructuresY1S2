class DataNode:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None
 
    def get_data(self):
        return self.__data
 
    def set_data(self, data):
        self.__data = data
 
    def get_next(self):
        return self.__next
 
    def set_next(self, next):
        self.__next = next

def main():
    sl1 = DataNode()
    sl1.set_data(input())
    print(sl1.get_data())
    print(sl1.get_next())
main()