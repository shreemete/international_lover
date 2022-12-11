
import pygame,sys
from pygame.locals import *
import random2


pygame.init()

w,h=1550,800
window=pygame.display.set_mode((w,h))

bg=(100,149,237)
pygame.display.set_caption("Game Project")

#boxes colour:
deactive=(120,160,250)
active=(255,255,255)
#table
tb=(100,200,255)
tbg=(200,100,250)

score=0
# color
# bg=(200,100,250)
txt_col=(80,0,80)
white=(255,255,255)
black=(0,0,0)
red=(220,0,0)
bright_red=(255,0,0)
green=(0,220,0)
bright_green=(0,255,0)
blue=(0,0,255)
org=(255,60,7)
btn_col=(64,10,128)
yellow=(255,255,0)
faintBlue=(100,120,200)
bright_faintBlue=(130,150,200)

#Text
#home
f=pygame.font.Font('freesansbold.ttf',24)
text_home=f.render('Home',True,(200,30,150))
tr_home=text_home.get_rect()
tr_home.center=(130,100)
#Back
text_exit=f.render('Exit',True,(200,30,150))
tr_exit=text_exit.get_rect()
tr_exit.center=(130,200)
#Play
text_play=f.render('Play',True,(200,30,150))
tr_play=text_play.get_rect()
tr_play.center=(750,400)


#images
#home
image1=pygame.image.load('home.png')
image1=pygame.transform.scale(image1,(30,30))
#back
image2=pygame.image.load('close.png')
image2=pygame.transform.scale(image2,(30,30))
#play
image8=pygame.image.load('play_btn.png')
image8=pygame.transform.scale(image8,(30,30))


def get_font(size):
    text_font = pygame.font.Font( 'freesansbold.ttf', size )
    return text_font

def display_text(text,font,col,x,y):
    textwindow = font.render( text, True, col )
    textRect=textwindow.get_rect()
    textRect.center=x,y
    window.blit(textwindow,textRect)

def btn(btn_width,btn_height,x,y,btn_bg,br_size,text,font,text_col,action):
    pygame.draw.rect( window, btn_bg, (x, y, btn_width, btn_height), br_size )
    display_text(text,font,text_col,x+(btn_width//2),y+(btn_height//2))

    mouse = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()

    if ((x < mouse[0] < x + btn_width) and (y < mouse[1] < y + btn_height)):
        pygame.draw.rect( window, bg, (x, y, btn_width, btn_height) )
        display_text( text, font, btn_bg, x + (btn_width // 2), y + (btn_height // 2) )
        if br_size==0:
            br_size=2

        pygame.draw.rect( window, white, (x, y, btn_width, btn_height), br_size )
        if press[0] == 1 and action != None :
            action()

# def exit_out():
#
#     pygame.draw.rect( window, white, (520, 250, 500, 200), 3)
#     pygame.draw.rect( window, bg, (520, 250, 500, 200) )
#     display_text("Do You Want to Exit ? ",get_font(30),white,780,300)
#     btn(120,60,580,350,bright_red,0,'Yes',get_font(30),white,game_loop)
#     btn( 120, 60, 840, 350, blue, 0, 'No', get_font( 30 ), white, home_page )

def button():
    home = window.blit( text_home, tr_home )
    exit = window.blit( text_exit, tr_exit )
    home_box = pygame.draw.rect( window, deactive, (30, 75, 150, 50), 1 )
    exit_box = pygame.draw.rect( window, deactive, (30, 175, 150, 50), 1 )
    home_image = window.blit( image1, (40, 83) )
    exit_image = window.blit( image2, (40, 183) )

    mouse = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()
    if (150 > mouse[0] > 30 and 75 < mouse[1] < 125):
        home_box = pygame.draw.rect( window, active, (30, 75, 150, 50), 1 )
        if press[0] == 1 :
            home_page()
    elif (150 > mouse[0] > 30 and 175 < mouse[1] < 225):
        exit_box = pygame.draw.rect( window, active, (30, 175, 150, 50), 1 )
        if press[0] == 1 :
            quit()

    else:
        home_box = pygame.draw.rect( window, deactive, (30, 75, 150, 50), 1 )
        exit_box = pygame.draw.rect( window, deactive, (30, 175, 150, 50), 1 )

def player_out():

    pygame.draw.rect( window, white, (520, 250, 500, 200), 3)
    pygame.draw.rect( window, bg, (520, 250, 500, 200) )
    display_text("Do You Want to Replay ? ",get_font(30),white,780,300)
    btn(120,60,580,350,blue,0,'Replay',get_font(30),white,game_loop)
    btn( 120, 60, 840, 350, bright_green, 0, 'Home', get_font( 30 ), white, home_page )


def game_loop():
    global score
    # Ball
    bx = 775
    by = 685
    bcl = (0, 0, 0)

    # rect

    rx = 675
    ry = 700
    rcl = (155, 10, 100)

    # ball motion:
    l_x = [-10, -9, -8, 8, 9, 10]
    l_y = [7, 8, 9, 10]
    rbx = random2.choice( l_x )
    rby = random2.choice( l_y )

    count =0

    while True:
        Menu_Mouse_Pos=pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # if event.type==pygame.MOUSEBUTTONDOWN:
            #     if checkInputforHome(Menu_Mouse_Pos):
            #         home_loop()
            #     if checkInputforExit(Menu_Mouse_Pos):
            #         exit_loop()

        window.fill( bg )
        pygame.draw.rect( window, tb, (200, 0, 1150, 800), 10 )
        pygame.draw.rect( window, tbg, (210, 10, 1130, 780) )
        bat = pygame.draw.rect( window, rcl, (rx, ry, 200, 30) )
        ball = pygame.draw.circle( window, bcl, (bx, by), 15 )

        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            if rx >= 225:
                rx -= 10
                if rx < bx < rx + 200 and ry - 15 == by:
                    rbx = (rbx + 1)
        if press[pygame.K_RIGHT]:
            if rx <= 1125:
                rx += 10
                if rx < bx < rx + 200 and ry - 15 == by:
                    rby = (rby + 1)

        if bx <= 224:
            rbx = (-rbx)
        if by <= 24:
            rby = (-rby)
            rbx = rbx

        if bx >= 1321:
            rbx = (-rbx)
            rby = rby


        if by > 760:
            f=open('data','r')
            sc=f.read()
            f.close()
            score=count
            if int(sc)<count:
                f=open("data",'w')
                f.write(str(count))
                f.close()
            player_out()
        else:
            bx -= rbx
            by -= rby

        if rx-2 < bx < rx + 200+2 and ry - 15 == by:
            rbx = (rbx)
            rby = -(rby)
            count+=1

        if bx == rx + 200 + 15 and ry-2 < by < ry + 30+2:
            rbx = (rbx + 1)
            rby = -rby
            count+=1
        if bx == rx - 15 and ry < by < ry + 30 + 15:
            rbx = -(rbx)
            rby = rby + 1
            count+=1
        if bx == rx - 15 and by == ry - 15:
            rbx = -(rbx + 1)
            rby = rby + 1
            count+=1

        button()
        display_text("Score : ",get_font(25),white,1200,30)
        display_text( str(count), get_font( 25 ), white, 1270, 30 )
        pygame.display.update()
        pygame.time.Clock().tick( 40 )

def home_page():
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        window.fill(bg)
        display_text("Welcome to My Game Project",get_font(40),white,780,200)
        display_text( "Your Score : ", get_font( 30 ), white, 780, 280 )

        display_text( str(score), get_font( 30 ), white, 880, 280 )
        display_text( "Best Score : ", get_font(  35 ), black, 780, 340 )
        f1=open('data','r')
        b_score=f1.read()
        display_text( str(b_score), get_font( 35 ), black, 890, 340 )
        btn(120,60,500,450,bright_green,0,"Play",get_font(30),white,game_loop)
        btn( 120, 60, 900, 450, bright_red, 0, "Exit", get_font( 30 ), white, quit)
        pygame.draw.rect( window, (255, 255, 255), (200, 40, 1150, 720), 4 )


        pygame.display.update()

if __name__ == '__main__':
    home_page()