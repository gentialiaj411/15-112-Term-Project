from cmu_graphics import *
class Backgrounds:
  def __init__(self):
    pass  
  def __init__(self):
    pass
<<<<<<< HEAD
  

  def draw(self):
=======
    
  def drawBackground(self):
>>>>>>> 005f8c88a9c3031ad7140c973bb0e08f208a192d
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

  def drawHomeScreen(app):
    drawLabel("RUN112", app.width/2, 100, size=120, fill='white', bold=True,
             font = 'sansSerif', border= 'slateGrey', borderWidth = 5)
    drawRect(160, 175, 150, 80, fill='green', border = 'white', borderWidth = 4)
    drawLabel("PLAY", 235, 215, size=40, fill='white', bold = True)
    drawRect(430, 175, 210, 80, fill='slateGrey', border = 'white', borderWidth = 4)
    drawLabel("SETTINGS", 535, 215, size=38, fill='white', bold = True)
    
    drawOval(290, 650, 200, 80, rotateAngle = -70, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawOval(510, 650, 200, 80, rotateAngle = 70, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawOval(230, 520, 200, 80, rotateAngle = -55, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawOval(570, 520, 200, 80, rotateAngle = 55, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawLine(280, 310, 380, 520, lineWidth = 15, fill = 'slateGrey')
    drawLine(520, 310, 420, 520, lineWidth = 15, fill = 'slateGrey')
    drawCircle(app.width/2, 520, 175, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawCircle(280, 310, 30, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawCircle(520, 310, 30, fill = 'lightGrey', border = 'slateGrey', borderWidth = 10)
    drawOval(340, 480, 70, 90, borderWidth = 4, fill = 'white', border= 'slateGrey')
    drawOval(460, 480, 70, 90, borderWidth = 4, fill = 'white', border= 'slateGrey')
    drawCircle(350, 480, 15, fill = 'slateGrey')
    drawCircle(450, 480, 15, fill = 'slateGrey')
    drawCircle(342, 480, 15, fill = 'white')
    drawCircle(458, 480, 15, fill = 'white')
    
  def drawSettings(app):
    drawLabel("Choose Color", app.width/2, 70, size=70, bold=True, fill='white', font='monospace')
    colorOptions = 
      {'red': (100, 680),
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
        drawLabel(color.capitalize(), x + 30, y + 70, fill = 'white', font = 'monospace', bold = True, size = 15)
        drawRect(x, y+60, 68, 20)
        if app.playerColor == color:
            drawRect(x-4, y-4, 68, 68, border='lightSteelBlue', borderWidth=5, fill=None)

    if app.playerColor == 'custom':
        drawLabel('Press R for more red', 725, 655, size = 11, fill = 'white', bold = True)
        drawLabel('Press r for less red', 725, 675, size = 11, fill = 'white', bold = True)
        drawLabel('Press G for more green', 725, 695, size = 11, fill = 'white', bold = True)
        drawLabel('Press g for less green', 725, 715, size = 11, fill = 'white', bold = True)
        drawLabel('Press B for more blue', 725, 735, size = 11, fill = 'white', bold = True)
        drawLabel('Press b for less blue', 725, 755, size = 11, fill = 'white', bold = True)
 
    drawRect(20, 20, 90, 90, fill = 'lightGrey', border = 'slateGrey', borderWidth = 6)
    drawRect(45, 55, 40, 35, fill = 'lightSlateGrey')
    drawPolygon(65, 35, 35, 55, 95, 55, fill = 'slateGray')
    drawRect(58, 70, 14, 20, fill = 'lightGrey')

    drawOval(290, 530, 200, 80, rotateAngle = -70, fill = app.color if app.playerColor == 'custom' else app.playerColor,
                border = 'slategrey', borderWidth = 10)
    drawOval(510, 530, 200, 80, rotateAngle = 70, fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawOval(230, 400, 200, 80, rotateAngle = -55, fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawOval(570, 400, 200, 80, rotateAngle = 55, fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawLine(280, 190, 380, 520, lineWidth = 15, fill = 'slategrey')
    drawLine(520, 190, 420, 520, lineWidth = 15, fill = 'slategrey')
    drawCircle(app.width/2, 400, 175, fill = app.color if app.playerColor == 'custom' else app.playerColor, border = 'slategrey', borderWidth = 10)
    drawCircle(280, 190, 30, fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawCircle(520, 190, 30, fill = app.color if app.playerColor == 'custom' else app.playerColor, 
                border = 'slategrey', borderWidth = 10)
    drawOval(340, 360, 70, 90, borderWidth = 4, fill = 'white', border = 'slategrey')
    drawOval(460, 360, 70, 90, borderWidth = 4, fill = 'white', border = 'slategrey')
    drawCircle(350, 360, 15, fill = 'slategrey')
    drawCircle(450, 360, 15, fill = 'slategrey')
    drawCircle(342, 352, 9, fill = 'white')
    drawCircle(458, 352, 9, fill = 'white')

  def drawGameOver(self):
    pass

  def drawGameScreen(self):
    drawRect(690, 20, 90, 90, fill = 'lightGrey', border = 'white', borderWidth = 8)
    drawLine(722, 40, 722, 90, fill = 'white', lineWidth = 12)
    drawLine(748, 40, 748, 90, fill = 'white', lineWidth = 12)
    drawLabel(f'Score: {app.score}', 10, 25, size = 35, bold = True, border = 'white',
                borderWidth = 2, align = 'left')

  def drawPause(self):
    drawRect(150, 150, 500, 500, fill = 'lightGrey', border = 'white', borderWidth = 15, opacity = 85)

    drawRect(200, 200, 180, 180, fill = 'whiteSmoke', border = 'grey', borderWidth = 6)
    drawRect(250, 280, 80, 70, fill = 'silver')
    drawPolygon(290, 230, 230, 280, 350, 280, fill = 'darkGrey')
    drawRect(276, 310, 28, 40, fill = 'whiteSmoke')

    drawRect(420, 200, 180, 180, fill = 'whiteSmoke', border = 'grey', borderWidth = 6)
    drawCircle(510, 290, 50, fill = 'silver')
    drawRect(445, 280, 130, 20, fill = 'silver')
    drawRect(445, 280, 130, 20, fill = 'silver', rotateAngle = 90)
    drawRect(445, 280, 130, 20, fill = 'silver', rotateAngle = 45)
    drawRect(445, 280, 130, 20, fill = 'silver', rotateAngle = -45)
    drawCircle(510, 290, 25, fill = 'whiteSmoke')

    drawRect(310, 420, 180, 180, fill = 'whiteSmoke', border = 'grey', borderWidth = 6)
    drawPolygon(350, 180, 350, 450, 350, 570, fill = 'darkGray')
    drawPolygon(450, 510, 350, 450, 350, 570, fill = 'darkGray')
  
