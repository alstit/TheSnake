from random import randint
import pygame
from collections import deque
from copy import deepcopy
import itertools


class Snake : 
    
    def __init__(self):
        self.x = randint(10,790)
        self.y = randint(10,590)
        self.head = list((self.x,self.y))
        self.thickness = 20
        self.size = 1
        self.speed = 50
        self.tail = deque()
        self.direction = "right" 
        
    def display(self,screen):         
        pygame.draw.rect(screen,(0,0,0),(self.head[0],self.head[1],self.thickness,self.thickness))
        for xy in self.tail:
            pygame.draw.rect(screen,(0,0,0),(xy[0],xy[1],self.thickness,self.thickness))

    def tailappend(self):
        if len(self.tail) != 0:
            xy=(self.tail[-1][0]+self.thickness,self.tail[-1][1])
        else : xy = (self.head[0]+self.thickness,self.head[1])
        self.tail.append(list(xy))
        
    def defDirection(self,direction):
        self.direction=direction
      
      
    def checkTailCollision(self):
            if self.headPosition().collidelistall(self.tailPosition()):
                print("game over")
                return True
            else : return False
        
    def headPosition(self):
        return pygame.Rect(self.head[0],self.head[1],self.thickness,self.thickness)
    
    def tailPosition(self):
        tailRect=[]
        for xy in list(itertools.islice(self.tail,1,len(self.tail))):
            tailRect.append(pygame.Rect(xy[0],xy[1],self.thickness,self.thickness))
        return tailRect
    
    def move(self,direction = None ):
        pygame.time.wait(self.speed)
        if direction == None:
            direction = self.direction
        self.tail.appendleft(deepcopy(self.head))        
        self.tail.pop()
        self.defDirection(direction)       
        if direction == "right":
            self.head[0]+= self.thickness
            if self.head[0]>800:
                self.head[0]=0
        elif direction == "left":
             self.head[0] -= self.thickness
             if self.head[0]<0:
                 self.head[0]=800
        elif direction == "down" :
                self.head[1] += self.thickness
                if self.head[1]>600:
                    self.head[1]=0
        elif direction == "up":
                self.head[1] -= self.thickness-1
                if self.head[1]<0:
                    self.head[1]=600

        