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

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())