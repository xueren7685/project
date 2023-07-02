import pygame
import math
import time#Import the Time library to obtain the current time.

pygame.init()

# Set the window size and titleR
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("20202068 SHIYAN")

clock = pygame.time.Clock()

def draw_clock():#Used to draw the appearance of the clock.
    # Set the center point and radius of the clock
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y) - 10

    # Draw the outer circle of the clock
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), radius, 2)

    # Get current time
    current_time = pygame.time.get_ticks() // 1000  # Convert to seconds
    hour = current_time // 3600 % 12#Calculate the current hours. The value ranges from 0 to 11.
    minute = (current_time % 3600) // 60#The value ranges from 0 to 59.
    second = current_time % 60#Calculates the current seconds. The value ranges from 0 to 59.

    # Calculate the position of the hour, minute and second hands
    hour_angle = math.radians((hour / 12) * 360 - 90)
    hour_x = center_x + int(0.4 * radius * math.cos(hour_angle))
    hour_y = center_y + int(0.4 * radius * math.sin(hour_angle))

    minute_angle = math.radians((minute / 60) * 360 - 90)
    minute_x = center_x + int(0.6 * radius * math.cos(minute_angle))
    minute_y = center_y + int(0.6 * radius * math.sin(minute_angle))

    second_angle = math.radians((second / 60) * 360 - 90)
    second_x = center_x + int(0.8 * radius * math.cos(second_angle))
    second_y = center_y + int(0.8 * radius * math.sin(second_angle))

    # Draw the hour, minute, and second hands
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (hour_x, hour_y), 6)
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (minute_x, minute_y), 4)
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (second_x, second_y), 2)

    # Draw the center point of the clock
    pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), 6)

    # Display time
    font = pygame.font.Font(None, 36)
    time_text = font.render(f"{hour:02d}:{minute:02d}:{second:02d}", True, (255, 255, 255))
    text_rect = time_text.get_rect(center=(center_x, center_y + radius + 20))
    screen.blit(time_text, text_rect)

# Initializes the last hour and the ringing sound
prev_hour = -1
ding_dong_sound = pygame.mixer.Sound("zhong.mp3")  # Use the bell sound file

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))  
    draw_clock() 

    current_hour = time.localtime().tm_hour
    if current_hour != prev_hour:
        
        ding_dong_sound.play()
        prev_hour = current_hour

    pygame.display.flip()
    clock.tick(1)  
