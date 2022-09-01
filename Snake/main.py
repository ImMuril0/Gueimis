import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

noise_collision = pygame.mixer.Sound('smw_coin.wav')

LARGURA = 1280
ALTURA = 720

VELOCIDADE = 5

VERMELHO = (255,0,0)
VERDE = (0,255,0)
PRETO = (0,0,0)
BRANCO = (255, 255, 255)
CINZA = (192,192,192)

x_snake = LARGURA//2
y_snake = ALTURA//2


x_control = VELOCIDADE
y_control = 0

pnts = 0

x_apple = randint(30, 1250)
y_apple = randint(30, 690)

fonte = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Follow Coin')
relogio = pygame.time.Clock()
comprimento_inicial = 5

snake_list = []

morreu = False

def snake_loud(snake_list):
    for XeY in snake_list:
        pygame.draw.rect(tela, (VERDE), (XeY[0], XeY[1], 20, 20))

def restart_game():
    global pnts, comprimento_inicial, x_snake, y_snake, snake_list, head_list, x_apple, y_apple,  morreu
    pnts = 0
    comprimento_inicial = 5
    x_snake = LARGURA//2
    y_snake = ALTURA//2
    snake_list = []
    head_list = []
    x_apple = randint(30, 1250)
    y_apple = randint(30, 690)
    morreu = False

while True:
    relogio.tick(60)
    tela.fill(CINZA)
    msg = f'Pontos: {pnts}'
    txt_formt = fonte.render(msg, True, (PRETO))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
     
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == VELOCIDADE:
                    pass
                else:
                    x_control = -VELOCIDADE
                    y_control = 0
            if event.key == K_d:
                if x_control == -VELOCIDADE:
                    pass
                else:
                    x_control = VELOCIDADE
                    y_control = 0
            if event.key == K_s:
                if y_control == VELOCIDADE:
                    pass
                else:
                    y_control = VELOCIDADE
                    x_control = 0
            if event.key == K_w:
                if  y_control == -VELOCIDADE:
                    pass
                else:
                    y_control = -VELOCIDADE
                    x_control = 0
    
    x_snake = x_snake + x_control
    y_snake = y_snake + y_control
          
    snake = pygame.draw.rect(tela, (VERDE), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.circle(tela, (VERMELHO), (x_apple, y_apple), 10)
    
    if snake.colliderect(apple):
        x_apple = randint(40, 1240)
        y_apple = randint(50, 670)
        pnts = pnts + 1
        noise_collision.play()
        comprimento_inicial = comprimento_inicial + 1
        
    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    snake_list.append(head_list)
    
    if snake_list.count(head_list) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'Game over! Pressione a tecla R para jogar novamente'
        txt_formt = fonte2.render(msg, True, (BRANCO))
        ret_txt = txt_formt.get_rect()
        morreu = True
        while morreu:
            tela.fill(CINZA)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
                        
            ret_txt.center = (LARGURA//2, ALTURA//2)
            tela.blit(txt_formt, (ret_txt))
            pygame.display.update()
    
    if x_snake > LARGURA:
        x_snake = 0
    if x_snake < 0:
        x_snake = LARGURA
    if y_snake > ALTURA:
        y_snake = 0
    if y_snake < 0:
        y_snake = ALTURA
    
    if len(snake_list) > comprimento_inicial:
        del snake_list[0]
    
    snake_loud(snake_list)
        
    tela.blit(txt_formt, (40,40))
    pygame.display.update()