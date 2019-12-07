from random import randint
import pygame
class Candy:
    
    _instance = None

    class __Candy:   
        def __init__(self):
            self.x=randint(10,790)
            self.y=randint(10,590)
            self.thickness=20
            
            
            
        def display(self,screen):
                pygame.draw.rect(screen,(255,0,0),(self.x,self.y,self.thickness,self.thickness))
                
        def position(self):
            return pygame.Rect(self.x,self.y,self.thickness,self.thickness)
        
        def newPosition(self):
            self.x=randint(0,800)
            self.y=randint(0,600)
             
            

    def __init__(self):
        if not Candy._instance:
            Candy._instance = Candy.__Candy()
    
    def __getattr__(self, attr):
        return getattr(self._instance, attr) 
    
    def __setattr__(self, attr, value):
        return setattr(self._instance, attr, value)
    