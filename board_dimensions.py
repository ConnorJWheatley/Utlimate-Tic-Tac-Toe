from constants import *

class BoardDimensions:

    def __init__(self, size, xcor, ycor):
        self.size = size
        self.sqsize = size // SQR_SIZE
        self.xcor = xcor
        self.ycor = ycor