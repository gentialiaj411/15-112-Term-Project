from cmu_graphics import *
import math
import random
class Platform:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        drawRect(self.x - self.width/2, self.y - self.height/2,
                 self.width, self.height, fill = self.color)
    
    
            
    

class Tunnel:
    def __init__(self, numSides, segments, spacing, radius, depth, cx, cy):
        self.numSides = numSides
        self.segments = segments
        self.spacing = depth/segments
        self.radius = radius
        self.depth = depth
        self.cx = cx
        self.cy = cy
        self.rotationOffset = 0
        self.rotationSpeed = 0.1
        self.sliceAngle = 2*math.pi / self.numSides
        self.rotation = 0
        self.vx = 10
        self.speed = 0.1
        self.rings = []
        self.chance = 0.10
        self.chanceIncrement = 0.02
        self.platforms = []
        self.holes = []
        self.xDisplacement = 0
        self.yDisplacement = 0
        self.initializeRings()



    def initializeRings(self):
        for i in range(self.segments):
            z = i * self.spacing
            ring = self.generateRing(z)
            self.rings.append(ring)
    

    def generateRing(self,z):
        platforms = []
        holes = []
        for side in range(self.numSides):
            angle = self.rotationOffset + side * self.sliceAngle
            nextAngle = self.rotationOffset + (side+1)*self.sliceAngle
            scale = 1 - (z / self.depth)
            r1 = self.radius * scale
            r2 = self.radius * (1 - ((z + self.spacing) / self.depth))

            x1 = self.cx + math.cos(angle)*r1
            y1 = self.cy + math.sin(angle)*r1
            x2 = self.cx + math.cos(nextAngle)*r1
            y2 = self.cy + math.sin(nextAngle)*r1
            x3 = self.cx + math.cos(nextAngle)*r2
            y3 = self.cy + math.sin(nextAngle)*r2
            x4 = self.cx + math.cos(angle)*r2
            y4 = self.cy + math.sin(angle)*r2

            platforms.append((x1,y1,x2,y2,x3,y3,x4,y4))
            if abs(z-(self.depth-self.spacing)) < 10**-5:
                holes.append(random.random() < self.chance)
            else:
                holes.append(False)
        return {"z" : z, "platforms": platforms, "holes": holes}
    #chatgpt start
    def incDifficulty(self, level):
        self.chance = min(
            1.0,
            self.chance + self.chanceIncrement * (level - 1)
        )
    #end
    def moveForward(self, speed):
        for ring in self.rings:
            ring["z"] -= speed
        if self.rings[0]["z"] < -self.spacing:
            self.rings.pop(0)
            lastZ = self.rings[-1]["z"]
            newRing = self.generateRing(lastZ + self.spacing)
            sideHoleIndex = random.randrange(self.numSides)
            newRing["holes"] = [i == sideHoleIndex for i in 
                                range(self.numSides)]
            self.rings.append(newRing)
            self.recalculatePlatforms()


    def recalculatePlatforms(self):
        for ring in self.rings:
            z = ring["z"]
            scale = max(0,min(1,1 - (z/self.depth)))
            nextScale = max(0,min(1, 1-((z+self.spacing)/self.depth)))
            newPlatforms = []
            r1 = self.radius * scale
            r2 = self.radius * nextScale
            for i in range(self.numSides):
                angle = self.rotationOffset + i * self.sliceAngle
                nextAngle = angle + self.sliceAngle
                x1 = self.cx + math.cos(angle) * r1 - self.xDisplacement
                y1 = self.cy + math.sin(angle) * r1 - self.yDisplacement
                x2 = self.cx + math.cos(nextAngle) * r1 - self.xDisplacement
                y2 = self.cy + math.sin(nextAngle) * r1 - self.yDisplacement
                x3 = self.cx + math.cos(nextAngle) * r2 - self.xDisplacement
                y3 = self.cy + math.sin(nextAngle) * r2 - self.yDisplacement
                x4 = self.cx + math.cos(angle) * r2 - self.xDisplacement
                y4 = self.cy + math.sin(angle) * r2 - self. yDisplacement
                


                newPlatforms.append((x1,y1,x2,y2,x3,y3,x4,y4))
            ring["platforms"] = newPlatforms            
        
        
    
    def rotateByAngle(self, angle):
        self.rotationOffset += angle
        self.recalculatePlatforms()
        

    def draw(self):
        drawRect(0, 0, app.width, app.height, fill='black')
        sortedRings = sorted(self.rings, key = lambda ring: ring["z"], 
                             reverse = True)
        farthestZ = self.depth
        for ring in sortedRings:
            z = ring["z"]
            platforms = ring["platforms"]
            holes = ring["holes"]
            minGreen = 50
            maxGreen = 250
            if z > self.depth:
                continue
            scale = max(0, min(1, 1 - (z/farthestZ)))
            for i, platform in enumerate(platforms):
                if i >= len(holes):
                    continue
                x1, y1, x2, y2, x3, y3, x4, y4 = platform
                
                if z < self.depth*0.4:
                    opacity = 100
                else:
                    fade = (z - self.depth*0.4)/(self.depth*0.5)
                    opacity = max(0,100*(1-fade))
                if holes[i]:
                    fillColor = 'black'
                else:
                    greenValue = int(minGreen+(maxGreen-minGreen)*scale)
                    fillColor = rgb(0,greenValue,0)
                drawPolygon(x1,y1,x2,y2,x3,y3,x4,y4, 
                            fill = fillColor, opacity = opacity)
    def isHole(self, ringIndex, segmentIndex):
        return self.rings[ringIndex]["holes"][segmentIndex]

    
    def moveHorizontal(self, amount):
        self.xDisplacement += amount
        for ring in self.rings:
            updatedPlatforms = []
            for platform in ring["platforms"]:
                x1, y1, x2, y2, x3, y3, x4, y4 = platform
                updatedPlatforms.append((x1-amount, y1, x2-amount, y2, 
                                         x3-amount, y3, x4-amount, y4))
            ring["platforms"] = updatedPlatforms
    
    def moveVertical(self, amount):
        self.yDisplacement += amount
        for ring in self.rings:
            updatedPlatforms = []
            for platform in ring["platforms"]:
                x1, y1, x2, y2, x3, y3, x4, y4 = platform
                updatedPlatforms.append((x1, y1-amount, x2, y2-amount, 
                                         x3, y3-amount, x4, y4-amount))
            ring["platforms"] = updatedPlatforms
                
        
                
    
    
        



    

        
        

   
    


