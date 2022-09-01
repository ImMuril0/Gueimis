import pygame, random

WIDTH = 1200
HEIGHT = 600
SPEED = 10
PLAYER_SPEED = 7
GROUND_WIDTH = 2 * WIDTH
GROUND_HEIGHT = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('sprites/Run__000.png').convert_alpha(),
                          pygame.image.load('sprites/Run__001.png').convert_alpha(),
                          pygame.image.load('sprites/Run__002.png').convert_alpha(),
                          pygame.image.load('sprites/Run__003.png').convert_alpha(),
                          pygame.image.load('sprites/Run__004.png').convert_alpha(),
                          pygame.image.load('sprites/Run__005.png').convert_alpha(),
                          pygame.image.load('sprites/Run__006.png').convert_alpha(),
                          pygame.image.load('sprites/Run__007.png').convert_alpha(),
                          pygame.image.load('sprites/Run__008.png').convert_alpha(),
                          pygame.image.load('sprites/Run__009.png').convert_alpha(),
                          ]
        
        self.image_left = [pygame.image.load('sprites/Left__000.png').convert_alpha(),
                          pygame.image.load('sprites/Left__001.png').convert_alpha(),
                          pygame.image.load('sprites/Left__002.png').convert_alpha(),
                          pygame.image.load('sprites/Left__003.png').convert_alpha(),
                          pygame.image.load('sprites/Left__004.png').convert_alpha(),
                          pygame.image.load('sprites/Left__005.png').convert_alpha(),
                          pygame.image.load('sprites/Left__006.png').convert_alpha(),
                          pygame.image.load('sprites/Left__007.png').convert_alpha(),
                          pygame.image.load('sprites/Left__008.png').convert_alpha(),
                          pygame.image.load('sprites/Left__009.png').convert_alpha(),]
        
        self.image_fall = pygame.image.load('sprites/Fall.png').convert_alpha()
        self.image_fall_left = pygame.image.load('sprites/Fall_left.png').convert_alpha()
        self.image_fly = pygame.image.load('sprites/Fly.png').convert_alpha()
        self.image_fly_left = pygame.image.load('sprites/Fly_left.png').convert_alpha()
        self.image_stoped = pygame.image.load('sprites/stoped.png').convert_alpha()
        self.image_stoped_left = pygame.image.load('sprites/stoped_left.png').convert_alpha()
        self.image = pygame.image.load('sprites/Run__000.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0
        
        self.right = False
        self.left = False

    def update(self, *args):
        self.rect[1] += SPEED
        
        def player_stoped(self):
            key = pygame.key.get_pressed()
            if not key[pygame.K_d] and not key[pygame.K_a]:
                self.image = self.image_stoped
                self.image = pygame.transform.scale(self.image,[100,100])
                if self.left == True:
                    self.image = self.image_stoped_left
                    self.image = pygame.transform.scale(self.image,[100,100])
        player_stoped(self)
        
        def run_right(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += PLAYER_SPEED
                self.current_image = (self.current_image + 1) % 10
                self.image = self.image_run[self.current_image]
                self.image = pygame.transform.scale(self.image,[100, 100])
                self.right = True
                self.left = False     
        run_right(self)
        
        def run_left(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                self.rect[0] -= PLAYER_SPEED
                self.current_image = (self.current_image + 1) % 10
                self.image = self.image_left[self.current_image]
                self.image = pygame.transform.scale(self.image,[100, 100])
                self.right = False
                self.left = True
        run_left(self)

        def fly(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= 30
                self.image = self.image_fly
                self.image = pygame.transform.scale(self.image, [100, 100])
                if self.left == True:
                    self.image = self.image_fly_left
                    self.image = pygame.transform.scale(self.image, [100, 100])
        fly(self)

        def fall(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_fall
                self.image = pygame.transform.scale(self.image, [100, 100])
                if self.left == True:
                    self.image = self.image_fall_left
                    self.image = pygame.transform.scale(self.image, [100, 100])
        fall(self)


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_HEIGHT

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

pygame.init()
game_window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Jogo 01')

BACKGROUND = pygame.image.load('sprites/background_03.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,[WIDTH, HEIGHT])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDTH * i)
    groundGroup.add(ground)

gameloop = True

def draw():
    playerGroup.draw(game_window)
    groundGroup.draw(game_window)
    
def update():
    groundGroup.update()
    playerGroup.update()
    
clock = pygame.time.Clock()
placar = 0

while gameloop:
    game_window.blit(BACKGROUND, (0, 0))
    font = pygame.font.SysFont('Arial',30)
    text = font.render('Placar', True, [255,255,255])
    game_window.blit(text, [1100, 20])
    contador = font.render(f'{placar}', True, [255,255,255])
    game_window.blit(contador, [1125, 50])
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    if is_off_screen(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(WIDTH - 40)
        groundGroup.add(newGround)

    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
        SPEED = 0
    else:
        SPEED = 10

    update()
    draw()
    pygame.display.update()