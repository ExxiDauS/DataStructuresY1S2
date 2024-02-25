class Student:
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa
    
    def get_std_id(self):
        return self.__std_id
    
    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa
    
    def print_detail(self):
        print("ID: " + str(self.get_std_id()))
        print("Name: " + str(self.get_name()))
        print("GPA: %.2f" % self.get_gpa())

class ProbHash:
    def __init__(self, size):
        self.__hash_table = [None] * size
        self.__size = size

    def hash(self, key):
        return key % self.__size
    
    def rehash(self, hkey):
        return hkey % self.__size
    
    def insert_data(self, student):
        value = self.hash(student.get_std_id())
        count = 0
        while self.__hash_table[value]:
            if count == self.__size:
                print("The list is full. "+ str(student.get_std_id()) +" could not be inserted.")
                return None
            value = self.rehash(value + 1)
            count += 1
        self.__hash_table[value] = student
        print("Insert " + str(student.get_std_id()) + " at index " + str(value))

    def search_data(self, std_id):
        value = self.hash(std_id)
        count = 0
        while count != self.__size:
            try:
                std = self.__hash_table[count].get_std_id()
                if std == std_id:
                    print("Found " + str(std_id) + " at index " + str(count))
                    return self.__hash_table[count]
                else:
                    pass
            except:
                pass
            count += 1
        print(str(std_id) +" does not exist.")
            

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()