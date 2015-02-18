import pygame
import sys
from pygame.locals import*
from main1 import *





def text_display(text,color,size):
   FONT=pygame.font.SysFont('monospace',size)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT


def l_display(screen):
  white=(255,255,255)
  red=(255,0,0)
  green=(0,255,0)
  x,y,z=255,0,0
  clr=(x,y,z)
  SCREEN_HEIGHT=360
  SCREEN_WIDTH=640


  a=text_display('LEVEL',clr,70)
  b=text_display('COMPLETE',clr,70)

  d=text_display('Press Esc To Return',white,20)

  SURFACER_a=a.get_rect()
  SURFACER_b=b.get_rect()

  SURFACER_a.center=(320,120)
  SURFACER_d=d.get_rect() 
  SURFACER_d.center=(320,280)
  SURFACER_b.center=(320,200)
  background1=pygame.image.load('extras/space.jpg')
  background2=pygame.image.load('Backgrounds/starfield.png')

  


  while True:
    screen.blit(background1,(0,0))
    screen.blit(background2,(0,0))
    screen.blit(a,SURFACER_a)
    screen.blit(d,SURFACER_d)
    screen.blit(b,SURFACER_b)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
      
        if event.type==pygame.KEYDOWN:

            if event.key==K_ESCAPE:
                metro(screen)
                return
    z+=1
    clr=(x,y,z)
    
    if z==255:
        z=0
    a=text_display('LEVEL',clr,70)
    b=text_display('COMPLETE',clr,70)
        
    
    pygame.display.update()


    


