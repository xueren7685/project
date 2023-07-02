import pygame
import numpy as np
## Define a function that gets the coordinates of the vertices of a regular polygon
def getRegularPolygon(N, radius=1):
    v = np.zeros((N, 2))
    for i in range(N):
        deg = i * 360. / N
        rad = deg + np.pi / 180.
        x = radius + np.cos(rad)
        y = radius + np.sin(rad)
        v[i] = [x, y]
    return v
# Define a function that gets the coordinates of a rectangle vertex
def getRectangle(width, height, x=0, y=0):
    points = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype='float')
    return points
# Define the rotation matrix function
def Rmat(degree):
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return R
# Define translation matrix functions
def Tmat(tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]], dtype='float')
    return T
# Initialize Pygame
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Define color
GREEN = (100, 200, 100)

pygame.init()
pygame.display.set_caption("20202068 SHIYAN")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Set the center point of the first rectangle
center1 = [100, 200.]
# Initialize the Angle and clip state
angle1 = 0
angle2 = 0
angle3 = 0
clamp_open = False
# Define the width and height of the first rectangle
width1 = 140
height1 = 35
rect1 = getRectangle(width1, height1)
# Define the width and height of the second rectangle
width2 = 140
height2 = 35
rect2 = getRectangle(width2, height2)
# Define the width and height of the third rectangle
width3 = 140
height3 = 35
rect3 = getRectangle(width3, height3)
# Define the width and height of the clip
clamp_width = 40
clamp_height = 20
clamp_rect1 = getRectangle(clamp_width/2, clamp_height)
clamp_rect2 = getRectangle(clamp_width/2, clamp_height)
# Draw function for drawing rectangles
def draw(M, points, color=(0, 0, 0)):
    R = M[0:2, 0:2]
    t = M[0:2, 2]
    points_transformed = (R @ points.T).T + t
    pygame.draw.polygon(screen, color, points_transformed, 2)
# Draw the clip function
def draw_clamp(M, width, height, color=(0, 0, 0)):
    R = M[0:2, 0:2]
    t = M[0:2, 2]
    points_transformed1 = (R @ np.array([[0, 0], [width/2, 0], [width/2, height], [0, height]]).T).T + t
    points_transformed2 = (R @ np.array([[width/2, 0], [width, 0], [width, height], [width/2, height]]).T).T + t
    pygame.draw.polygon(screen, color, points_transformed1, 0)
    pygame.draw.polygon(screen, color, points_transformed2, 0)
# Game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Button Pressed!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                angle1 += 5
            elif event.key == pygame.K_d:
                angle1 -= 5
            elif event.key == pygame.K_w:
                angle2 += 5
            elif event.key == pygame.K_s:
                angle2 -= 5
            elif event.key == pygame.K_q:
                angle3 += 5
            elif event.key == pygame.K_e:
                angle3 -= 5
            elif event.key == pygame.K_SPACE:
                clamp_open = not clamp_open

    screen.fill(GREEN)
# Compute the transformation matrix of the first rectangle and draw it
    M1 = np.eye(3) @ Tmat(center1[0], center1[1]) @ Rmat(angle1) @ Tmat(0, -height1/2.)
    draw(M1, rect1, (255, 0, 0))
# Compute the transformation matrix of the second rectangle and draw it
    M2 = M1 @ Tmat(width1, 0) @ Tmat(0, height1/2.) @ Rmat(angle2) @ Tmat(0, -height1/2.)
    draw(M2, rect2, (255, 255, 0))
# Compute the transformation matrix of the third rectangle and draw it
    M3 = M2 @ Tmat(width2, 0) @ Tmat(0, height2/2.) @ Rmat(angle3) @ Tmat(0, -height2/2.)
    draw(M3, rect3, (0, 0, 255))
    pygame.draw.circle(screen, (0, 0, 0), center1, 4)
    C = M1 @ Tmat(width1, 0) @ Tmat(0, height1/2.)
    center2 = C[0:2, 2]
    pygame.draw.circle(screen, (0, 0, 0), center2, 5)
# Draw join points and clips
    clamp_M = M3 @ Tmat(width3, 0) @ Tmat(0, height3/2.)
    if clamp_open:
        draw_clamp(clamp_M, clamp_width, clamp_height, (255, 0, 255))
    else:
        draw_clamp(clamp_M, clamp_width/2, clamp_height, (255, 0, 255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
