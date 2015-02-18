import pygame
from random import randint
import math
from process import *
import pygame.mixer




class period:
    sp=1
    tr=0
    kl=0
    
    
class BaseClass(pygame.sprite.Sprite):

    allsprites=pygame.sprite.Group()
    def __init__(self,x,y,image_string):

        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image=pygame.image.load(image_string)

        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y
        
        

    def destroy(self,ClassName):
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self
        
        

class Bug(BaseClass):
    List=pygame.sprite.Group()
    going_right=True
    def __init__(self,x,y,image_string):

        BaseClass.__init__(self,x,y,image_string)
        Bug.List.add(self)
        self.velx,self.vely=0,0
        self.jumping,self.go_down=False,False
        self.life=1
        self.blood=1
        self.call=0
        self.score=0
        self.spawn=0
        
        
       
        

    def motion(self,SCREENWIDTH,SCREENHEIGHT):
        predicted_location=self.rect.x+self.velx
        if predicted_location<0:
           self.velx=0
        elif predicted_location+(self.rect.width)>SCREENWIDTH:
           self.velx=0
        predicted_location1=self.rect.y+self.vely

        if predicted_location1+(self.rect.height)>SCREENHEIGHT:
           self.vely=0
        elif predicted_location1<0:
           self.vely=0

        if self.call==6:
            self.image=pygame.image.load('ship/f2.png')
        if self.call==12:
            self.image=pygame.image.load('ship/f3.png')
        if self.call==18:
            self.image=pygame.image.load('ship/f4.png')
        if self.call==24:
            self.image=pygame.image.load('ship/f1.png')
            self.call=6

        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.call+=2
        
        
        if period.kl==10:
            
               period.sp=2
               

        elif period.kl==20:
              
               period.sp=3
               
               
        elif period.kl==30:
              
               period.sp=4

        elif period.kl==35:
              
               period.sp=5

        elif period.kl==40:
            
               
               period.sp=6
        
           
           
        

  

class Fly(BaseClass):
    List=pygame.sprite.Group()
    def __init__(self,x,y,image_string):
         BaseClass.__init__(self,x,y,image_string)
         Fly.List.add(self)
         self.call=0
         self.health=100
         self.half_health=100
         self.stat=period.sp
         self.vely=0
         self.velx=0
         if self.stat==1:
           self.velx=-randint(3,6)
         elif self.stat==2:
           self.velx=-randint(3,6)
           self.half_health=50
         elif self.stat==3:
             self.velx=5
             self.half_health=30
         elif self.stat==4:
             self.velx=0
             self.vely=6
             self.half_health=10
         elif self.stat==5:
             self.velx=5
             self.vely=5
             self.half_health=10
         elif self.stat==6:
             self.velx=0
             self.vely=-7
             self.half_health=4
         
         
         
             
         
         
         #self.amplitude,self.period=randint(20,30),randint(4,5)/100.0

    @staticmethod
    def update_all(SCREENWIDTH,SCREENHEIGHT):
        for fly in Fly.List:
            fly.fly(SCREENWIDTH,SCREENHEIGHT)
            if fly.health<=0:
                if fly.stat==period.sp:
                   period.kl+=1
                if fly.stat==6:
                    period.tr=1
                for bug in Bug.List:
                    bug.spawn-=1
                fly.destroy(Fly)
            
    def fly(self,SCREENWIDTH,SCREENHEIGHT):
        predicted_location=self.rect.x+self.velx
        if predicted_location<0:
           self.velx=-self.velx
        elif predicted_location+self.rect.width>SCREENWIDTH:
           self.velx=-self.velx
        predicted_location1=self.rect.y+self.vely

        if predicted_location1+self.rect.height>SCREENHEIGHT:
           self.vely=-self.vely
        elif predicted_location1<0:
           self.vely=-self.vely
        '''if self.rect.x+self.rect.width>SCREENWIDTH or self.rect.x<0:
            #self.image=pygame.transform.flip(self.image,True,False)
            self.velx=-self.velx
        if self.rect.y+self.rect.height>SCREENHEIGHT or self.rect.y<0:
            #self.image=pygame.transform.flip(self.image,True,False)
            self.vely=-self.vely'''
        if self.stat==2:
         if self.call==6:
            self.image=pygame.image.load('extras/e_f2.png')
         elif self.call==12:
            self.image=pygame.image.load('extras/e_f3.png')
         elif self.call==18:
            self.image=pygame.image.load('extras/e_f4.png')
         elif self.call==24:
            self.image=pygame.image.load('extras/e_f5.png')
         elif self.call==30:
            self.image=pygame.image.load('extras/e_f6.png')
         elif self.call==36:
            self.image=pygame.image.load('extras/e_f1.png')
            self.call=6
        if self.stat==1:
          if self.call==6:
            self.image=pygame.image.load('chopper/chopper1.gif')
            self.image=pygame.transform.flip(self.image,True,False)
          elif self.call==12:
            self.image=pygame.image.load('chopper/chopper2.gif')
            self.image=pygame.transform.flip(self.image,True,False)
          elif self.call==18:
            self.image=pygame.image.load('chopper/chopper3.gif')
            self.image=pygame.transform.flip(self.image,True,False)
            self.call=6
        if self.stat==4:
            if self.call==300:
                self.velx=-5
                self.vely=0
            elif self.call==600:
                self.vely=6
                self.velx=0
                self.call=0
        if self.stat==5:
            if self.call%600==0:
                self.velx+=1
                self.vely+=2
                if self.vely==11:
                    self.velx=5
                    self.vely=5
        if self.stat==6:
            if self.call==300:
                self.velx=-7
                self.vely=0
            elif self.call==596:
                self.vely=8
                self.velx=0
                self.call=0
            
                
        '''if self.stat==3: 
            
          if self.call==2:
            self.image=pygame.image.load('alien10002.png')
          elif self.call==4:
            self.image=pygame.image.load('alien10003.png')
          elif self.call==6:
            self.image=pygame.image.load('alien10004.png')
          elif self.call==8:
            self.image=pygame.image.load('alien10005.png')
          elif self.call==10:
            self.image=pygame.image.load('alien10006.png')
          elif self.call==12:
            self.image=pygame.image.load('alien10007.png')
          elif self.call==14:
            self.image=pygame.image.load('alien10008.png')
          elif self.call==16:
            self.image=pygame.image.load('alien10009.png')
          elif self.call==18:
            self.image=pygame.image.load('alien10010.png')
          elif self.call==20:
            self.image=pygame.image.load('alien10011.png')
          elif self.call==22:
            self.image=pygame.image.load('alien10012.png')
          elif self.call==24:
            self.image=pygame.image.load('alien10013.png')
          elif self.call==26:
            self.image=pygame.image.load('alien10014.png')
          elif self.call==28:
            self.image=pygame.image.load('alien10015.png')
          elif self.call==30:
            self.image=pygame.image.load('alien10001.png')
            self.call=2'''
            
        
        self.rect.x+=self.velx
        self.rect.y+=self.vely
       
        #self.rect.y=self.amplitude*math.sin(self.period*self.rect.x)+ 30
        

        self.call+=2
    #@staticmethod
    #def movement(SCREENWIDTH):
     #   for fly in Fly.List:
        #    fly.fly(SCREENWIDTH)




class BugProjectile(pygame.sprite.Sprite):
    List=pygame.sprite.Group()
    normal_list=[]
    fire=True
    def __init__(self,x,y,image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_string)

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

       
        try:
            last_element=BugProjectile.normal_list[-1]
            difference=abs(self.rect.x-last_element.rect.x)

            if difference<self.rect.width+40:
                return


        except Exception:
            pass
            
        BugProjectile.normal_list.append(self)
        BugProjectile.List.add(self)
        self.velx=None
        music=pygame.mixer.Sound('sound/laser4_0.wav')
        music.set_volume(0.9)
        music.play()


    @staticmethod
    def movement(SCREENWIDTH):
        for projectile in BugProjectile.List:
            projectile.rect.x+=projectile.velx
            
            if projectile.rect.x+projectile.rect.width<0:
                projectile.destroy()
            elif projectile.rect.x>SCREENWIDTH:
                projectile.destroy()
                
           
              
    def destroy(self):
        BugProjectile.List.remove(self)
        BugProjectile.normal_list.remove(self)
        del self

class FlyProjectile(pygame.sprite.Sprite):
    List=pygame.sprite.Group()
    normal_list=[]
    fire=True
    def __init__(self,x,y,image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_string)

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
  
        

        

        '''try:
            last_element=FlyProjectile.normal_list[-1]
            difference=abs(self.rect.x-last_element.rect.x)

            if difference<self.rect.width:
                return


        except Exception:
            pass'''
            
        FlyProjectile.normal_list.append(self)
        FlyProjectile.List.add(self)
        self.velx=None

    @staticmethod
    def movement(SCREENWIDTH):
        for projectile in FlyProjectile.List:
            projectile.rect.x+=projectile.velx
            
            if projectile.rect.x+projectile.rect.width<0:
                projectile.destroy()
            elif projectile.rect.x>SCREENWIDTH:
                projectile.destroy()
                
           
              
    def destroy(self):
        FlyProjectile.List.remove(self)
        FlyProjectile.normal_list.remove(self)
        del self

        
















        
        

    
