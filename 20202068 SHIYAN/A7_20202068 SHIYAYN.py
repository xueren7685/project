import pygame
import numpy as np
# Define a function that gets the coordinates of the four vertices of the rectangle
def getRectangle(width,height,x=0,y=0):
   
   # Create the four vertex coordinates of the rectangle
   points=np.array([[0,0],
                    [width,0],
                    [width,height],
                    [0,height]],dtype='float')
   # Translate the rectangle, moving its position to the specified coordinates (x, y)
   points=points+[x,y]
   #points=np.array([[x,y],
                    #[x+width,y],
                   # [x+width,y+height],
                    #[x,y+height]],dtype='float')
   return points
# Define a function that generates a rotation matrix
def Rmat(degree):
   # Convert angles to radians
   radian=np.deg2rad(degree)
   # Compute the elements of the rotation matrix
   c=np.cos(radian)
   s=np.sin(radian)
   # Build the rotation matrix
   R=np.array([[c,-s,0],[s,c,0],[0,0,1]])
   return R
# Define a function that generates a translation matrix
def Tmat(tx,ty):
   # Construct translation matrix
   T=np.array([[1,0,tx],
              [0,1,ty],
              [0,0,1]],dtype='float')
   return T
pygame.init()
WINDOW_WIDTH=800
WINDOW_HEIGHT=600 
 

GREEN=(100,200,100)

pygame.init()
pygame.display.set_caption("20202068 SHIYAN")
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()
angle3=0
width3=200
height3=75
# Gets the vertex coordinates of the rectangle
rect3=getRectangle(width3,height3,x=0,y=-height3/2.)
# Define a drawing function to draw a graph
def draw(M,points,color=(0,0,0),p0=None):
   # Gets the rotation part of the transformation matrix
   R=M[0:2,0:2]
   # Gets the translation portion of the transformation matrix
   t=M[0:2,2]
   # Transform the vertex coordinates
   points_transformed=(R @ points.T).T+t
   # Draw the transformed graph
   pygame.draw.polygon(screen,color,points_transformed,2)
   # If starting point p0 is given, draw the line from the starting point to the first vertex after the transformation
   if p0 is not None:
      pygame.draw.line(screen,(0,0,0),p0,points_transformed[0])
angle=0
done=False
while not done:
    angle+=5
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
          done=True
    screen.fill(GREEN)
   
    cent=(400,400)
    M=Tmat(cent[0],cent[1])
    draw(M,rect3,(0,0,0))
    M1=M@Rmat(angle)
    draw(M1,rect3,(255,0,0))
    M2=M1@Rmat(90)
    M3=M2@Rmat(90)
    M4=M3@Rmat(90)
    draw(M2,rect3,(0,255,0))
    draw(M3,rect3,(255,0,250))
    draw(M4,rect3,(255,250,0))

    pygame.draw.circle(screen,(0,0,0),cent,5)
    pygame.display.flip()
    clock.tick(60)
pygame,quit()       