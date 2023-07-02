import pygame  
import random  
import math  


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Bullet:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
# Move the bullet up
    def move(self):
        self.y -= 5

    def draw(self, screen):
        if self.shape == "circle":
         # Draw a white round bullet    
            pygame.draw.circle(screen, WHITE, (self.x, self.y), 10)
        elif self.shape == "rectangle":
        # Draw a red rectangular bullet   
            pygame.draw.rect(screen, RED, (self.x - 10, self.y - 10, 20, 20))
        elif self.shape == "triangle":
         # Draw a green triangle bullet   
            pygame.draw.polygon(screen, GREEN, [(self.x, self.y - 10), (self.x - 10, self.y + 10), (self.x + 10, self.y + 10)])
        elif self.shape == "line":
            # Draw a straight blue bullet
            pygame.draw.line(screen, BLUE, (self.x - 10, self.y), (self.x + 10, self.y), 5)

pygame.init()


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("20202068 SHIYAN")

clock = pygame.time.Clock()

# Initial position and rotation Angle of the launcher
cannon_x = WINDOW_WIDTH // 2  # The horizontal coordinate of the launcher is located in the center of the window
cannon_y = WINDOW_HEIGHT - 30  # The vertical coordinate of the launcher is located at the bottom of the window, and there is a certain distance from the bottom
cannon_angle = 0  # The initial rotation Angle of the launcher is 0 degrees
bullets = []  # A list of bullet objects to store

done = False
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()  # Get key status
    if keys[pygame.K_LEFT]:  # If you press the left arrow key
        cannon_angle += 1  # The launcher is rotated 1 degree counterclockwise
    if keys[pygame.K_RIGHT]: # If you press the right arrow key
        cannon_angle -= 1  # The launcher is rotated 1 degree clockwise

    # Limit the rotation Angle of the launcher to between 0 and 360 degrees
    cannon_angle %= 360

    if keys[pygame.K_SPACE]: # If you press the space bar
        shapes = ["circle", "rectangle", "triangle", "line"] # Define a list of optional shapes
        shape = random.choice(shapes)  # Select a random shape from the shape list

        # Calculate the initial position of the bullet based on the position of the firing cylinder and the rotation Angle
        bullet_x = cannon_x + int(40 * math.cos(math.radians(cannon_angle)))
        bullet_y = cannon_y - int(40 * math.sin(math.radians(cannon_angle)))

        bullet = Bullet(bullet_x, bullet_y, shape)  # Create a bullet object
        bullets.append(bullet)  # Adds the bullet object to the bullet list

    screen.fill(WHITE)  

  # Draw the launcher
    pygame.draw.rect(screen, BLACK, (cannon_x - 10, cannon_y - 20, 20, 40)) # Draw the rectangular portion of the launcher
    pygame.draw.line(screen,BLACK, (cannon_x, cannon_y), (cannon_x + int(40 * math.cos(math.radians(cannon_angle))), cannon_y - int(40 * math.sin(math.radians(cannon_angle)))), 5)  # Draw the rotating line portion of the launcher

    # Update and draw bullets
    for bullet in bullets:
        bullet.move()  # Move the bullet position
        bullet.draw(screen)  # Draw the shape of the bullet

    # Remove bullets that have left the window
    bullets = [bullet for bullet in bullets if bullet.y > 0]

    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()  
