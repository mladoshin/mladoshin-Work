import pygame

BLACK = (0,0, 0)
WHITE = (255, 255,255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
GREEN = (50, 255, 50)
pygame.init()

size = (1000, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()


#classes
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brickSide):
        super().__init__()
        self.side = brickSide
        self.image = pygame.Surface([self.side, self.side])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, health, bricks):
        super().__init__()
        self.bricks = bricks
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def setSpeed(self, speed):
        self.speed = speed

    def isCollision(self):
        player_hit_group = pygame.sprite.spritecollide(self, self.bricks, False)
        flag = False
        for hit in player_hit_group:
            flag = True
            print(hit.rect.x)

        return flag



    def move(self, direction):
        if (self.isCollision() == False):
            if (direction=="up"):
                self.rect.y -= self.speed
            elif(direction == "down"):
                self.rect.y += self.speed
            elif(direction == "left"):
                self.rect.x -= self.speed
            elif(direction == "right"):
                self.rect.x += self.speed

class Game():
    def __init__(self, brickSide):
        self.numBricks = 0
        self.brickSide = brickSide
        self.all_sprites_group = pygame.sprite.Group()
        self.bricks_sprites_group = pygame.sprite.Group()
        self.player = Player(100, 100, 20, 20, 5, 100, self.bricks_sprites_group)
        self.all_sprites_group.add(self.player)
        self.done = False

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
        print(self.numBricks)


        print(self.player)

    def start(self):
        self.done = False
        self.mainLoop()

    def end(self):
        self.done = True

    def reRender(self):
        #render the player
        self.all_sprites_group.draw(screen)
        self.bricks_sprites_group.draw(screen)
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
                self.player.setSpeed(5)

            clock.tick(60)
        #EndWhile



game = Game(40)
game.start()

pygame.quit()
