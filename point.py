class point:

    def __init__(self, Xcord, Ycord):
        self.Xcord = Xcord
        self.Ycord = Ycord

    def set_Xcord(self, Xcord):
        self.Xcord = Xcord
    
    def set_Ycord(self, Ycord):
        self.Ycord = Ycord

    def get_Xcord(self):
        return self.Xcord

    def get_Ycord(self):
        return self.Ycord

    def get_point(self):
        return self.Xcord, self.Ycord
    

    
