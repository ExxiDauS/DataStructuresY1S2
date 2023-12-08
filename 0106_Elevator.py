"""0106_Elevator"""

class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor
    
    def go_to_floor(self, floor):
        self.current_floor = floor

    def check_max_floor(self):
        return self.max_floor

    def report_current_floor(self):
        return self.current_floor

def main():
    'go up pls'
    lift = Elevator(int(input()))
    while True:
        floor = input()
        if floor.capitalize() == "Done":
            break
        if int(floor) > lift.check_max_floor():
            print("Invalid Floor!")
        else:
            lift.go_to_floor(int(floor))
    print(lift.report_current_floor())
main()
