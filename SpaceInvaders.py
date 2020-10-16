import pygame
import random
import math
pygame.font.init()
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
GREEN = (50, 255, 50)


SIZE = (640, 480)
SCREEN = pygame.display.set_mode(SIZE)

WIN = pygame.display.set_caption("My window")


# ----------------------->
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height, health):
        super().__init__()
        self.bullets = []
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.color = color

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        

    def get_width(self):
        return self.image.get_width()

    def get_Height(self):
        return self.image.get_height()

    def draw(self, obj):
        SCREEN.blit(self.image, (self.x, self.y))
        #print(len(self.bullets))

        for bullet in self.bullets[:]:
            bullet.move()
            bullet.draw()
            if bullet.y <= 0-bullet.height:
                self.bullets.remove(bullet)

            

            #if bullet.collide(obj):
                #print("Hit the Enemy")
                #obj.health -= 10
                #self.bullets.remove(bullet)

    def shoot(self):
        print("Shoot")
        bullet = Bullet(self.x+15, self.y, 10, 20, 5)
        #bullet.draw()
        self.bullets.append(bullet)

        



class Player(Ship):
    isKilled = False
    health = 100
    movingSpeed = 5

    def __init__(self, _x, _y, width, height):
        super().__init__(_x, _y, WHITE, width, height, self.health)
        self.mask = pygame.mask.from_surface(self.image)

    def moveToLeft(self):
        self.x = self.x - self.movingSpeed
        if (self.x <= 0):
            self.x = 0

    def moveToRight(self):
        self.x = self.x + self.movingSpeed

        if (self.x >= SIZE[0]-self.width):
            self.x = SIZE[0]-self.width

    def moveUp(self):
        self.y = self.y - self.movingSpeed

        if (self.y <= 0):
            self.y = 0

    def moveDown(self):
        self.y = self.y + self.movingSpeed

        if (self.y >= SIZE[1]-self.height):
            self.y = SIZE[1]-self.height

class Bullet:
    isVisible = False

    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.y = self.y - self.speed

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

    def collide(self, obj):
        #print(obj.x)
        #print(obj.y)
        print(collide(self, obj))
        return False

    



class Enemy(Ship):
    movingSpeed = 2
    def __init__(self, _x, _y, width, height, health, color):
        super().__init__(_x, _y, color, width, height, health)
        self.mask = pygame.mask.from_surface(self.image)

    def moveForward(self):
        self.y = self.y + self.movingSpeed


def collide(obj1, obj2):
    offsetX = obj1.x = obj2.x
    offsetY = obj1.y = obj2.y
    return obj1.mask.overlap(obj2.mask, (offsetX, offsetY)) != None


# ----------------------->


def main():
    done = False
    FPS = 60
    level = 1
    lives = 5
    mainFont = pygame.font.SysFont("comicsans", 50)

    enemies=[]
    wave_length = 5

    lost = False
    lost_count = 0

    player = Player(200, 440, 40, 40)

    clock = pygame.time.Clock()

    def reRenderWindow():
        SCREEN.fill(BLACK)
        lives_label = mainFont.render("Lives: "+str(lives), 1, WHITE)
        level_label = mainFont.render("Level: "+str(level), 1, WHITE)
        
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (640 - 150, 10))

        #drawing all the enemies
        for enemy in enemies:
            enemy.draw(player)
            if collide(enemy, player):
                print("The player is damaged!")

        #drawing the player
        player.draw(player)

        if lost:
                lost_label = mainFont.render("You lost!", 1, WHITE)
                SCREEN.blit(lost_label, (SIZE[0]/2 - lost_label.get_width()/2, 250))

        pygame.display.update()

    while not done:

        clock.tick(FPS)
        reRenderWindow()

        if lives <= 0 or player.health <=0:
            #lost
            lost = True
            
        if lost:
            if lost_count > FPS * 3:
                done = True
            else:
                continue
            

        if len(enemies)==0:  #adding new enemies
            level+=1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, SIZE[0]-100), random.randrange(-1000, -100), 20, 20, 100, BLUE)
                enemies.append(enemy)


    # --Userinputandcontrols
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                print("Left click!")
                player.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            #move the player to the right
            player.moveToLeft()
            print("Left")
        if keys[pygame.K_d]:
            #move the player to the left
            player.moveToRight()
            print("Right")
        if keys[pygame.K_w]:
            #move the player up
            print("Up")
            player.moveUp()
        if keys[pygame.K_s]:
            #move the player down
            print("Down")
            player.moveDown()


        for enemy in enemies[:]:
            enemy.draw(enemy)
            if lost==False:
                enemy.moveForward()
            if enemy.y + enemy.get_Height() > SIZE[1]:
                lives -= 1
                enemies.remove(enemy)
            


        # drawing
            
            
            

        
    # -Theclockticksover


# EndWhile-Endofgameloop
main()
#print("Your score: "+str(player.score))
