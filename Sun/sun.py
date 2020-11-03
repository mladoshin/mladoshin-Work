import pygame;
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

sun_x = 40
sun_y = 40
isDay = True
while not done:
    sun_x = sun_x + 2
    sun_y = sun_y + 1

    if (sun_x > 680):
        sun_x = -140
        sun_y = -70
        isDay = False
    if (sun_x > 40):
        isDay = True
        
    #--Userinputandcontrols
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        #EndIf
    #Nextevent
            #--Gamelogicgoesafterthiscomment
            #--ScreenbackgroundisBLACK
    screen.fill(BLACK)
            #--Drawhere
    if (isDay == True):
        pygame.draw.rect(screen,WHITE,(0,0,640,480))
        
    pygame.draw.circle(screen,YELLOW,(sun_x,sun_y),40,0)
    pygame.draw.rect(screen,BLUE,(220,165,200,150))
    pygame.draw.rect(screen,GREEN,(0,300,640,480))
    
            #--flipdisplaytorevealnewpositionofobjects
    pygame.display.flip()
            #-Theclockticksover
    clock.tick(60)
#EndWhile-Endofgameloop
pygame.quit()
