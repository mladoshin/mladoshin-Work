import pygame;
import random;
import math;
BLACK = (0,0, 0)
WHITE = (255, 255,255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
GREEN = (50, 255, 50)
pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My window")
done = False;
clock = pygame.time.Clock()

d = 20

ballPosition = [d, d]
batStep = 15
Direction = [1, 1]

batPosition = [20, 200]
ballSpeed = 1

Direction[0] = random.randint(1,5)
Direction[1] = random.randint(1,5)
print("X: "+str(Direction[0]))
print("Y: "+str(Direction[1]))

while not done:
    
        
    #--Userinputandcontrols
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                
                batPosition[1]=batPosition[1]-batStep
                if (batPosition[1] <= 0):
                    batPosition[1] = 0

            if event.key == pygame.K_DOWN:
                batPosition[1]=batPosition[1]+batStep
                if batPosition[1] >= 380:
                    batPosition[1] = 380
             
    screen.fill(BLACK)
            #--Drawhere

    
    
    #drawing  
    pygame.draw.circle(screen,BLUE,(ballPosition[0],ballPosition[1]),15,0)
    pygame.draw.rect(screen,WHITE,(0, batPosition[1], 20,100)) #bat
    pygame.draw.rect(screen,WHITE,(620,0,640,480))
    #--flipdisplaytorevealnewpositionofobjects
    pygame.display.flip()
            #-Theclockticksover

    #ball movement

    ballPosition[0]=ballPosition[0]+Direction[0] #x movement of the ball
    ballPosition[1]=ballPosition[1]+Direction[1] #y movement of the ball

    #collision of the ball and the bat
    if (ballPosition[0] <= batPosition[0]+20) and ((ballPosition[1] > batPosition[1]-15) and (ballPosition[1] < batPosition[1]+100)):
        Direction[0] = (-1)*Direction[0]
        print("Hit the bat!")
                                                
    if (ballPosition[0] >= 605):  #Right wall
        #Direction[1] = (-1)*Direction[1]
        Direction[0] = (-1)*Direction[0]
        print("Hit the right wall")
        
    
    if (ballPosition[1] >= 465): #bottom wall
        Direction[1] = (-1)*Direction[1]
        print("Hit the bottom wall")

    if (ballPosition[1] <= 15): #top wall
        Direction[1] = (-1)*Direction[1]
        print("Hit the top wall")

    if (ballPosition[0] <= 15): #Left wall
        print("You lost!")
        done = True
        

        
        

    #moving the ball
    ballPosition[0] = ballPosition[0]+int((Direction[0]*ballSpeed)/2)
    ballPosition[1] = ballPosition[1]+int((Direction[1]*ballSpeed)/2)
    
    clock.tick(60)
#EndWhile-Endofgameloop
pygame.quit()
