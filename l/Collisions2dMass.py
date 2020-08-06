width = 800;
height = 800;
balls = [];
size_ = 15;
radiusFactor = 0.5;
arrowSize = 3.5;
timeStep = 5;

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
        self.Py = self.mass * self.yspeed;
        self.Px = self.mass * self.xspeed;
        
        
    def update(self):
        if self.x > width:
            self.x =1;
        if self.y > height:
            self.y = 1;
        if self.x < 0:
            self.x =width-1;
        if self.y < 0:
            self.y = height-1;
        
        self.x = self.x + self.xspeed/timeStep;
        self.y =self.y + self.yspeed/timeStep;
        
    def display(self):
        
        fill(self.col);
        ellipse(self.x, self.y , self.mass,self.mass);
        pushStyle();
        strokeWeight(2)
        line(self.x, self.y, self.x + self.xspeed + arrowSize, self.y+self.yspeed+arrowSize);
        popStyle();
        
        
def newV(a,b):
    #for a
    v1x = ( ((a.mass - b.mass)/(a.mass+b.mass))*a.xspeed  +  ((2*b.mass)/(a.mass+b.mass))*b.xspeed); 
    v1y = ( ((a.mass - b.mass)/(a.mass+b.mass))*a.yspeed  +  ((2*b.mass)/(a.mass+b.mass))*b.yspeed); 
    #for b
    v2x=( ((2*a.mass)/(a.mass+b.mass))*a.xspeed  + ((b.mass-a.mass)/(b.mass+a.mass))*b.xspeed);
    v2y=( ((2*a.mass)/(a.mass+b.mass))*a.yspeed  + ((b.mass-a.mass)/(b.mass+a.mass))*b.yspeed);
    
    return [v1x,v1y,v2x,v2y];
    
def setup():
    background(209);
    size(width,height);
    frameRate(15);
    
def draw():

    background(209);
    if mousePressed:
        balls.append(ball(mouseX,mouseY,random(-5,5),random(-5,5),random(20,40),color(random(0,255),random(0,255),random(0,255))));
    
    for k in range(timeStep):    
        for i in range(0,len(balls), +1):
            balls[i].update();
            balls[i].display();
    
    
            if(len(balls) > 0):
                for j in range(len(balls)-1, 0, -1):
                    if( i != j):
                        if(collided(balls[i].x, balls[i].y, balls[j].x, balls[j].y,balls[i].mass,balls[j].mass)):
                    
                            speeds = newV(balls[i], balls[j]);
                            balls[i].xspeed = speeds[0];
                            balls[i].yspeed = speeds[1];
                        
                            balls[j].xspeed = speeds[2];
                            balls[j].yspeed = speeds[3];
                    
                      
                        #collisions = collisions + 1;
                            print("collisions");

        
