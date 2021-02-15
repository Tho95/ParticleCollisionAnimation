class Box:

    def __init__(self, height, width, position):
        self.height = height
        self.width = width

    def getTop(self):
        top = self.position[1] + (self.height / 2)
        return top

    def getBottom(self):
        bottom = self.position[1] - (self.height / 2)
        return bottom

    def getRight(self):
        right = self.position[0] + (self.width / 2)
        return right

    def getLeft(self):
        left = self.position[0] - (self.width / 2)
        return left