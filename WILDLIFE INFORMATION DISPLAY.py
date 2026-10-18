# Wildlife Information Display

# Import necessary library
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the display window
display_surface = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Set the window title
pygame.display.set_caption("Wildlife Information Display")

# Load and resize the background image
background_image = pygame.transform.scale(
    pygame.image.load("jungle.PNG").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load and resize the panda image
wildlife_image = pygame.transform.scale(
    pygame.image.load("panda.PNG").convert_alpha(),
    (220, 220)
)

# Position the panda image at the centre
wildlife_rect = wildlife_image.get_rect(
    center=(
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2 - 30
    )
)

# Create different font styles
heading_font = pygame.font.SysFont("comicsansms", 36, bold=True)
fact_font = pygame.font.SysFont("georgia", 24, italic=True)

# Render the heading text
heading_text = heading_font.render(
    "Wildlife Spotlight: Panda",
    True,
    pygame.Color("darkgreen")
)

# Position the heading
heading_rect = heading_text.get_rect(
    center=(SCREEN_WIDTH // 2, 45)
)

# Render an interesting panda fact
fact_text = fact_font.render(
    "Pandas mainly eat bamboo!",
    True,
    pygame.Color("darkblue")
)

# Position the fact text
fact_rect = fact_text.get_rect(
    center=(SCREEN_WIDTH // 2, 420)
)


# Main game loop
def game_loop():

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    running = True

    while running:

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the background
        display_surface.blit(background_image, (0, 0))

        # Draw the panda image
        display_surface.blit(wildlife_image, wildlife_rect)

        # Display the heading and fact
        display_surface.blit(heading_text, heading_rect)
        display_surface.blit(fact_text, fact_rect)

        # Update the screen
        pygame.display.flip()

        # Limit the game to 30 frames per second
        clock.tick(30)

    # Close Pygame
    pygame.quit()


# Run the application
if __name__ == "__main__":
    game_loop()