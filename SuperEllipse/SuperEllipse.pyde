
def setup():
    size(500,500)
    background(255)
    colorMode(HSB)
    
a = 1
b = 1
n = 5
r = 100
i = 0
back = False

def sgn(w):
    if w < 0:
        return -1
    elif w > 0:
        return 1
    else:
        return 0

def draw():
    global n, back
    translate(width/2, height/2)
    
    background(255)
    fill(map(n, 0, 5, 0, 360), 255, 255)
    noStroke()
    beginShape()
    
    if not back:
        n -= 0.05
    else:
        n += 0.05
    if n < 0.1:
       back = True
    if n > 5:
        back = False
    
    t = 0
    while (t < 2*PI):
        x = abs(cos(t))**(2/n) * a * sgn(cos(t)) * r
        y = abs(sin(t))**(2/n) * b * sgn(sin(t)) * r
        vertex(x,y)
        
        t += 0.1
    endShape(CLOSE)
    
    
