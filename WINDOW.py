#IMPORT NECESSARY LIBRARIES
import pygame
#INITIALIZE PYGAME
pygame.init()
#SETUP A WINDOW
screen = pygame.display.set_mode((600, 800))
#CREATE A LOOP TO KEEP THE WINDOW OPEN
done = False
while not done:
    #CLEAR THE EVENT QUEUE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            #MAKE THE CHANGES VISIBLE
    pygame.display.flip()