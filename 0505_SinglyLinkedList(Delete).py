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
                print(current.get_data(), end=" -> ")
                current = current.get_next()
            print(current.get_data())

    def insert_last(self, data):
        new_node = DataNode(data)
        self.count += 1
        if not self.head:
            self.head = new_node
        #* for _ in range(self.count):
        #*     if (current != None):
        #*         current = current.get_next()
        #* current.set_next(new_node)
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)
    def insert_front(self, data):
        """Insert_front"""
        new_node = DataNode(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def insert_before(self, node_data, data):
        """Insert_before"""
        new_node = DataNode(data)
        current = self.head
        previous = None

        if current is None:
            print("Cannot insert, {} does not exist.".format(node_data))
            return

        if current.get_data() == node_data:
            self.insert_front(data)
            return

        while current is not None and current.get_data() != node_data:
            previous = current
            current = current.get_next()

        if current is None:
            print("Cannot insert, {} does not exist.".format(node_data))
            return

        new_node.set_next(current)
        previous.set_next(new_node)
        self.count += 1

    def delete(self, data):
        """Delete"""
        current = self.head
        previous = None

        if current is None:
            print("Cannot delete, {} does not exist.".format(data))
            return

        if current.get_data() == data:
            self.head = current.get_next()
            self.count -= 1
            return

        while current is not None and current.get_data() != data:
            previous = current
            current = current.get_next()

        if current is None:
            print("Cannot delete, {} does not exist.".format(data))
            return

        previous.set_next(current.get_next())
        self.count -= 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()


main()