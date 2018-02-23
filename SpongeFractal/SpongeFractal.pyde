a = 0
bo = 1
allBoxes = []

def setup():
    
    size(500, 500, P3D)
    global bo, allBoxes
    bo = Box(0, 0, 0, 200)
    allBoxes.append(bo)
    
    


def draw():
    global a, allBoxes
    background(51)
    translate(width/2, height/2)
    fill(255, 100)
    
    rotateX(a)
    rotateY(-a*0.4)
    a += 0.01
    for b in allBoxes:
        b.show()
    
    
    
class Box:
    
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        
    def chop(self):
        boxes = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if abs(x) + abs(y) + abs(z) > 1:
                        newR = self.r / 3
                        b = Box(self.x+x*newR, self.y+y*newR, self.z+z*newR, newR)
                        boxes.append(b)
        return boxes
        
    def show(self):
        pushMatrix()
        translate(self.x, self.y, self.z)
        fill(self.x+ self.y+ self.z, 50)
        box(self.r)
        popMatrix()
        
def mousePressed():
    global allBoxes
    newB = []
    for b in allBoxes:
        newB += b.chop()
    allBoxes = newB