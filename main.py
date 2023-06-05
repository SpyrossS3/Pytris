# Pytris: A practice in Tetris with Pygame
import sys, pygame

pygame.init()

black = 0,0,0
width = 800
height = 800
size = width, height
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() # Python crashes when trying to close the game if this is not here
            sys.exit()
    
    screen.fill(black)
    pygame.display.flip()