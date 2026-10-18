import pygame
pygame.init()
screen_width , screen_height = 800 ,600
#INITIALIZE DISPLAY SURFACE
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("ADDING AN IMAGE AND BACKGROUND")
#LOAD THE SCALE IMAGES DIRECTLY
background_image = pygame.transform.scale(pygame.image.load("background.PNG").convert(),
                                          (screen_width , screen_height))
penguin_image = pygame.transform.scale(pygame.image.load("penguin.PNG").convert_alpha(),
                                        (200 , 200))
penguin_rect = penguin_image.get_rect(center = (screen_width // 2 , screen_height //2-30))
#INITIALIZE FONT, RENDER, TEXT AND SET TEXT POSITION
text = pygame.font.Font(None,20).render("I AM NOT LAZY,JUST IN ENERGY SAVING MODE",True,pygame.Color("black") )
text_rect= text.get_rect(center=(screen_width//2, screen_height//2+110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running= False
        screen.blit(background_image,(0,0))
        screen.blit(penguin_image,penguin_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__== "__main__":
    game_loop()

