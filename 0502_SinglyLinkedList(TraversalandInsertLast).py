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

class SinglyLinkedList:
    def __init__(self, number=0):
        self.count = number
        self.head = None

    def traverse(self):
        current = self.head
        if not self.head:
            print("This is an empty list.")
        else:
            while current.get_next():
                print(current.get_data())
                print(current.get_next())
                print(current.get_data(), end=" -> ")
                current = current.get_next()
            print(current.get_data())

    def insert_last(self, data):
        new_node = DataNode(data)
        self.count += 1
        if not self.head:
            self.head = new_node
        # else:
        #     current = self.head
        #     for _ in range(self.count):
        #         if (current.get_next() != None):
        #             current = current.get_next()
        #     current.set_next(new_node)
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()