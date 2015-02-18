import pygame
import sys
import classes,random
from pygame.locals import*
from metro2 import*
import pygame.mixer
from full import*

def process(bug,FPS,total_frames,screen):
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
        
                classes.BugProjectile.fire= not  classes.BugProjectile.fire
                
            if event.key==pygame.K_ESCAPE:
              b=metrow(screen)
              if b==2:
                classes.period.sp=1
                classes.period.kl=0
                for proj in classes.BugProjectile.List:
                    proj.destroy()
                    
                for bug in classes.Bug.List:
                    bug.destroy(classes.Bug)
               
                for proj in classes.FlyProjectile.List:
                    proj.destroy()
                  
                
                for fly in classes.Fly.List:
                    fly.destroy(classes.Fly)
                
                    
                return 1
              elif b==1:
                pass
                
                
            
            if event.key==pygame.K_d:
                classes.Bug.going_right=True
                #bug.image=pygame.image.load('ship/f1.png')
                bug.velx=5
            elif event.key==pygame.K_a:
                classes.Bug.going_right=False
                #bug.image=pygame.image.load('ship/f1.png')
              
                bug.velx=-5
            elif event.key==pygame.K_w:
                bug.vely=-5
            elif event.key==pygame.K_s:
                bug.vely=+5
            
        if event.type==pygame.KEYUP:
             if event.key==pygame.K_d:
                 bug.velx=0
             elif event.key==pygame.K_a:
                 bug.velx=0
             elif event.key==pygame.K_s:
                 bug.vely=0
             elif event.key==pygame.K_w:
                 bug.vely=0
            

            
  
    
              
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:

            def direction():
                
              p.velx=8
                
            if (classes.BugProjectile.fire):
                p=classes.BugProjectile(bug.rect.x+bug.rect.width-10,bug.rect.y
                                        +(bug.rect.height/2)-2,'extras/shell.gif')
                direction()
                
            else:
                p=classes.BugProjectile(bug.rect.x+bug.rect.width,bug.rect.y,
                                        'extras/gun.gif')
                direction()

    if classes.period.sp in(1,2,3):
       spawn(FPS,total_frames,bug)
       spawn1(FPS,total_frames)
    else:
       spawn1(FPS,total_frames)
       spawn2(FPS,total_frames,bug)
       spawn3(FPS,total_frames,bug)

    collisions(bug)
    return 0
  

def spawn(FPS,total_frames,bug):
    five_seconds=FPS*5
    if total_frames%five_seconds==0 and bug.spawn<=6:
       
        
        x=640-64
        y=random.randint(30,360-70)
        
        #classes.Fly(x,y,'e_f1.png')
        bug.spawn+=1
       
        if classes.period.sp==1:
          classes.Fly(x,y,'chopper/chopper1.gif')
        elif classes.period.sp==2:
          classes.Fly(x,y,'extras/e_f1.png')
        elif classes.period.sp==3:
           classes.Fly(x,y,'extras/alien10001.png')
        
def spawn2(FPS,total_frames,bug):
    five_seconds=FPS*5
    if total_frames%five_seconds==0 and bug.spawn==0:
       
        
        x=640-64
        y=random.randint(30,360-70)
        
        #classes.Fly(x,y,'e_f1.png')
        bug.spawn+=1
       
        if classes.period.sp==4:
           classes.Fly(x,y,'spacenew1/speedship.png')
        elif classes.period.sp==5:
           classes.Fly(x,y,'spacenew1/smallfreighterspr.png')

        elif classes.period.sp==6:
           classes.Fly(640-120,180,'spacenew1/heavyfreighter.png')
            
        


def spawn1(FPS,total_frames):
    four_seconds=FPS*5
    music1=pygame.mixer.Sound('sound/laser1.wav')
    music2=pygame.mixer.Sound('sound/laser8.wav')
    music3=pygame.mixer.Sound('sound/laser5.wav')
    music1.set_volume(0.7)
    music2.set_volume(0.7)
    music3.set_volume(0.7)
    if total_frames%four_seconds==0:
        for fly in classes.Fly.List:
          if fly.stat==1:
            p=classes.FlyProjectile(fly.rect.x-fly.rect.width-40,fly.rect.y+5
                                    ,'extras/bullet.png')
            p.velx=-10
           
  
            
            music1.play()


          elif fly.stat==2:
            p=classes.FlyProjectile(fly.rect.x-fly.rect.width-50,fly.rect.y+8
                                    ,'Enemy/bulgp.gif')
            p.velx=-12
           
          
            music2.play()
            
          elif fly.stat==3:
              p=classes.FlyProjectile(fly.rect.x-(fly.rect.width)-21,fly.rect.y+30
                                    ,'Enemy/bul2.gif')
              p.velx=-12
             
              
              music3.play()

          


def spawn3(FPS,total_frames,bug):
    two_seconds=FPS*2
    music4=pygame.mixer.Sound('sound/laser8.wav')
    music5=pygame.mixer.Sound('sound/laser6.wav')
    music6=pygame.mixer.Sound('sound/laser11.wav')
    music4.set_volume(0.7)
    music5.set_volume(0.7)
    music6.set_volume(0.7)
    if total_frames%two_seconds==0 and bug.spawn==1:
        for fly in classes.Fly.List:
          if fly.stat==4:
              p=classes.FlyProjectile(fly.rect.x-fly.rect.width-50,fly.rect.y+25
                                    ,'Enemy/bul3.gif')
              p.velx=-14
              
              
              music4.play()
          if fly.stat==5:

              
              p=classes.FlyProjectile(fly.rect.x-(fly.rect.width/2)-7,fly.rect.y+20
                                    ,'Enemy/bul4.gif')
              p.velx=-12
              
              
              music5.play()

          if fly.stat==6:
              
             
              p=classes.FlyProjectile(fly.rect.x-(fly.rect.width/2)-35,fly.rect.y+30
                                    ,'Enemy/bul5.gif')
              p.velx=-14

              p=classes.FlyProjectile(fly.rect.x-(fly.rect.width/2)-35,fly.rect.y+72
                                    ,'Enemy/bul5.gif')
              p.velx=-14
            
         
              music6.play()
              
             

              

def collisions(bug):
    for fly in classes.Fly.List:
       if pygame.sprite.spritecollide(fly,classes.BugProjectile.List,False):

           if classes.BugProjectile.fire:
               fly.health-=fly.half_health
               bug.score+=5
               
               

           else:
                fly.velx=0


    for proj in classes.BugProjectile.List:
            if pygame.sprite.spritecollide(proj,classes.Fly.List,False):
                proj.rectx=2*-proj.rect.width
                proj.destroy()

    
       
    
    

            


                
            
            

       
       
        
    


    
