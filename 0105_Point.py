"""0105_Point"""

class Point:
    'check'
    def __init__(self, xxx, yyy, xxx2, yyy2):
        'init'
        self.set_coordinates(xxx, yyy)
        self.set_othercoordinates(xxx2, yyy2)

    def set_coordinates(self, xxx, yyy):
        'coor'
        self.xxx = xxx
        self.yyy = yyy

    def set_othercoordinates(self, xxx2, yyy2):
        'set coor v2'
        self.xxx2 = xxx2
        self.yyy2 = yyy2

    def get_coordinates(self):
        'get1'
        return (self.xxx, self.yyy)

    def get_coordinatesv2(self):
        'get2'
        return (self.xxx2, self.yyy2)

    def calculate_distance(self):
        'calculate'
        return ((self.xxx2 - self.xxx)**2 + (self.yyy2 - self.yyy)**2) ** 0.5

def main():
    'check point'
    coor = Point(float(input()), float(input()), float(input()), float(input()))
    print("%.2f" % coor.calculate_distance())

main()
