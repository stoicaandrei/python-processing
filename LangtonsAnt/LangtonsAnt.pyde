import random

dir, rectSize, rectOnLine, arr = 0, 2, 0, 0
x, y = 0, 0
antDir = 0

ANTUP = 0;
ANTRIGHT = 1;
ANTDOWN = 2;
ANTLEFT = 3;

def setup():
    size(1000, 1000)
    global rectOnLine, arr, antPos
    rectOnLine = width / rectSize
    arr = [[0 for i in range(rectOnLine)] for j in range(rectOnLine)]
    antPos = (rectOnLine / 2, rectOnLine / 2)
    center = rectOnLine / 2
    
    for i in range(rectOnLine):
        for j in range(rectOnLine):
            stroke(0)
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
    
    arr[x][y] = not arr[x][y]
    stroke(0)
    fill(255)
    if arr[x][y]:
        fill(0)
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
                    
def draw():
    for i in range(10):
        MoveForward()
        if arr[x][y]:
            TurnLeft()
        else:
            TurnRight()
        
    
    