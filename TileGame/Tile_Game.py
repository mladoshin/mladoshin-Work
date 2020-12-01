import pygame
import math
import random

BLACK = (0,0, 0)
WHITE = (255, 255,255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
GREEN = (50, 255, 50)
RED = (255, 0, 0)
pygame.init()

size = (1000, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()


#classes

#People base class for player and enemy
class People(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, speed, health, bricks):
        self.bricks = bricks
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed
        self.color = color
        self.bullets_list = pygame.sprite.Group()

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.playerX = 0
        self.playerY = 0

    def updatePlayerPosition(self, x, y):
        self.playerX = x
        self.playerY = y

    #method for wall colisions
    def isCollision(self):
        player_hit_group = pygame.sprite.spritecollide(self, self.bricks, False)
        flag = False
        direction = ""
        x = None
        y = None

        no_direction=["", "", "", ""]

        for hit in player_hit_group:
            flag = True
            #print("hit.rect.y: "+str(hit.rect.y))
            #print("self.rect.y: "+str(self.rect.y))
            x = hit.rect.x
            y = hit.rect.y

            if(self.rect.y == y+39):
                no_direction[0] = "up"
                self.rect.y = y+40
                print("up")

            if(self.rect.y+19 == y):
                no_direction[1] = "down"
                self.rect.y = y-20
                print("down")

            if(self.rect.x == x+39):
                no_direction[2] = "left"
                self.rect.x = x+40
                print("left")

            if(self.rect.x+19 == x):
                no_direction[3] = "right"
                self.rect.x = x-20
                print("right")


        return no_direction

    #move method
    def move(self):
        pass
    
    def setSpeed(self, speed):
        self.speed = speed

    #shooting method
    def shoot(self):
        bullet = Bullet(self.rect.x, self.rect.y, 10, 20, WHITE, 5)
        self.bullets_list.add(bullet)
        self.bullets_list.update()
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))



#brick class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brickSide):
        super().__init__()
        self.side = brickSide
        self.image = pygame.Surface([self.side, self.side])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Player class
class Player(People, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, speed, health, bricks):
        super().__init__(x, y, width, height, color, speed, health, bricks)
        pygame.sprite.Sprite.__init__(self)
        self.inventory = []

    #move method for the player
    def move(self, direction):
        no_direction=self.isCollision()

        if (direction=="up" and no_direction[0]!="up"):
            self.rect.y -= self.speed
        elif(direction == "down" and no_direction[1]!="down"):
            self.rect.y += self.speed
        elif(direction == "left" and no_direction[2]!="left"):
            self.rect.x -= self.speed
        elif(direction == "right" and no_direction[3]!="right"):
            self.rect.x += self.speed

        self.updatePlayerPosition(self.rect.x, self.rect.y)

class Loot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Weapon(Loot):
    def __init__(self, x, y, width, height, color, clip):
        super().__init__(x, y, width, height, color)
        self.clip = clip

#class FireArm(Weapon):
#    def __init__(self, )
#        super().__init__()

class Enemy(People):
    def __init__(self, x, y, width, height, color, speed, health, bricks, player):
        super().__init__(x, y, width, height, color, speed, health, bricks)
        pygame.sprite.Sprite.__init__(self)
        self.attackVector = [0, 0, 0]
        self.player = player
        self.fieldView = 400

    def attack(self):
        
        if (self.attackVector[2] <= self.fieldView):
            self.move()

    def moveX(self, x):
        #print("VectorX: "+str(self.attackVector[0])+"   VectorY: "+str(self.attackVector[1]))
        pass

    def moveY(self, y):
        pass

    def move(self):
        no_direction=self.isCollision()
        if (self.attackVector[0] == 0):
            fraction = 0
        else:
            fraction = self.attackVector[1] / self.attackVector[0]

        xSpeed = self.speed/(math.sqrt(1+pow(fraction, 2)))
        ySpeed = xSpeed*fraction
        
        #print(ySpeed)
        if (self.attackVector[0] < 0):
            #left
            self.rect.x -= math.ceil(xSpeed)
        else:
            #right
            self.rect.x += math.ceil(xSpeed)


        if (self.attackVector[1] < 0):
            #down
            self.rect.y += math.ceil(ySpeed)
        else:
            #up
            self.rect.y -= (-1)*math.floor(ySpeed)


    def getVector(self):
        return self.attackVector

    def update(self):
        
        self.attackVector[0] = self.player.rect.x-self.rect.x
        self.attackVector[1] = self.rect.y-self.player.rect.y
        self.attackVector[2] = math.sqrt(pow(self.attackVector[0], 2)+pow(self.attackVector[1], 2))
        #print(self.attackVector)
        #print("playerX: "+str(self.player.rect.x)+"  enemyX: "+str(self.rect.x))
        if (self.attackVector[2] <= self.fieldView):
            self.attack()

        #print(self.attackVector[2])



#Bullet class
class Bullet(pygame.sprite.Sprite):
    isVisible = False

    def __init__(self, x, y, width, height, color, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed

        #surface
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.y = self.rect.y - self.speed

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, group):
        self.move()
        if (self.rect.y < -20):
            group.remove(self)
            print("Remove the bullet")

        self.draw()

#Game class
class Game():
    def __init__(self, brickSide):
        self.numBricks = 0
        self.brickSide = brickSide
        self.enemy_sprites_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.bricks_sprites_group = pygame.sprite.Group()
        self.loot_sprites_group = pygame.sprite.Group()
        self.player = Player(100, 100, 20, 20, BLUE, 1, 100, self.bricks_sprites_group)
        self.all_sprites_group.add(self.player)
        self.done = False

        self.createOutterWalls()
                    
        
        for i in range(5, 10):
            brick = Brick(i*self.brickSide, 5*40, self.brickSide)
            self.bricks_sprites_group.add(brick)
            self.numBricks += 1
        print(self.numBricks)



        

        #print(self.player)
    def createLoot(self):
        loot = Loot(random.randint(40, 960), random.randint(40, 960), 20, 20, GREEN)
        self.all_sprites_group.add(loot)
        self.loot_sprites_group.add(loot)
        
    def createOutterWalls(self):
        for row in range(0, int(1000/self.brickSide)) :
            for col in range(0, int(1000/self.brickSide)):
                if(row == 0) or (row == 1000/40-1):
                    #add block
                    brick = Brick(col*self.brickSide, row*self.brickSide, self.brickSide)
                    self.bricks_sprites_group.add(brick)
                    self.numBricks += 1
                elif(col == 0) or (col == 1000/40-1):
                    brick = Brick(col*self.brickSide, row*self.brickSide, self.brickSide)
                    self.bricks_sprites_group.add(brick)
                    self.numBricks += 1

    def start(self):
        self.done = False
        enemy = Enemy(600, 600, 20, 20, RED, 1, 100, self.bricks_sprites_group, self.player)
        self.enemy_sprites_group.add(enemy)
        self.all_sprites_group.add(enemy)
        self.mainLoop()

    def end(self):
        self.done = True

    def reRender(self):
        self.enemy_sprites_group.update()
        #render the player
        self.all_sprites_group.draw(screen)
        self.bricks_sprites_group.draw(screen)
        #self.loot_sprites_group.draw(screen)
        pygame.display.update()

    def mainLoop(self):
        
        while not self.done:      
            screen.fill(BLACK)

            self.reRender()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                    #move the player to the right
                self.player.move("left")
            if keys[pygame.K_d]:
                    #move the player to the left
                self.player.move("right")
            if keys[pygame.K_w]:
                    #move the player up
                self.player.move("up")
            if keys[pygame.K_s]:
                #move the player down
                self.player.move("down")
            if keys[pygame.K_LSHIFT]:
                #move the player down
                self.player.setSpeed(10)
            else:
                self.player.setSpeed(1)

            clock.tick(240)
        #EndWhile



game = Game(40)
game.start()

pygame.quit()
