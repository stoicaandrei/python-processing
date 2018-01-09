import random

arr = None
rectSize = 10
rectOnLine = 0

def setup():
    size(600, 600)
    
    global arr, rectSize, rectOnLine
    rectOnLine = width/rectSize
    arr = [[0 for i in range(rectOnLine)] for i in range(rectOnLine)]
    
    for i in range(rectOnLine):
        for j in range(rectOnLine):
            if random.random() <= 0.5:
                arr[i][j] = 1
    
def draw():
    global arr, rectSize, rectOnLine
    for i in range(rectOnLine):
        for j in range(rectOnLine):
            stroke(102)
            if arr[i][j]:
                fill(255)
            else:
                fill(0)
            rect(i * rectSize, j * rectSize, rectSize, rectSize)
            
    narr = [[0 for i in range(rectOnLine)] for i in range(rectOnLine)]
    for i in range(rectOnLine):
        for j in range(rectOnLine):
            n = nCount(i, j)
            if not arr[i][j] and n == 3:
                narr[i][j] = 1
            elif arr[i][j] and (n < 2 or n > 3):
                narr[i][j] = 0
            else:
                narr[i][j] = arr[i][j]
    arr = narr
            
def nCount(x, y):
    n = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            try:
                if arr[nx][ny]:
                    n += 1
            except:
                n = n
    if arr[x][y]:
        n -= 1
    return n