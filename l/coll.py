
width = 1400;
height = 800;
balls = [];
ballPos = [];
size_ = 25;
def collided(x,y,x2,y2):
    if(((x-x2)**2 + (y-y2)**2) <= 2*(size_**2)):
        return True;
    else:
        return False;
def reset():
    balls = [];
    
class ball:
    #global balls; 
    #global ballPos;
    def __init__(self, xpos,ypos,xspeed,yspeed,col):
        self.x = xpos;
        self.y = ypos;
        self.xspeed = xspeed;
        self.yspeed = yspeed;
        self.col = col;
        #self.index = len(balls);
        
        
    def update(self):
        if self.x > width:
            self.x =1;
        if self.y > height:
            self.y = 1;
        if self.x < 0:
            self.x =width-1;
        if self.y < 0:
            self.y = height-1;
        
        self.x = self.x + self.xspeed;
        self.y =self.y + self.yspeed;
        #ballPos[self.index] = [self.x + self.xspeed, self.y + self.yspeed];
        
    def display(self):
        fill(self.col);
        #rectMode(CENTER);
        ellipse(self.x, self.y , size_,size_);
a = ball(0,0,5,5,color(12,23,34));

def setup():
    background(209);
    size(width,height);
    frameRate(20);
def draw():
    background(209);
    if mousePressed:
        balls.append(ball(mouseX,mouseY,random(-5,5),random(-5,5),color(random(0,255),random(0,255),random(0,255))));
        
    for i in range(0,len(balls), +1):
        balls[i].update();
        balls[i].display();
    
    
        if(len(balls) > 0):
            for j in range(len(balls)-1, 0, -1):
                if( i != j):
                    if(collided(balls[i].x, balls[i].y, balls[j].x, balls[j].y)):
                        balls[i].xspeed = balls[i].xspeed  *-1;
                        balls[j].xspeed  = balls[j].xspeed  *-1;
                        balls[i].yspeed  = balls[i].yspeed  *-1;
                        balls[j].yspeed  = balls[j].yspeed  *-1;
                        print("collided");
                        
    
    if keyPressed and keyCode == SHIFT:
        print("reset");
        reset();
        setup();
