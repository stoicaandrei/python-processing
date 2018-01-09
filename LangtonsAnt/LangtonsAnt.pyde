import random

dir, rectSize, rectOnLine, arr = 0, 2, 0, 0
antPos = 0
antDir = 0
name = ['Up', 'Right', 'Down', 'Left']

def setup():
    size(1000, 600)
    global rectOnLine, arr, antPos
    rectOnLine = width / rectSize
    arr = [[0 for i in range(rectOnLine)] for j in range(rectOnLine)]
    antPos = (rectOnLine / 2, rectOnLine / 2)
    center = rectOnLine / 2
    
    for i in range(rectOnLine):
        for j in range(rectOnLine):
            #stroke(255)
            fill(255)
            rect(i * rectSize, j * rectSize, rectSize, rectSize)
    
def draw():
    global antPos, arr, antDir
    
    for i in range(10000):
        x, y = antPos
        if arr[x][y]:
            antDir -= 1
        else:
            antDir += 1
            
        if antDir < 0:
            antDir = 3
        
        if antDir > 3:
            antDir = 0
        
        #stroke(255)
        arr[x][y] = not arr[x][y]
        if arr[x][y]:
            fill(0)
        else:
            fill(255)
        rect(x * rectSize, y * rectSize, rectSize, rectSize)
        
        if antDir == 0:
            y -= 1
        elif antDir == 1:
            x += 1
        elif antDir == 2:
            y += 1
        else:
            x -= 1
            
        if x == rectOnLine or x == -1 or y == rectOnLine or y == -1:
            x = random.randrange(0, rectOnLine)
            y = random.randrange(0, rectOnLine)
        
        antPos = (x, y)
    
    