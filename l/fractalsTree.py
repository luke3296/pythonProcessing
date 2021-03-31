angle = 80;
branch_ratio = 0.67;
branch_num = 50;
feature_size = 6;

def setup():
    global f
    f = createFont("Arial", 16, True) 
    global  angle;
    angle = 80;
    global branch_ratio;
    branch_ratio = 0.67;
    size(800,800);
    
def draw():
    global f
    global branch_num;
    global branch_ratio;
    global angle;
    background(51);
    stroke(255);
    global feature_size;
    textFont(f,16)            
    fill(255)
    txt = str("W/S branch ratio: "+ str(branch_ratio)+" A/D branch num: "+ str(branch_num)+" mouse left/right angle: "+ str(angle) + " R/T feature Size " + str(feature_size))       
    text(txt,0,16)
    if keyPressed:
        if key == 'a':
            branch_num += 5;
        elif key == 'd':
            branch_num -= 5;
        elif key == 'w':
            branch_ratio += 0.01;
        elif key == 's':
            branch_ratio -= 0.01;
        elif key == 'r':
            if(feature_size > 2):
                feature_size -= 1;
        elif key =='t':
            if(feature_size < 28):
                feature_size +=1;
    translate(width/2, height);            
    branch(branch_num);
        

    
def branch(len):
    global angle
    global branch_ratio;
    global feature_size;
    line(0,0,0,-len);
    translate(0, -len);
    if(len > feature_size):
        pushMatrix();
        rotate( angle);
        branch(len * branch_ratio);
        popMatrix();
        pushMatrix();
        rotate( -angle)
        branch(len * branch_ratio);
        popMatrix();

def mousePressed(): 
    global angle;
    if mouseButton == LEFT:
        angle -= 0.1;
    elif mouseButton == RIGHT:
        angle += 0.1;
