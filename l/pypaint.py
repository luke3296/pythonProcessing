width_ = 1400;
height_ = 800;
colours = [[0,0,0],[255,0,0],[0,255,0],[0,0,255],
               [20,40,60],[60,0,40],[0,70,30],[20,40,0],
               [200,0,200],[100,0,0],[200,85,0],[0,48,48],
               [180,0,0],[0,0,180],[255,255,255]];
_size = 25;
size_ = 25;
centers = [25,118,211,305,398,491,585,678,717,865,958,1051,1145,1238,1331];
colList = [0,0,0];
c = color(0,0,0); 
def getColourFromMouse( x, y):
    for i in range (len(colours)):
        if (((mouseX - centers[i]) ** 2) + ((mouseY - _size)**2)) <= 100+(_size**2):
            #globalCol =  color(colours[i][0],colours[i][1],colours[i][2]);
            print(colours[i][0],colours[i][1],colours[i][2]);
            #return [colours[i][0],colours[i][1],colours[i][2]];
            global c;
            c = color(colours[i][0],colours[i][1],colours[i][2]);
          #  print("in range of col");
   
            
def setup():
    
    size(1400,800);
    
 
    for i in range( len(colours)):
        noStroke();
        fill(colours[i][0],colours[i][1],colours[i][2]);
        ellipse(i*width/15 +size_, size_, size_, size_);
        print(i*width/15 + size_);
        

def draw():
    if mousePressed:
        getColourFromMouse(mouseX,mouseY);
        noStroke();
        fill(c);
        ellipse(mouseX,mouseY,25,25);
    if keyPressed and keyCode == SHIFT:
        background(209);
        setup();