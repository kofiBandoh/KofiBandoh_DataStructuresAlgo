import point

class rectangle:

    def __init__(self, bottomLeft, topRight):
        self.bottomLeft = bottomLeft
        self.topRight = topRight
        self.length = self.topRight.get_point()[0] - self.bottomLeft.get_point()[0]
        self.width = self.topRight.get_point()[1] - self.bottomLeft.get_point()[1]
    
    def get_bottomLeft(self):
        return self.bottomLeft
    
    def get_topRight(self):
        return self.topRight

    def set_topRight(self, topRight):
        self.topRight = topRight

    def set_bottomLeft(self, bottomLeft):
        self.bottomLeft = bottomLeft

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return 2 * (self.length + self.width)

    def check_overlap(self, other):
        if(self.bottomLeft.get_point()[0] < other.topRight.get_point()[0] and self.topRight.get_point()[0] > other.bottomLeft.get_point()[0]
            and self.bottomLeft.get_point()[1] < other.topRight.get_point()[1] and self.topRight.get_point()[1] > other.bottomLeft.get_point()[1]):
            return True
        return False