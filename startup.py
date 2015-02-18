import pygame
import sys
from pygame.locals import*





def text_display(text,color,size):
   FONT=pygame.font.SysFont('monospace',size)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT


def s_display(screen):
  white=(255,255,255)
  red=(255,0,0)
  green=(0,255,0)
  x,y,z=255,0,0
  clr=(x,y,z)
  SCREEN_HEIGHT=360
  SCREEN_WIDTH=640


  a=text_display('SPACIO',clr,90)

  d=text_display('Loading...',white,30)
  r=1

  SURFACER_a=a.get_rect()

  SURFACER_a.center=(320,160)
  SURFACER_d=d.get_rect() 
  SURFACER_d.center=(340,260)
  background1=pygame.image.load('extras/space.jpg')
  background2=pygame.image.load('Backgrounds/starfield.png')
  
  img=pygame.image.load('Ship/f1.png')

  FPS=30
  imgx=-20
  imgy=360-40
  pixMove=7
  call=0
  tr=0


  fpsTime=pygame.time.Clock()

  


  while True:
    
    imgx+=pixMove
    if tr==FPS*6:
        return
        
    if imgx>640+69:
        imgx=-10
        
    if call==6:
        img=pygame.image.load('Ship/f2.png')
    if call==12:
        img=pygame.image.load('Ship/f3.png')
    if call==18:
        img=pygame.image.load('Ship/f4.png')
    if call==18:
        img=pygame.image.load('Ship/f1.png')
        call=6
    call+=2

   
    screen.blit(background1,(0,0))
    screen.blit(background2,(0,0))
    screen.blit(a,SURFACER_a)
    screen.blit(d,SURFACER_d)
    screen.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
      
    z+=1
    clr=(x,y,z)
    
    if z==255:
        z=0
    a=text_display('SPACIO',clr,90)

    if r in(1,2,3,4,5,6,7,8,9,10):
      d=text_display('Loading...',green,30)
      r+=1
    elif r in(11,12,13,14,15,16,17,18,19):
      d=text_display('Loading...',white,30)
      r+=1
    if r==20:
        r=1
      

    fpsTime.tick(FPS)
    tr+=1
    
    pygame.display.update()




   
    


