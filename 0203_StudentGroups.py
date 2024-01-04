class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        tmp = ''
        if self.data != []:
            tmp = self.data.pop()
            self.size -= 1
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
        return tmp
    def is_empty(self):
        return True if self.data == [] else False
    def get_stack_top(self):
        if self.data != []:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)

def main(group, member):
    'stack test'
    f_stack = ArrayStack()
    a_list = []
    count = 0
    for _ in range(member):
        f_stack.push(input())
    for _ in range(group):
        n_list = []
        a_list.append(n_list)
    while f_stack.is_empty() == False:
        for i in range(len(a_list)):
            if f_stack.is_empty():
                break
            a_list[i].append(f_stack.pop())
    for j in a_list:
        count += 1
        print("Group", str(count) + ": " + ', '.join(j))
main(int(input()), int(input()))
