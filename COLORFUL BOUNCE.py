import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT+2
#BACKGROUND COLORS
BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")
#SPRITE COLORS
YELLOW = pygame.Color("yellow")
RED = pygame.Color("red")
LIGHTGREEN = pygame.Color("lightgreen")
MAGENTA = pygame.Color("magenta")
WHITE = pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #get  the sprites rect
        self.rect = self.image.get_rect()
        #set initial velocity
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        #move the sprites with the velocity
        self.rect.move_ip(self.velocity)
        #flag to track if the sprite hits a boundry
        boundry_hit = False
        #check for collisions for left and right boundries and reverse directions
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
            #check for collisions for top and bottom boundries and reverse directions
        if self.rect.top<=0 or self.rect.bottom>=400:
                    self.velocity[1] = -self.velocity[1]
                    boundry_hit = True
                    #if boundry was hit. post events to change colors
        if boundry_hit:
              pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
              pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
            #METHODS TO CHANGE THE SPRITE COLORS
    def change_color(self):
          self.image.fill(random.choice([YELLOW,WHITE,MAGENTA,RED,LIGHTGREEN]))
          #FUNCTION TO CHANGE THE BACKGROUND COLOR
def change_background_color():
      global bg_color 
      bg_color =random.choice([BLUE,LIGHTBLUE,DARKBLUE])
#CREATE A GROUP TO HOLD THE SPRITE
all_sprite_list = pygame.sprite.Group()
#initialize the sprite
sp1 = Sprite(WHITE,20,30)
#RANDOMLY POSITION THE SPRITE
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,270)
#add the sprite to teh group
all_sprite_list.add(sp1)
#create the game window
screen = pygame.display.set_mode((500,400))
#set the window title
pygame.display.set_caption("BOUNDRY SPRITES")
#SET THE INITIAL BACKGROUND COLOR
bg_color = BLUE
#APPLY THE BACKGROUND COLOR
screen.fill(bg_color)
#game loop control flag
exit = False
#create a clock object
clock = pygame.time.Clock()
while not exit :
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                  exit= True
            elif event.type == SPRITE_COLOR_CHANGE_EVENT:
                  sp1.change_color()
            elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
               change_background_color()

  # Update all sprites
        all_sprite_list.update()
  # Fill the screen with the current background color
        screen.fill(bg_color)
  # Draw all sprites to the screen
        all_sprite_list.draw(screen)

  # Refresh the display
        pygame.display.flip()
  # Limit the frame rate to 240 fps
        clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()
