import pygame
import sys
from pygame.locals import*
from helpnew import*


class stat:
   loc=1

def text_display(text,color):
   FONT=pygame.font.SysFont('monospace',50)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT

def rext_display(text,color):
   FONT=pygame.font.SysFont('monospace',15)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT

def metro(screen):
 white=(255,255,255)
 red=(255,0,0)
 green=(0,255,0)
 yellow = (255,255,0)


 SCREEN_HEIGHT=360
 SCREEN_WIDTH=640

 a=text_display('Start',red)
 b=text_display('Help',white)
 c=text_display('Exit',white)
 d=rext_display('Spacio 1.0 |Pi Accessible Learning Environment',white)

 SURFACER_a=a.get_rect()
 SURFACER_b=b.get_rect()
 SURFACER_c=c.get_rect()
 SURFACER_d=d.get_rect()
 SURFACER_a.center=(320,90)
 SURFACER_b.center=(320,180)
 SURFACER_c.center=(320,270)
 SURFACER_d.center=(320,345)
 background1= pygame.image.load('extras/space.jpg')
 background2=pygame.image.load('Backgrounds/starfield.png')

 while True:
    screen.blit(background1,(0,0))
    screen.blit(background2,(0,0))
    screen.blit(a,SURFACER_a)
    screen.blit(b,SURFACER_b)
    screen.blit(c,SURFACER_c)
    screen.blit(d,SURFACER_d)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                stat.loc=stat.loc+1
                if stat.loc==4:
                    stat.loc=1
                
            if event.key==pygame.K_w:
                stat.loc=stat.loc-1
                if stat.loc==0:
                    stat.loc=3
            if event.key==pygame.K_RETURN:
                if stat.loc==3:
                    pygame.quit()
                    sys.exit()
                if stat.loc==1:
                   return
                
                if stat.loc==2:
                    txt_display(screen)
                    

                    
                
    a=text_display('Start',white)                
    b=text_display('Help',white)
    c=text_display('Exit',white)            
    if stat.loc==1:
        a=text_display('Start',red)
       
    elif stat.loc==2:
        b=text_display('Help',red)
    elif stat.loc==3: 
        c=text_display('Exit',red)
       

    pygame.display.update()


   
    


