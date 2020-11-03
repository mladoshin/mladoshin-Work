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

SCORE = 0

# ----------------------->
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height, health):
        super().__init__()
        self.bullets = []
        self.width = width
        self.height = height
        self.health = health
        self.color = color
        self.bullet_group = pygame.sprite.Group()

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        #init the position
        self.rect.x = x
        self.rect.y = y

        self.health_progress_bar = HealthBar(self.rect.x, self.rect.y, self.width, 6, self.health)

        

        

    def get_width(self):
        return self.image.get_width()

    def get_Height(self):
        return self.image.get_height()

    def getDamage(self, val):
        self.health -= val
        

    def shoot(self):
        print("Shoot")
        bullet = Bullet(self.rect.x+15, self.rect.y, 10, 20, WHITE, 5)
        self.bullets.append(bullet)
        self.bullet_group.add(bullet)
        #bullet.draw()
        

        



class Player(Ship):
    isKilled = False
    health = 100
    movingSpeed = 5
    score = 0

    def __init__(self, _x, _y, width, height):
        super().__init__(_x, _y, WHITE, width, height, self.health)
        self.damage = 100

    def incrementScore(self, val):
        self.score += val

    def moveToLeft(self):
        self.rect.x = self.rect.x - self.movingSpeed
        if (self.rect.x <= 0):
            self.rect.x = 0

    def moveToRight(self):
        self.rect.x = self.rect.x + self.movingSpeed

        if (self.rect.x >= SIZE[0]-self.width):
            self.rect.x = SIZE[0]-self.width

    def moveUp(self):
        self.rect.y = self.rect.y - self.movingSpeed

        if (self.rect.y <= 0):
            self.rect.y = 0

    def moveDown(self):
        self.rect.y = self.rect.y + self.movingSpeed

        if (self.rect.y >= SIZE[1]-self.height):
            self.rect.y = SIZE[1]-self.height

    def draw(self, enemy_group):
        
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        self.bullet_group.draw(SCREEN)
        self.bullet_group.update(self.bullet_group)

        #collision between enemies and the player
        player_hit_group = pygame.sprite.spritecollide(self,enemy_group,True)

        #collision of the bullets and enemies
        bullet_hit_group = pygame.sprite.groupcollide(enemy_group, self.bullet_group, False, True)


        for hit in bullet_hit_group:
            self.incrementScore(10)
            hit.getDamage(self.damage)

            if (hit.health <= 0):
                enemy_group.remove(hit)

            print("Hit the enemy")


        for foo in player_hit_group:
            self.health -= 20
            self.incrementScore(5)

        self.health_progress_bar.update(self, self.health, True) # display the health bar


class HealthBar():
    def __init__(self, objX, objY, width, height, initHealth):
        self.maxHealth = initHealth
        self.outterContainer = pygame.Surface([width, height])
        self.outterContainer.fill(WHITE)
        self.rectOutter = self.outterContainer.get_rect()
        self.rectOutter.x = objX
        self.rectOutter.y = objY

        self.innerContainer = pygame.Surface([width, height])
        self.innerContainer.fill(GREEN)
        self.rectInner = self.innerContainer.get_rect()
        self.rectInner.x = objX
        self.rectInner.y = objY
        self.maxWidth = width
        self.height = height

    def update(self, player, health, isPlayer):
        percent = health/self.maxHealth
        newWidth = int(self.maxWidth * percent)

        if (newWidth <= 0):
            newWidth = 0

        self.innerContainer = pygame.Surface([newWidth, self.height])
        self.innerContainer.fill(GREEN)
        self.rectInner = self.innerContainer.get_rect()
        self.rectInner.x = player.rect.x 
        

        self.rectOutter.x = player.rect.x
        if (isPlayer):
            self.rectOutter.y = player.rect.y + player.height + 10
            self.rectInner.y = player.rect.y + player.height + 10
        else:
            print(self)

            self.rectOutter.y = player.rect.y - 10
            self.rectInner.y = player.rect.y - 10

        self.draw()

    def draw(self):
        SCREEN.blit(self.outterContainer, (self.rectOutter.x, self.rectOutter.y))
        SCREEN.blit(self.innerContainer, (self.rectInner.x, self.rectInner.y))
    

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
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, group):
        self.move()
        if (self.rect.y < -20):
            group.remove(self)
            print("Remove the bullet")


    



class Enemy(Ship):
    movingSpeed = 2
    def __init__(self, _x, _y, width, height, health, color):
        super().__init__(_x, _y, color, width, height, health)
        self.damage = 50

    def moveForward(self):
        self.rect.y = self.rect.y + self.movingSpeed

    def resetPosition(self):
        self.rect.y = -30
         
    def updateBar(self):
        self.health_progress_bar.update(self, self.health, False)

    def update(self, player):

        self.health_progress_bar.update(self, self.health, False)
        self.moveForward()
        
        if self.rect.y > SIZE[1]+self.height: 
            self.resetPosition() #resetting the position of the enemy after
            player.getDamage(5)  #decrement the player health if the enemy passes him

        






# ----------------------->


def main():
    done = False
    FPS = 60
    level = 0
    lives = 5
    
    mainFont = pygame.font.SysFont("comicsans", 50)

    #group of all enemies
    enemy_group = pygame.sprite.Group()

    #group for all bullets
    bullet_group = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()

    wave_length = 5

    lost = False
    lost_count = 0

    player = Player(200, 440, 40, 40)

    clock = pygame.time.Clock()


    #init the enemies
    def createEnemies():
        for i in range(wave_length):
            enemy = Enemy(random.randrange(50, SIZE[0]-100), random.randrange(-1000, -100), 20, 20, 100, BLUE)
            enemy_group.add(enemy)
            all_sprites_group.add(enemy)

    def reRenderWindow(lives):
        player.update()
        enemy_group.update(player)

        SCREEN.fill(BLACK)
        health_label = mainFont.render("Health: "+str(player.health), 1, WHITE)
        level_label = mainFont.render("Level: "+str(level), 1, WHITE)
        score_label = mainFont.render("Score: "+str(player.score), 1, WHITE)
        
        SCREEN.blit(health_label, (10, 10))
        SCREEN.blit(level_label, (640 - 150, 10))
        SCREEN.blit(score_label, (10, 50))

        #drawing all the enemies
        enemy_group.draw(SCREEN)

        #drawing the player
        player.draw(enemy_group)

        #collisions
        

        #collisions end

        pygame.display.update()

    while not done:
        clock.tick(FPS)
        
        
        

        
        

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
        if keys[pygame.K_d]:
            #move the player to the left
            player.moveToRight()
        if keys[pygame.K_w]:
            #move the player up
            player.moveUp()
        if keys[pygame.K_s]:
            #move the player down
            player.moveDown()
        if keys[pygame.K_LSHIFT]:
            #move the player down
            player.movingSpeed = 10
        else:
            player.movingSpeed = 5
            


        # drawing
        reRenderWindow(lives)

        if (player.health <= 0):
            done = True

        if (len(enemy_group) == 0):
            wave_length += 5
            level += 1
            createEnemies()

            
            

    #tick the clock    
    


# EndWhile-Endofgameloop
main()
#print("Your score: "+str(player.score))
