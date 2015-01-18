import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
#ball values
ball_pos=[WIDTH/2,HEIGHT/2];
ball_vel=[random.randrange(5,10),-random.randrange(4,8)];
#paddle values
paddle2_pos=HEIGHT/2;
paddle1_pos=HEIGHT/2;
paddle1_vel=paddle2_vel=0;
#scores
score1=score2=0;
# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel,hits # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2];
    if(right==True):
        ball_vel=[random.randrange(5,10),-random.randrange(4,8)];
    else:
        ball_vel=[-random.randrange(5,10),-random.randrange(4,8)];
      

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  
    ch=random.randrange(0,2);
    if(ch==0):
        ball_init(False);
    else:
        ball_init(True);
    #paddle values
    paddle2_pos=HEIGHT/2;
    paddle1_pos=HEIGHT/2;
    paddle1_vel=paddle2_vel=0;
    #scores
    score1=score2=0;    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,hits
 
    # update paddle's vertical position, keep paddle on the screen
    x1=paddle1_pos+paddle1_vel;
    if(x1<HALF_PAD_HEIGHT):
        x1=HALF_PAD_HEIGHT;
    elif(x1>HEIGHT-HALF_PAD_HEIGHT-1):
        x1=HEIGHT-1-HALF_PAD_HEIGHT
    x2=paddle2_pos+paddle2_vel;
    if(x2<HALF_PAD_HEIGHT):
        x2=HALF_PAD_HEIGHT;
    elif(x2>HEIGHT-HALF_PAD_HEIGHT-1):
        x2=HEIGHT-1-HALF_PAD_HEIGHT
    paddle1_pos=x1;
    paddle2_pos=x2;       
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #paddle1
    c.draw_polygon([[0, paddle1_pos+HALF_PAD_HEIGHT], [PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT ], [PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT],[0,paddle1_pos-HALF_PAD_HEIGHT]], 1, "Green", "Red");
    #paddle2
    c.draw_polygon([[WIDTH-1, paddle2_pos+HALF_PAD_HEIGHT], [WIDTH-1-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT ], [WIDTH-1-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT],[WIDTH-1,paddle2_pos-HALF_PAD_HEIGHT]], 1, "Green", "Blue");
    # update ball
    
    x1=ball_pos[0]+ball_vel[0];
    x2=ball_pos[1]+ball_vel[1];
    
    if(x2<BALL_RADIUS):
        x2=BALL_RADIUS;
        ball_vel[1]=-ball_vel[1];
    elif(x2>HEIGHT-1-BALL_RADIUS):
        x2=HEIGHT-1-BALL_RADIUS;
        ball_vel[1]=-ball_vel[1];
    if(x1<BALL_RADIUS+PAD_WIDTH):
       if(x2<paddle1_pos+HALF_PAD_HEIGHT and x2 > paddle1_pos-HALF_PAD_HEIGHT):
            x1=BALL_RADIUS+PAD_WIDTH+5;
            ball_vel[0]=-ball_vel[0]*1.1;
            ball_vel[1]=ball_vel[1]*1.1;
       else:
            score2=score2+1;
            ch=random.randrange(0,2);
            if(ch==0):
                ball_init(False);
            else:
                ball_init(True);
            return;    
    elif(x1> WIDTH-1-BALL_RADIUS-PAD_WIDTH) :  
        if(x2<paddle2_pos+HALF_PAD_HEIGHT and x2 > paddle2_pos-HALF_PAD_HEIGHT):
            x1=WIDTH-1-BALL_RADIUS-PAD_WIDTH-5;
            ball_vel[0]=-ball_vel[0]*1.1;
            ball_vel[1]=ball_vel[1]*1.1;
        else:
            score1=score1+1;
            ch=random.randrange(0,2);
            if(ch==0):
                ball_init(False);
            else:
                ball_init(True);
            return;
    
    
    ball_pos[0]=x1;
    ball_pos[1]=x2;           
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,2,"White","Orange"); 
    c.draw_text(str(score1),[WIDTH/4,100],50,"White");
    c.draw_text(str(score2),[WIDTH-WIDTH/4,100],50,"White");
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    temp=10
    #player1
    if(key==simplegui.KEY_MAP["W"]):
        paddle1_vel=-temp;
    if(key==simplegui.KEY_MAP["S"]):
        paddle1_vel=temp;
    #player2
    if(key==simplegui.KEY_MAP["up"]):
        paddle2_vel=-temp;
    if(key==simplegui.KEY_MAP["down"]):
        paddle2_vel=temp;
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    #player1
    if(key==simplegui.KEY_MAP["W"]):
        paddle1_vel=0;
    if(key==simplegui.KEY_MAP["S"]):
        paddle1_vel=0;
    #player2
    if(key==simplegui.KEY_MAP["up"]):
        paddle2_vel=0;
    if(key==simplegui.KEY_MAP["down"]):
        paddle2_vel=0;

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()
