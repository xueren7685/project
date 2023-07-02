import pygame
import numpy as np

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
pygame.display.set_caption("20202068 SHIYAN ")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
background_image = pygame.image.load("R.jpg")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
sun_image = pygame.image.load("sun.png")
sun_image = pygame.transform.scale(sun_image, (100, 100))
planet_image = pygame.image.load("planet.png")
planet_image = pygame.transform.scale(planet_image, (80, 80))
moon_image = pygame.image.load("moon.png")
moon_image = pygame.transform.scale(moon_image, (40, 40))
spaceship_image = pygame.image.load("spaceship.png")
spaceship_image = pygame.transform.scale(spaceship_image, (60, 60))

class Sun:
    def __init__(self, radius, center):
        self.radius = radius# Radius of the sun
        self.center = center## Central location of the sun
# Draw the sun on the screen
    def draw(self, screen):
       screen.blit(sun_image, (self.center[0] - self.radius, self.center[1] - self.radius))

class Planet:
    def __init__(self, radius, distance, speed, center, color):
        self.radius = radius# The radius of the planet
        self.distance = distance# Distance between the planet and the sun
        self.speed = speed# The speed of the planet
        self.center = center# The central position of the planet
        self.color = color# Color of the planet
        self.angle = 0# Current Angle of the planet
#Create a moon object
        self.moon = self.Moon(10, self.distance / 2, self.speed, self.center)
# Update the planet's Angle
    def update(self):
        self.angle += self.speed
        self.moon.update(self.center, self.distance, self.angle)# Update moon position

    def draw(self, screen):
        # Calculate the new position based on the distance and Angle of the planet
        x = self.distance * np.cos(np.radians(self.angle))
        y = self.distance * np.sin(np.radians(self.angle))
        planet_center = (self.center[0] + int(x), self.center[1] + int(y))
        # Draw an image of the planet on the screen
        screen.blit(planet_image, (planet_center[0] - self.radius, planet_center[1] - self.radius))
        # Draw an image of the moon
        self.moon.draw(screen)

    class Moon:
        def __init__(self, radius, distance, speed, center):
            self.radius = radius# Moon radius
            self.distance = distance# The distance between the moon and the planets
            self.speed = speed# Speed of the moon
            self.center = center# Moon center location
            self.angle = 0# Current moon Angle
# Update moon position
        def update(self, planet_center, planet_distance, planet_angle):
            self.angle += self.speed
            x = (self.distance + planet_distance) * np.cos(np.radians(self.angle + planet_angle))
            y = (self.distance + planet_distance) * np.sin(np.radians(self.angle + planet_angle))
            self.center = (planet_center[0] + int(x), planet_center[1] + int(y))
# Draw an image of the moon on the screen
        def draw(self, screen):
            screen.blit(moon_image, (self.center[0] - self.radius, self.center[1] - self.radius))

class Spaceship:
    def __init__(self, position, speed):
        self.position = np.array(position)# Initial position of the ship
        self.speed = np.array(speed)# The speed of the ship

    def update(self):
        self.position -= self.speed  # Update the ship's position
# Draw an image of the ship on the screen
    def draw(self, screen):
        screen.blit(spaceship_image, (int(self.position[0]), int(self.position[1])))

def main():
    sun = Sun(50, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))# Create a Sun object
    planet = Planet(20, 100, 1, sun.center, BLUE)# Create a planet object
    spaceship = Spaceship([WINDOW_WIDTH + 50, WINDOW_HEIGHT // 2], [2, 0])  # Create a spaceship object

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
# Update the positions of planets and ships
        planet.update()
        spaceship.update()
# Draw a background image on the screen
        screen.blit(background_image, (0, 0))

        sun.draw(screen)
        planet.draw(screen)
        spaceship.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
