import pygame
import sys
import time
import pygame.mixer
from pygame.locals import*
from classes import*
from process import*
from helpnew import*
from gameover import*
from main1 import *
from metro2 import*
import classes
from level import *
from startup import *
from full import*






pygame.init()

 


SCREEN_HEIGHT=360
SCREEN_WIDTH=640
 
def text_display(text,color):
   FONT=pygame.font.SysFont('monospace',25)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT



ic=pygame.image.load('extras/ino.png')
pygame.display.set_icon(ic)
screen=pygame.display.set_mode((640,360),0,32)


pygame.display.set_caption('SPACIO')
#toggle_fullscreen()
s_display(screen)
metro(screen)
clr1=(22,122,211)
clr2=(255,44,166)
clr3=(34,55,145)
white=(255,255,255)
red=(255,0,0)
clock=pygame.time.Clock()
FPS=24
total_frames=0
#background=pygame.image.load('Backgrounds/farback.gif')
bug=Bug(0,0,'ship/f1.png')
#fly=Fly(40,100,40,35,'fly.png')
#music=pygame.mixer.music.load('music.wav')
#pygame.mixer.music.play()
background1=pygame.image.load('Backgrounds/starfield.png')


background=pygame.image.load('extras/space.jpg')
life=pygame.image.load('life/enemy9.png')
life1=pygame.image.load('life/enemy2.png')
gem=pygame.image.load('ship/diamond5.gif')
times=pygame.image.load('ship/f5.gif')
t=pygame.image.load('extras/shell.gif')

a=text_display(str(bug.score),white)
SURFACER_a=a.get_rect()
SURFACER_a.center=(SCREEN_WIDTH-256-80,SCREEN_HEIGHT-15)


k=text_display('1180',white)
SURFACER_k=k.get_rect()
SURFACER_k.center=(SCREEN_WIDTH-256-80-150,SCREEN_HEIGHT-15)

music8=pygame.mixer.music.load('sound/Stellardrone - Billions And Billions.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)


while True:
      
    if classes.period.tr==1:

     
        for proj in classes.BugProjectile.List:
                      proj.destroy()
        for fly in classes.Fly.List:
                      fly.destroy(classes.Fly)
        for proj in classes.FlyProjectile.List:
                      proj.destroy()
        
        if bug.score>=1180:
               l_display(screen)
        else:
           t_display(screen)
           
        bug.destroy(Bug)
        metro(screen)
        
        clock=pygame.time.Clock()
        classes.period.sp=1
        classes.period.kl=0
        classes.period.tr=0
        bug=Bug(0,0,'ship/f1.png')
     
    for proj in classes.FlyProjectile.List:
            if pygame.sprite.spritecollide(proj,classes.Bug.List,False):
                proj.rectx=2*-proj.rect.width
                proj.destroy()
                bug.life+=1
                bug.rect.x=0
                bug.rect.y=0

    for fly in classes.Fly.List:
         
            if pygame.sprite.spritecollide(fly,classes.Bug.List,False):

                fly.health-=fly.half_health
                bug.life+=1   
                bug.rect.x=0
                bug.rect.y=0


    
    if bug.life==1:
               life1=pygame.image.load('life/enemy2.png')
    elif bug.life==2:
               life1=pygame.image.load('life/li2.gif')
                 
    elif bug.life==3:
               life1=pygame.image.load('life/li5.gif')
    elif bug.life==4:
               life1=pygame.image.load('life/li3.gif')
    elif bug.life==5:
               life1=pygame.image.load('life/li6.gif')
    elif bug.life==6:
               life1=pygame.image.load('life/li4.gif')
    elif bug.life==7:
               life1=pygame.transform.scale(life1,(0,0))
               bug.life=1
               bug.blood+=1
    if bug.blood==4:
             
               for proj in classes.BugProjectile.List:
                      proj.destroy()
               for fly in classes.Fly.List:
                      fly.destroy(classes.Fly)
               for proj in classes.FlyProjectile.List:
                      proj.destroy()
               bug.destroy(Bug)
               t_display(screen)
               clock=pygame.time.Clock()
               classes.period.sp=1
               classes.period.kl=0
               bug=Bug(0,0,'ship/f1.png')
              
    

    if classes.BugProjectile.fire:
       t=pygame.image.load('extras/shell.gif')
       for proj in classes.BugProjectile.List:
            proj.image=pygame.image.load('extras/shell.gif')
    elif not classes.BugProjectile.fire:
       t=pygame.image.load('extras/gun.gif')
       for proj in classes.BugProjectile.List:
            proj.image=pygame.image.load('extras/gun.gif')
    

    a=text_display(str(bug.score),white)
    
    l=process(bug,FPS,total_frames,screen)
  
  
    if l==1:
        bug=Bug(0,0,'ship/f1.png')

    
    screen.blit(background,(0,0))
    screen.blit(background1,(0,0))
    screen.blit(a,SURFACER_a)
   
    screen.blit(k,SURFACER_k)
    screen.blit(gem,(SCREEN_WIDTH-256-80-42,SCREEN_HEIGHT-30))
    screen.blit(gem,(SCREEN_WIDTH-256-80-210,SCREEN_HEIGHT-30))

    if bug.blood==1:
        screen.blit(times,(SCREEN_WIDTH-35,5))
        screen.blit(times,(SCREEN_WIDTH-35-23,5))
        screen.blit(times,(SCREEN_WIDTH-35-2*23,5))

    elif bug.blood==2:
        screen.blit(times,(SCREEN_WIDTH-35,5))
        screen.blit(times,(SCREEN_WIDTH-35-23,5))

    elif bug.blood==3:
        screen.blit(times,(SCREEN_WIDTH-35,5))
       


        
    screen.blit(t,(640-256-80-48-35,360-18))
   
    screen.blit(life1,(SCREEN_WIDTH-256,SCREEN_HEIGHT-32))

    screen.blit(life,(SCREEN_WIDTH-256,SCREEN_HEIGHT-32))
    

    bug.motion(SCREEN_WIDTH,SCREEN_HEIGHT)
    BugProjectile.movement(SCREEN_WIDTH)
    FlyProjectile.movement(SCREEN_WIDTH)

   
    Fly.update_all(SCREEN_WIDTH,SCREEN_HEIGHT)
   
    total_frames+=1

    
    
    BaseClass.allsprites.draw(screen)
    BugProjectile.List.draw(screen)
    FlyProjectile.List.draw(screen)


    pygame.display.flip()
    clock.tick(FPS)





    
