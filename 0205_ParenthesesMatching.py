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

def parentheses(expression):
    'full fill this shit pls'
    tmp = ''
    s_tmp = []
    count_l = 0
    count_r = 0
    st1 = ArrayStack()
    for i in str(expression):
        s_tmp.append(i)
        if i != "(" and st1.is_empty():
            pass
        else:
            st1.push(i)
        if i == ')':
            if st1.is_empty():
                st1.pop()
            else:
                for _ in range(st1.size):
                    tmp = st1.pop()
                    if tmp == "(":
                        break
    count_l = s_tmp.count("(")
    count_r = s_tmp.count(")")
    if st1.is_empty() and count_l == count_r:
        print("Parentheses in", expression, "are matched")
        print(st1.is_empty())
    else:
        print("Parentheses in", expression, "are unmatched")
        st1.push('1')
        print(st1.is_empty())

parentheses(input())
