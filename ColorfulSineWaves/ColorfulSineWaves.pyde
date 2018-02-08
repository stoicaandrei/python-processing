
def setup():
    size(500, 500)
    colorMode(HSB)

angle = 0
    
def draw():
    global angle
    
    background(0)
    translate(width/2, height/2+50)
    off = 0
    ra = 0
    for i in range(-width/2 + 25, width/2 - 25, 25):
        h = map(sin(angle + off), -1, 1, 50, 150)
        w = map(h, 50, 150, 10, 24)
        fill((angle+off)**2%360, 255, 255)
        rect(i, 0, w, -h)
        off += 0.1
        
    angle += 0.05