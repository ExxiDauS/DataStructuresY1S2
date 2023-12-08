"0104_Rectangle"

class Rectangle:
    'rectangle'
    def __init__(self, height, width):
        'init'
        self.height = height
        self.width = width

    def calculate_area(self):
        'area'
        return self.height * self.width

    def calculate_perimeter(self):
        'perimeter'
        return (self.height * 2) + (self.width * 2)

def main():
    'calculate'
    rectangle = Rectangle(float(input()), float(input()))
    cond = input()
    if cond == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()

    print("%.2f" % result)

main()
