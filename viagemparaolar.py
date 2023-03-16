from constants import SCREEN_WIDTH,SCREEN_HEIGHT,SCROLL_SPEED,FPS
import pygame
from john import John
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Viagem para o Lar")

ground_scroll = 0
# images
background= pygame.image.load('img/bg.jpg')
ground = pygame.image.load('img/gd.png')

# John
bird_group = pygame.sprite.Group()
flappy = John(100, int(SCREEN_HEIGHT / 2))
bird_group.add(flappy)

run = True
while run:
    clock.tick(FPS)
    # screen
    
    # background
    screen.blit(background,(0,0))
    
    # scroll
    screen.blit(ground, (ground_scroll,150))
    ground_scroll -= SCROLL_SPEED
    if abs(ground_scroll) > 400:
        ground_scroll = 0
    
    # john
    bird_group.draw(screen)
    bird_group.update()
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()
            