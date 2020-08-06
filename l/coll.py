width = 800;
height = 800;
balls = [];
size_ = 15;
radiusFactor = 0.5;

def collided(x,y,x2,y2,m1,m2):
    if( (((x-x2)**2 + (y-y2)**2) - 100 ) <=  radiusFactor*((m1**2)+(m2**2))   <= ((x-x2)**2 + (y-y2)**2) + 100): #this is not good edge detection
        return True;
    else:
        return False;
def reset():
    balls = [];
    setup();
    
class ball:

    def __init__(self, xpos,ypos,xspeed,yspeed,mass,col):
        self.x = xpos;
        self.y = ypos;
        self.xspeed = xspeed;
        self.yspeed = yspeed;
        self.mass = mass;
        self.col = col;
        
        
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
        
    def display(self):
        fill(self.col);
        ellipse(self.x, self.y , self.mass,self.mass);
        

def setup():
    background(209);
    size(width,height);
    frameRate(15);
    
def draw():

    background(209);
    if mousePressed:
        balls.append(ball(mouseX,mouseY,random(-5,5),random(-5,5),random(10,30),color(random(0,255),random(0,255),random(0,255))));
        
    for i in range(0,len(balls), +1):
        balls[i].update();
        balls[i].display();
    
    
        if(len(balls) > 0):
            for j in range(len(balls)-1, 0, -1):
                if( i != j):
                    if(collided(balls[i].x, balls[i].y, balls[j].x, balls[j].y,balls[i].mass,balls[j].mass)):
                        balls[i].xspeed = balls[i].xspeed  *-1;
                        balls[j].xspeed  = balls[j].xspeed  *-1;
                        balls[i].yspeed  = balls[i].yspeed  *-1;
                        balls[j].yspeed  = balls[j].yspeed  *-1;
                        #collisions = collisions + 1;
                        print("collisions");
                        
    
    if keyPressed and keyCode == SHIFT:
        print("reset");
        reset();
