import pygame

pygame.init()

WIDHT = 1200
HEIGHT = 600

GROUND_W = 2 * WIDHT
GROUND_H = 30

SPEED = 10
GAME_SPEED = 20
FLY = 30

AMARELO = (255,255,0)

FPS = 30

tela = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('Run')
relogio = pygame.time.Clock()

BACKGROUND = pygame.image.load('sprites/background_03.jpg')
BACKGROUND  = pygame.transform.scale(BACKGROUND, (WIDHT, HEIGHT))

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
                          pygame.image.load('sprites/Run__009.png').convert_alpha(),]
        
        self.image_fall = pygame.image.load('sprites/Fall.png').convert_alpha()
        self.image = pygame.image.load('sprites/Run__000.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.current_image = 0
        
        
    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += GAME_SPEED
            if key[pygame.K_a]:
                self.rect[0] -= GAME_SPEED
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image,(100,100))
        move_player(self)
        self.rect[1] += SPEED
        
        def fly(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= FLY
                self.image = pygame.image.load('sprites/Fly.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100,100])
                print('fly')
        fly(self)
        
        def fall(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_fall
                self.image = pygame.transform.scale(self.image, [100,100])
                print('fall')
        fall(self)
    
class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(GROUND_W, GROUND_H))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_H
        
    def update(self, *args):
        self.rect[0] -= GAME_SPEED
        
def is_off_screen(sprite):
     return sprite.rect[0] < -(sprite.rect[2])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDHT * i)
    groundGroup.add(ground)

loop = True
   
def draw():
    playerGroup.draw(tela)
    groundGroup.draw(tela)
   
def  update():
    groundGroup.update()
    playerGroup.update()
   
while True:
    tela.blit(BACKGROUND, (0, 0))
    relogio.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    if is_off_screen(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(WIDHT - 20)
        groundGroup.add(newGround)
        
    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
        SPEED = 0
        print('collision')
    else:
        SPEED = 10  
            
    update()
    draw()
    pygame.display.update()
