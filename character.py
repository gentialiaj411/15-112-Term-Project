from cmu_graphics import *
class Character:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.gravity = 0.5
        self.dy = 0
        self.onGround = True
        self.currentPlatform = None

    def updatePosition(self):
        if self.onGround == False:
            self.dy += self.gravity
        self.x += self.dx
        self.y += self.dy
        if self.y >= self.yLower:
            self.y = self.yLower
            self.dy = 0
            self.onGround = True
    def moveLeft(self):
        self.dx = -10
    def moveRight(self):
        self.dx = 10
    def jump(self):
        if self.onGround:
            self.dy = -12
            self.onGround = False
    def stopMoving(self):
        self.dx = 0

    def draw(self):
        drawOval(self.x - 8, self.y + 8, 40, 15, 
                 rotateAngle = -80, fill = self.color,
                border = 'slategrey', borderWidth = 2)
        drawOval(self.x + 8, self.y + 8, 40, 15, 
                 rotateAngle = 80, fill = self.color, 
                border = 'slategrey', borderWidth = 2)
        drawOval(self.x - 12, self.y, 40, 15, 
                 rotateAngle = -40, fill = self.color, 
                border = 'slategrey', borderWidth = 2)
        drawOval(self.x + 12, self.y, 40, 15, 
                 rotateAngle = 40, fill = self.color, 
                border = 'slategrey', borderWidth = 2)
        drawLine(self.x - 15, self.y - 28, self.x - 5, 
                 self.y, lineWidth = 4, fill = 'slategrey')
        drawLine(self.x + 15, self.y - 28, self.x + 5, 
                 self.y, lineWidth = 4, fill = 'slategrey')
        drawCircle(self.x - 15, self.y - 28, 5.5, 
                   fill = self.color, 
                border = 'slategrey', borderWidth = 2)
        drawCircle(self.x + 15, self.y - 28, 5.5, 
                   fill = self.color, 
                border = 'slategrey', borderWidth = 2)
        drawCircle(self.x, self.y, self.radius, 
                   fill = self.color, 
                border = 'slategrey', borderWidth = 2)
    

