import pygame
from pygame.locals import *

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('20202068 SHIYAN')

clock = pygame.time.Clock()

# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("cute.mp3")

# Load and set up graphics.
background_image = pygame.image.load("zhu.jpeg").convert()
background_image = pygame.transform.scale(background_image, (800, 600))

player_image = pygame.image.load("panda.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (200, 200))  # 调整Panda图片的尺寸

# Rotate image function
def rotate_image(image, degrees, scale):
    rotated_image = pygame.transform.rotate(image, degrees)
    rotated_image = pygame.transform.scale(rotated_image, scale)
    return rotated_image

# Load and set up the source image
source_image = pygame.image.load("panda.png").convert_alpha()
source_image = pygame.transform.scale(source_image, (400, 300))

# Rotate the source image to create three rotated versions
rotated_image_1 = rotate_image(source_image, 90, (150, 150))
rotated_image_2 = rotate_image(source_image, 120, (100, 100))
rotated_image_3 = rotate_image(source_image, 270, (90, 90))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    # Copy background image to screen
    screen.blit(background_image, (0, 0))

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy player image to screen
    screen.blit(player_image, [x - player_image.get_width() // 2, y - player_image.get_height() // 2])

    # Copy rotated images to screen
    screen.blit(rotated_image_1, [100, 100])
    screen.blit(rotated_image_2, [300, 100])
    screen.blit(rotated_image_3, [500, 100])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
