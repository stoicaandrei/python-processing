n = 0
c = 6

def setup():
    size(600, 600)
    background(0)
    colorMode(HSB)
    frameRate(120)
    
def draw():
    global n
    
    a = n * 157.6
    r = c * n ** 0.5
    x = r * cos(a);
    y = r * sin(a);
    
    translate(width/2,height/2)
    fill(a % 256, 255, 255)
    ellipse(x, y, 8, 8)
    n += 1