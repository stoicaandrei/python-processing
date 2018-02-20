
def setup():
    size(400, 400)
    colorMode(HSB)
    
a = 100
b = 100
n1 = 0.5
n2 = 0.5
n3 = 0.5
m = 0.1
    
def draw():
    global n1, n2, n3, m
    if m < 2:
        m += 0.01
    else:
        m = 0.1
        n1 += random(0.2)
        n2 = random(n2, n1)
        n3 = random(n3, n1)
            
    translate(width/2, height/2)
    background(255)
    noFill()
    stroke(0)
    beginShape()
    t = 0
    while t < 12 * PI:
        fill(map(m, 0, 5, 0, 360), 255, 255)
        p1 = abs(1.0/a * cos(m/4*t)) ** n2
        p2 = abs(1.0/b * sin(m/4*t)) ** n3
        r = 1.0/((p1+p2)**(1/n1))
        
        x = r * cos(t)
        y = r * sin(t)
        vertex(x, y)
        
        t += 0.1
        
    endShape(CLOSE)