width = 700;
height = 700;
class ball:
    def __init__(self, xpos,ypos,xspeed,yspeed,col):
        self.x = xpos;
        self.y = ypos;
        self.xspeed = xspeed;
        self.yspeed = yspeed;
        self.col = col;
        
    def update(self):
        if self.x > width:
            self.x =0;
        if self.y > height:
            self.y = 0;
        self.x = self.x + self.xspeed;
        self.y =self.y + self.yspeed;
        
    def display(self):
        fill(self.col);
        rectMode(CENTER);
        rect(self.x, self.y , 20,20);
    
#b1 = ball(10,50,5,0,color(0,255,0));
#b2 = ball(600,50,-5,0,color(0,0,255));
balls = [];
#balls.append(b1);
#balls.append(b2);
def setup():
    size(height,width);
    background(255);
    #frameRate(10);
def draw():

    #if b1.x == b2.x and b1.y == b2.y :
     #   print("collided");
        
    if mousePressed:
        balls.append( ball(mouseX,mouseY,random(-10,10),random(-10,10), color(random(0,255),random(0,255),random(0,255))));
        
    for i in range(len(balls)):
        balls[i].display();
        balls[i].update();
