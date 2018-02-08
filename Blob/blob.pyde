def setup():
    size(500, 500)

yoff = 0

def draw():
    background(0)
    global yoff
    
    r = 100
    translate(width/2, height/2)
    beginShape()
    a = 0
    xoff = 0
    while a < 2 * PI:
        a += 0.1
        
        off = map(noise(xoff , yoff), 0, 1, -25, 25)
        r += off
        xoff += 0.1
        x = r * cos(a)
        y = r * sin(a)
        r = 100
        vertex(x, y)
    endShape()
    
    yoff += 0.05