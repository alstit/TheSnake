import pygame
from Snake import *
from pygame.constants import *
from Candy import  *




pygame.init()

screen=pygame.display.set_mode(size=(800, 600))

snake = Snake()

newGameFlag = 0

direction = None               
screen.fill((255,255,255))
                               
while (True):
    pygame.time.wait(16)
    
    if newGameFlag == 0:
        screen.fill((255,255,255))
    candy = Candy()
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                direction="right"
            if event.key == K_LEFT :
                direction="left"
            if event.key == K_UP:
                direction="up"
            if event.key == K_DOWN:
                direction=("down")               
            if event.key == K_ESCAPE:
                del snake
                snake=Snake() 
                newGameFlag=0
                   
    candy.display(screen)          
    snake.move(direction)
    #snake.checkTailCollision()
    if snake.checkTailCollision()==True:
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('game over, press escape for new game', True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)
        pygame.display.flip()
        newGameFlag=1

        
        
    snake.display(screen)
    if snake.headPosition().colliderect(candy.position()):
        snake.tailappend()
        candy.newPosition()
    
    pygame.display.flip()
    
    