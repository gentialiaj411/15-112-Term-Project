from cmu_graphics import *
from character import Character
from platforms import Platform, Tunnel
import math
import pygame


def onAppStart(app):
    startMusic()
    app.level = 1
    app.nextLevelScore = 250
    app.forwardSpeed = 3
    app.height = 800
    app.width = 800
    app.mode = 'home'
    app.playerColor = 'blue'
    app.character = Character(app.width/2, app.height*4/5, 20, 
                              app.color if app.playerColor == 'custom' else app.playerColor)
    app.tunnel = Tunnel(numSides=6,segments=10,spacing=20,radius=400,depth=600,
                        cx=app.width/2,cy=app.height/2)
    app.ringDepth = app.tunnel.depth / app.tunnel.segments
    app.ballX = app.width/2
    app.ballY = app.width*4/5
    app.worldX = 0
    app.worldY = 0
    app.vx = 0
    app.vy = 0
    app.steps = 0
    app.currentPlatform = None
    app.lastRotatedPlatform = None
    app.lastLandingIndex= None
    app.score = 0
    app.stepsPerSecond = 40
    app.platform = Platform(app.width/2, 700, 200, 20, 'green')
    app.landingIndex = -1
    app.landingT = -1
    app.red = 255
    app.green = 255
    app.blue = 0
    app.color = rgb(app.red, app.green, app.blue)
    app.highScore = 0

def startMusic(): 
    #chatgpt
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


def standingOnPlatform(app, character):
    if len(app.tunnel.rings) == 0:
        return False
    
    frontRing = app.tunnel.rings[0]
    for i in range(app.tunnel.numSides):
        if frontRing["holes"][i]:
            continue
        platform = frontRing["platforms"][i]      
        x1, y1, x2, y2, x3, y3, x4, y4 = platform
        dx, dy = x2 - x1, y2 - y1
        lineLength = dx**2 + dy**2
        if lineLength == 0:
            t = 0
            closestX, closestY = x1, y1
        else:
            t = max(0,min(1, ((character.x - x1)*dx + 
                              (character.y - y1)*dy) / lineLength))
            closestX = x1+t*dx
            closestY = y1+t*dy
        distanceToLine = math.sqrt((character.x-closestX)**2 + 
                                   (character.y - closestY)**2)
        if (distanceToLine <= character.radius + 5 and app.vy >= 0 and 
        character.y <= closestY):
            if app.tunnel.isHole(0,i):
                character.onGround = False
                app.tunnel.moveVertical(10)
                return False
            app.landingIndex = i
            app.landingT = t
            app.currentPlatform = frontRing["platforms"][i]
            app.vy = 0
            character.onGround = True
            return True
    character.onGround = False
    return False
    
def resetGame(app):
    app.character = Character(app.width/2, 717, 20, 
                              app.color if app.playerColor == 'custom' 
                              else app.playerColor)
    app.score = 0
    app.worldY = 0
    app.worldX = 0
    app.vy = 0
    app.vx = 0
    app.steps = 0
    app.currentPlatform = None
    app.lastRotatedPlatform = None
    app.tunnel = Tunnel(numSides=6,segments=10,spacing=20,
                        radius=400,depth=600,
                        cx=app.width/2,cy=app.height/2)
    #chatgpt start
    app.level = 1
    app.nextLevelScore = 250
    app.forwardSpeed = 3

    app.tunnel = Tunnel(numSides=6, segments=10, spacing=20,
                        radius=400, depth=600,
                        cx=app.width/2, cy=app.height/2)
    app.tunnel.incDifficulty(app.level)
    #chatgpt end 
def redrawAll(app):
    drawBackground(app)
    if app.mode == 'home':
        homeScreen(app)
    elif app.mode == 'game':
        app.tunnel.draw()
        app.character.draw()
        gameScreen(app)
    elif app.mode == 'settings':
        settingsScreen(app)
    elif app.mode == 'gameOver':
        gameOverScreen(app)
    elif app.mode == 'paused':
        pauseScreen(app)

def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill='black')
    drawCircle(160, 160, 5, fill = 'lemonChiffon')
    drawCircle(600, 120, 5, fill = 'lemonChiffon')
    drawCircle(304, 230, 5, fill = 'lemonChiffon')
    drawCircle(139, 393, 5, fill = 'lemonChiffon')
    drawCircle(793, 129, 5, fill = 'lemonChiffon')
    drawCircle(398, 498, 5, fill = 'lemonChiffon')
    drawCircle(702, 629, 5, fill = 'lemonChiffon')
    drawCircle(336, 92, 5, fill = 'lemonChiffon')
    drawCircle(23, 793, 5, fill = 'lemonChiffon')
    drawCircle(349, 294, 5, fill = 'lemonChiffon')
    drawCircle(193, 39, 5, fill = 'lemonChiffon')
    drawCircle(520, 205, 5, fill = 'lemonChiffon')
    drawCircle(23, 535, 5, fill = 'lemonChiffon')
    drawCircle(230, 602, 5, fill = 'lemonChiffon')
    drawCircle(403, 23, 5, fill = 'lemonChiffon')
    drawCircle(623, 405, 5, fill = 'lemonChiffon')
    drawCircle(734, 308, 5, fill = 'lemonChiffon')
    drawCircle(698, 435, 5, fill = 'lemonChiffon')
    drawCircle(585, 520, 5, fill = 'lemonChiffon')
    drawCircle(604, 284, 5, fill = 'lemonChiffon')
    drawCircle(720, 40, 5, fill = 'lemonChiffon')
    drawCircle(680, 180, 5, fill = 'lemonChiffon')
    drawCircle(60, 190, 5, fill = 'lemonChiffon')
    drawCircle(140, 720, 5, fill = 'lemonChiffon')
    drawCircle(319, 770, 5, fill = 'lemonChiffon')
    drawStar(740, 700, 12, 4, fill = 'paleGoldenRod')
    drawStar(70, 110, 12, 4, fill = 'paleGoldenRod')
    drawStar(220, 295, 12, 4, fill = 'paleGoldenRod')
    drawStar(739, 230, 12, 4, fill = 'paleGoldenRod')
    drawStar(395, 683, 12, 4, fill = 'paleGoldenRod')
    drawStar(124, 634, 12, 4, fill = 'paleGoldenRod')
    drawStar(98, 395, 12, 4, fill = 'paleGoldenRod')
    drawStar(423, 304, 12, 4, fill = 'paleGoldenRod')
    drawStar(583, 382, 12, 4, fill = 'paleGoldenRod')
    drawStar(473, 745, 12, 4, fill = 'paleGoldenRod')
  
def onKeyPress(app, key):
    if key == 'x':
        app.mode = 'gameOver'
    if app.playerColor == 'custom':
        if key == 'R':
            app.red += 20
            if app.red > 255 : app.red = 255
        elif key == 'r':
            app.red -= 20
            if app.red < 0 : app.red = 0
        elif key == 'G':
            app.green += 20
            if app.green > 255 : app.green = 255
        elif key == 'g':
            app.green -= 20
            if app.green < 0 : app.green = 0
        elif key == 'B':
            app.blue += 20
            if app.blue > 255 : app.blue = 255
        elif key == 'b':
            app.blue -= 20
            if app.blue < 0 : app.blue = 0
        app.color = rgb(app.red, app.green, app.blue)

def onKeyHold(app, keys):
    if app.mode == 'game':
        app.vx = 0
        if 'space' in keys and app.character.onGround:
            app.vy = -10
            app.character.onGround = False
        if 'right' in keys:
            app.vx = 5
        elif 'left' in keys:
            app.vx = -5

def onKeyRelease(app, key):
    if key in ['right', 'left']:
        app.vx = 0

def onStep(app):
    app.steps += 1
    if app.mode == 'game':
        app.score += 1.75
        if not app.character.onGround:
            app.vy += app.character.gravity
        app.worldY += app.vy
        if app.vx != 0:
            app.tunnel.moveHorizontal(app.vx)
            app.worldX += app.vx
        
        if app.vy != 0:
            app.tunnel.moveVertical(app.vy)
        #chatgpt start    
        app.tunnel.moveForward(app.forwardSpeed)

        makeBottomHorizontal(app)

        if app.score >= app.nextLevelScore:
            app.level += 1
            app.nextLevelScore += 250
            app.forwardSpeed += 1
            app.tunnel.incDifficulty(app.level)
        #chatgpt end

        if app.worldY > app.tunnel.depth:
            if app.score > app.highScore:
                app.highScore = app.score
            app.mode = 'gameOver'


def makeBottomHorizontal(app):
    if not standingOnPlatform(app, app.character):
        return
    if app.landingIndex == app.lastLandingIndex:
        return
    app.lastLandingIndex = app.landingIndex
    x1, y1, x2, y2, x3, y3, x4, y4 = app.currentPlatform
    if abs(y2-y1) > 5:
        oldCX = (x1+x2)/2
        xDifference = app.character.x - oldCX
        characterBottom = app.character.y + app.character.radius
        sign = -1 if xDifference > 0 else 1
        app.tunnel.rotateByAngle(sign*app.tunnel.sliceAngle)
        newPlatform = app.tunnel.rings[0]["platforms"][app.landingIndex]
        newX1, newY1, newX2, newY2 = newPlatform[:4]
        newCx = (newX1 + newX2)/2
        targetX = newCx + xDifference - app.character.x
        app.tunnel.moveHorizontal(targetX)
        app.tunnel.moveVertical(newY1 - characterBottom - 2)

def onMousePress(app, x, y):
    if app.mode == 'home':
        if 160 <= x <= 310 and 175 <= y <= 255:  
            resetGame(app)
            app.mode = 'game'
        elif 430 <= x <= 640 and 175 <= y <= 255:  
            app.mode = 'settings'
            
    elif app.mode == 'settings':
        if 100 <= x <= 160 and 680 <= y <= 740:
            app.playerColor = 'red'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 170 <= x <= 230 and 680 <= y <= 740:
            app.playerColor = 'orange'
        elif 310 <= x <= 370 and 680 <= y <= 740:
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 240 <= x <= 300 and 680 <= y <= 740:
            app.playerColor = 'yellow'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 310 <= x <= 370 and 680 <= y <= 740:
            app.playerColor = 'green'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 380 <= x <= 440 and 680 <= y <= 740:
            app.playerColor = 'blue'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 450 <= x <= 510 and 680 <= y <= 740:
            app.playerColor = 'purple'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 520 <= x <= 580 and 680 <= y <= 740:
            app.playerColor = 'pink'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.playerColor)
        elif 590 <= x <= 650 and 680 <= y <= 740:
            app.playerColor = 'custom'
            app.character = Character(app.width/2, app.height*3/4, 
                                      20, app.color)
        elif 20 <= x <= 110 and 20 <= y <= 110:
            app.mode = 'home'
        
    elif app.mode == 'game':
        if 690 <= x <= 780 and 20 <= y <= 110:
            app.mode = 'paused'

    elif app.mode == 'gameOver':
        resetGame(app)
        if 220 <= x <= 340 and 370 <= y <= 430:
            app.mode = 'home'
        elif 370 <= x <= 490 and 370 <= y <= 430:
            app.mode = 'settings'
            
    elif app.mode == 'paused':
        if 200 <= x <= 380 and 200 <= y <= 380:
            app.mode = 'home'
        elif 420 <= x <= 600 and 200 <= y <= 380:
            app.mode = 'settings'
        elif 310 <= x <= 490 and 420 <= y <= 600:
            app.mode = 'game'

def gameOverScreen(app):
    drawRect(60, 90, 680, 140, fill = 'white', 
             border = 'slateGrey', 
             borderWidth = 7)
    drawRect(80, 110, 640, 100, fill = 'maroon')
    drawLabel("GAME OVER", app.width/2, 160, size=105, 
              fill='white', 
                bold=True, font = 'monospace', 
                border = 'firebrick', 
                borderWidth = 4)
    drawRect(190, 250, 420, 100, fill = 'white',
              border = 'slateGrey', 
             borderWidth = 7)
    drawRect(205, 265, 390, 70, fill = 'maroon')
    drawLabel(f'Score: {app.score}', app.width/2, 285, size=40, fill='white', 
              bold=True, font='monospace')

    drawRect(220, 370, 120, 60, fill = 'white', 
             border = 'slateGrey', 
             borderWidth = 5)
    drawRect(370, 370, 220, 60, fill = 'white', 
             border = 'slateGrey', 
             borderWidth = 5)
    drawLabel('HOME', 280, 400, size = 40, fill = 'maroon', 
              bold = True, 
              font = 'monospace')
    drawLabel('SETTINGS', 480, 400, size = 40, fill = 'maroon', 
              bold = True, 
              font = 'monospace')
    
    drawOval(370, 640, 100, 45, rotateAngle = -70, 
             fill = app.color if app.playerColor == 'custom' else app.playerColor,
                border = 'slategrey', borderWidth = 5)
    drawOval(430, 640, 100, 45, rotateAngle = 70, 
             fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 5)
    drawOval(350, 600, 100, 45, rotateAngle = -50, 
             fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 5)
    drawOval(450, 600, 100, 45, rotateAngle = 50, 
             fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 5)
    drawLine(360, 520, 390, 600, lineWidth = 8, 
             fill = 'slategrey')
    drawLine(440, 520, 410, 600, lineWidth = 8, 
             fill = 'slategrey')
    
    drawCircle(360, 520, 15, 
               fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 5)
    drawCircle(440, 520, 15, 
               fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 5)
    
    drawCircle(400, 600, 60, 
               fill = app.color if app.playerColor == 'custom' else app.playerColor, 
               border = 'slategrey', borderWidth = 5)
    
    drawCircle(400, 600, 120, fill = None, border = 'maroon', 
               borderWidth = 12)
    drawLine(315, 515, 485, 685, fill = 'maroon', lineWidth = 14)
    drawLabel(f'High Score: {int(app.highScore)}',
              app.width/2, 315, size=30, fill='yellow', bold=True, font='monospace')

def homeScreen(app):
    drawLabel("RUN112", app.width/2, 100, size=120, 
              fill='white', bold=True,
             font = 'sansSerif', border= 'slateGrey', 
             borderWidth = 5)
    drawRect(160, 175, 150, 80, fill='green', border = 'white', 
             borderWidth = 4)
    drawLabel("PLAY", 235, 215, size=40, fill='white', 
              bold = True)
    drawRect(430, 175, 210, 80, fill='slateGrey', 
             border = 'white', borderWidth = 4)
    drawLabel("SETTINGS", 535, 215, size=38, fill='white', 
              bold = True)
    
    drawOval(290, 650, 200, 80, rotateAngle = -70, 
             fill = 'lightGrey', border = 'slateGrey', 
             borderWidth = 10)
    drawOval(510, 650, 200, 80, rotateAngle = 70, 
             fill = 'lightGrey', border = 'slateGrey', 
             borderWidth = 10)
    drawOval(230, 520, 200, 80, rotateAngle = -55, 
             fill = 'lightGrey', border = 'slateGrey', 
             borderWidth = 10)
    drawOval(570, 520, 200, 80, rotateAngle = 55, 
             fill = 'lightGrey', border = 'slateGrey', 
             borderWidth = 10)
    drawLine(280, 310, 380, 520, lineWidth = 15, 
             fill = 'slateGrey')
    drawLine(520, 310, 420, 520, lineWidth = 15, 
             fill = 'slateGrey')
    drawCircle(app.width/2, 520, 175, fill = 'lightGrey', 
               border = 'slateGrey', borderWidth = 10)
    drawCircle(280, 310, 30, fill = 'lightGrey', 
               border = 'slateGrey', borderWidth = 10)
    drawCircle(520, 310, 30, fill = 'lightGrey', 
               border = 'slateGrey', borderWidth = 10)
    drawOval(340, 480, 70, 90, borderWidth = 4, 
             fill = 'white', border= 'slateGrey')
    drawOval(460, 480, 70, 90, borderWidth = 4, 
             fill = 'white', border= 'slateGrey')
    drawCircle(350, 480, 15, fill = 'slateGrey')
    drawCircle(450, 480, 15, fill = 'slateGrey')
    drawCircle(342, 480, 15, fill = 'white')
    drawCircle(458, 480, 15, fill = 'white')

def settingsScreen(app):
    drawLabel("Choose Color", app.width/2, 70, size=70, 
              bold=True, fill='white', font='monospace')
    colorOptions = {
      'red': (100, 680),
        'orange': (170, 680),
        'yellow': (240, 680),
        'green': (310, 680),
        'blue': (380, 680),
        'purple': (450, 680),
        'pink': (520, 680),
        'custom':(590, 680)}

    for color, (x, y) in colorOptions.items():
        if color != 'custom':
            drawRect(x, y, 60, 60, fill = color)
        else:
            drawRect(x, y, 60, 60, fill = app.color)
        drawLabel(color.capitalize(), x + 30, y + 70, 
                  fill = 'white', font = 'monospace', bold = True, size = 15)
        drawRect(x, y+60, 68, 20)
        if app.playerColor == color:
            drawRect(x-4, y-4, 68, 68, border='lightSteelBlue',
                      borderWidth=5, fill=None)

    if app.playerColor == 'custom':
        drawLabel('Press R for more red', 725, 655, 
                  size = 11, fill = 'white', bold = True)
        drawLabel('Press r for less red', 725, 675, 
                  size = 11, fill = 'white', bold = True)
        drawLabel('Press G for more green', 725, 695, 
                  size = 11, fill = 'white', bold = True)
        drawLabel('Press g for less green', 725, 715, 
                  size = 11, fill = 'white', bold = True)
        drawLabel('Press B for more blue', 725, 735, 
                  size = 11, fill = 'white', bold = True)
        drawLabel('Press b for less blue', 725, 755, 
                  size = 11, fill = 'white', bold = True)
 
    drawRect(20, 20, 90, 90, fill = 'lightGrey', 
             border = 'slateGrey', borderWidth = 6)
    drawRect(45, 55, 40, 35, fill = 'lightSlateGrey')
    drawPolygon(65, 35, 35, 55, 95, 55, fill = 'slateGray')
    drawRect(58, 70, 14, 20, fill = 'lightGrey')

    drawOval(290, 530, 200, 80, rotateAngle = -70, 
             fill = app.color if 
             app.playerColor == 'custom' else app.playerColor,
                border = 'slategrey', borderWidth = 10)
    drawOval(510, 530, 200, 80, rotateAngle = 70, 
             fill = app.color if 
             app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawOval(230, 400, 200, 80, rotateAngle = -55, 
             fill = app.color if 
             app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawOval(570, 400, 200, 80, rotateAngle = 55, 
             fill = app.color if 
             app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawLine(280, 190, 380, 520, lineWidth = 15, 
             fill = 'slategrey')
    drawLine(520, 190, 420, 520, lineWidth = 15, 
             fill = 'slategrey')
    drawCircle(app.width/2, 400, 175, 
               fill = app.color if 
               app.playerColor == 'custom' else app.playerColor, border = 'slategrey', borderWidth = 10)
    drawCircle(280, 190, 30, 
               fill = app.color if 
               app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawCircle(520, 190, 30, 
               fill = app.color if 
               app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawOval(340, 360, 70, 90, borderWidth = 4, fill = 'white', 
             border = 'slategrey')
    drawOval(460, 360, 70, 90, borderWidth = 4, fill = 'white', 
             border = 'slategrey')
    drawCircle(350, 360, 15, fill = 'slategrey')
    drawCircle(450, 360, 15, fill = 'slategrey')
    drawCircle(342, 352, 9, fill = 'white')
    drawCircle(458, 352, 9, fill = 'white')

def gameScreen(app): 
    #chatgpt
    drawRect(690, 20, 90, 90, fill='lightGrey', border='white', 
             borderWidth=8)
    drawLine(722, 40, 722, 90, fill='white', lineWidth=12)
    drawLine(748, 40, 748, 90, fill='white', lineWidth=12)

    drawLabel(
        f"Score: {int(app.score)}",
        20, 30,
        fill='white', 
        size=30, bold=True,
        align='left'
    )

    drawLabel(
        f"Level: {app.level}",
        20, 60,
        fill='white',
        size=24, bold=True,
        align='left'
    )
def pauseScreen(app):
    drawRect(150, 150, 500, 500, fill = 'lightGrey', 
             border = 'white', borderWidth = 15, opacity = 85)

    drawRect(200, 200, 180, 180, fill = 'whiteSmoke', 
             border = 'grey', borderWidth = 6)
    drawRect(250, 280, 80, 70, fill = 'silver')
    drawPolygon(290, 230, 230, 280, 350, 280, fill = 'darkGrey')
    drawRect(276, 310, 28, 40, fill = 'whiteSmoke')

    drawRect(420, 200, 180, 180, fill = 'whiteSmoke', 
             border = 'grey', borderWidth = 6)
    drawCircle(510, 290, 50, fill = 'silver')
    drawRect(445, 280, 130, 20, fill = 'silver')
    drawRect(445, 280, 130, 20, fill = 'silver', 
             rotateAngle = 90)
    drawRect(445, 280, 130, 20, fill = 'silver', 
             rotateAngle = 45)
    drawRect(445, 280, 130, 20, fill = 'silver', 
             rotateAngle = -45)
    drawCircle(510, 290, 25, fill = 'whiteSmoke')

    drawRect(310, 420, 180, 180, fill = 'whiteSmoke', 
             border = 'grey', borderWidth = 6)
    drawPolygon(350, 180, 350, 450, 350, 570, 
                fill = 'darkGray')
    drawPolygon(450, 510, 350, 450, 350, 570, 
                fill = 'darkGray')
  

def main():
    runApp()

main()
