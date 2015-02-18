import pygame
import sys
from pygame.locals import*

class stat:
   loc=1

def text_display(text,color):
   FONT=pygame.font.SysFont('monospace',30)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT

def txt_display(screen):
   yellow = (255,255,0)
   SCREEN_HEIGHT=360
   SCREEN_WIDTH=640

   white=(255,255,255)
   red=(255,0,0)
   green=(0,255,0)
   background1=pygame.image.load('extras/space.jpg')
   background2=pygame.image.load('Backgrounds/starfield.png')

   aa=text_display('W -> Up',white)
   bb=text_display('D -> Right',white)
   cc=text_display('S -> Down',white)
   dd=text_display('A -> Left',white)
   ee=text_display('SPACE -> Shoot',white)
   ff=text_display('E -> Weapon Change',white)
   gg=text_display('ENTER -> Select/Action',white)
   hh=text_display('RETURN TO MENU',white)
   SURFACER_aa=aa.get_rect()
   SURFACER_aa.center=(320,40)

   
   SURFACER_bb=bb.get_rect()
   SURFACER_bb.center=(320,80)
  
   SURFACER_cc=cc.get_rect()
   SURFACER_cc.center=(320,120)

   SURFACER_dd=dd.get_rect()
   SURFACER_dd.center=(320,160)

   SURFACER_ee=ee.get_rect()
   SURFACER_ee.center=(320,200)
   
   SURFACER_ff=ff.get_rect()
   SURFACER_ff.center=(320,240)
  
   SURFACER_gg=gg.get_rect()
   SURFACER_gg.center=(320,280)
   
   SURFACER_hh=hh.get_rect()
   SURFACER_hh.center=(320,320)
   



   while True:
    screen.blit(background1,(0,0))
    screen.blit(background2,(0,0))
    screen.blit(aa,SURFACER_aa)
    screen.blit(bb,SURFACER_bb)
    screen.blit(cc,SURFACER_cc)
    screen.blit(dd,SURFACER_dd)
    screen.blit(ee,SURFACER_ee)
    screen.blit(ff,SURFACER_ff)
    screen.blit(gg,SURFACER_gg)
    screen.blit(hh,SURFACER_hh)
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                stat.loc=stat.loc+1
                if stat.loc==9:
                    stat.loc=1
            if event.key==pygame.K_ESCAPE:
                return
                
            if event.key==pygame.K_w:
                stat.loc=stat.loc-1
                if stat.loc==0:
                    stat.loc=8
            if event.key==pygame.K_RETURN:
                if stat.loc==8:
                    
                    return
                    
                
                    
     
    a=text_display('W -> Up',white)     
    aa=text_display('W -> Up',white)
    bb=text_display('D -> Right',white)
    cc=text_display('S -> Down',white)
    dd=text_display('A -> Left',white)
    ee=text_display('SPACE -> Shoot',white)
    ff=text_display('E -> Weapon Change',white)
    gg=text_display('ENTER -> Select/Action',white)
    hh=text_display('RETURN TO MENU',white)
   
   
   

    if stat.loc==1:
        aa=text_display('W -> Up',red)
    elif stat.loc==2:
        bb=text_display('D -> Right',red)
    elif stat.loc==3: 
        cc=text_display('S -> Down',red)
    elif stat.loc==4:
        dd=text_display('A -> Left',red)
    elif stat.loc==5:
        ee=text_display('SPACE -> Shoot',red)
    elif stat.loc==6:
        ff=text_display('E -> Weapon Change',red)
    elif stat.loc==7:
        gg=text_display('ENTER -> Select/Action',red)
    elif stat.loc==8:
        hh=text_display('RETURN TO MENU',red)
                        
       

    pygame.display.update()
    #txt_display(screen,aa,bb,cc,dd,ee,ff,gg,hh)
   





