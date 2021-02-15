
class Particle:

    def __init__(self,canvas,radius,mass,position,velocity,acceleration,color):
        self.canvas = canvas
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.mass = mass
        self.color = color

    def getTop(self):
        top = self.position[1] + self.radius
        return top
    def getBottom(self):
        bottom = self.position[1] - self.radius
        return bottom

    def getLeft(self):
        left = self.position[0] - self.radius
        return left

    def getRight(self):
        right = self.position[0] + self.radius
        return right