import random

dir, rectSize, rectOnLine, arr = 0, 2, 0, 0
x, y = 0, 0
antDir = 0

colors = [(255, 255, 255), (255, 51, 0), (0, 255, 0), (0, 255, 255),\
          (255, 255, 0), (153, 0, 255), (204, 102, 153), (51, 51, 0), \
          (153, 102, 51), (0, 0, 153)]
numColors = len(colors)

ANTUP = 0;
ANTRIGHT = 1;
ANTDOWN = 2;
ANTLEFT = 3;

def setup():
    size(900, 900)
    global rectOnLine, arr, x, y
    rectOnLine = width / rectSize
    arr = [[0 for i in range(rectOnLine)] for j in range(rectOnLine)]
    x = rectOnLine / 2
    y = rectOnLine / 2
    
    for i in range(rectOnLine):
        for j in range(rectOnLine):
            stroke(255)
            fill(255)
            rect(i * rectSize, j * rectSize, rectSize, rectSize)
            
def TurnRight():
    global antDir
    antDir += 1
    if antDir > ANTLEFT:
        antDir = ANTUP

def TurnLeft():
    global antDir
    antDir -= 1
    if antDir < ANTUP:
        antDir = ANTLEFT
        
def MoveForward():
    global x, y, arr
    
    arr[x][y] += 1
    if arr[x][y] == numColors:
        arr[x][y] = 0
    r, g, b = colors[arr[x][y]]
    stroke(r, g, b)
    fill(r, g, b)
    rect(x * rectSize, y * rectSize, rectSize, rectSize)
    
    if antDir == ANTUP:
        y -= 1
    elif antDir == ANTRIGHT:
        x += 1
    elif antDir == ANTDOWN:
        y += 1
    else:
        x -= 1
        
    if x == rectOnLine or x == -1 or y == rectOnLine or y == -1:
        x = random.randrange(0, rectOnLine)
        y = random.randrange(0, rectOnLine)
    # if x == rectOnLine:
    #     x = 0
    # elif x == -1:
    #     x = rectOnLine - 1
    # elif y == rectOnLine:
    #     y = 0
    # elif y == -1:
    #     y = rectOnLine - 1
                    
                                                    
def draw():
    for i in range(1000):
        MoveForward()
        if arr[x][y] in (0, 2, 3, 4, 7): #change those numbers
            TurnLeft()
        else:
            TurnRight()
        
    
    