import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

noise_collision = pygame.mixer.Sound('smw_coin.wav')

LARGURA = 1280
ALTURA = 720

VELOCIDADE = 10

VERMELHO = (255,0,0)
VERDE = (0,255,0)
PRETO = (0,0,0)
AMARELO = (255, 255, 0)

x_red = 150
y_red = 590
pnts_red = 0

x_verde = 1130
y_verde = 590
pnts_green = 0

pnts_total = 2

x_coin = (LARGURA//2)
y_coin = 100

fonte = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Follow Coin')
relogio = pygame.time.Clock()

ganhou = False

def restart_game():
    global ganhou, x_red, y_red, pnts_green, pnts_red, x_verde, y_verde, x_coin, y_coin
    x_red = 150
    y_red = 590
    pnts_red = 0
    x_verde = 1130
    y_verde = 590
    pnts_green = 0
    x_coin = (LARGURA//2)
    y_coin = 100
    ganhou = False

x_verde = 1130
y_verde = 590
pnts_green = 0

while True:
    relogio.tick(60)
    tela.fill(PRETO)
    msg_red = f'Pontos: {pnts_red}'
    msg_green = f'Pontos: {pnts_green}'
    txt_formt = fonte.render(msg_red, True, (VERMELHO))
    txt_formt2 = fonte.render(msg_green, True, (VERDE))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        ''' 
        if event.type == KEYDOWN:
            if event.key == K_a:
                x_red = x_red - 20
            if event.key == K_d:
                x_red = x_red + 20
            if event.key == K_s:
                y_red = y_red + 20
            if event.key == K_w:
                y_red = y_red - 20''' 
                
    if pygame.key.get_pressed()[K_a]:
        x_red = x_red - (VELOCIDADE)
    if pygame.key.get_pressed()[K_w]:
        y_red = y_red - (VELOCIDADE)
    if pygame.key.get_pressed()[K_d]:
        x_red = x_red + (VELOCIDADE)
    if pygame.key.get_pressed()[K_s]:
        y_red = y_red + (VELOCIDADE)
    
    if pygame.key.get_pressed()[K_LEFT]:
        x_verde = x_verde - (VELOCIDADE)
    if pygame.key.get_pressed()[K_UP]:
        y_verde = y_verde - (VELOCIDADE)
    if pygame.key.get_pressed()[K_RIGHT]:
        x_verde = x_verde + (VELOCIDADE)
    if pygame.key.get_pressed()[K_DOWN]:
        y_verde = y_verde + (VELOCIDADE)
    
    
    red = pygame.draw.circle(tela, (VERMELHO), (x_red, y_red), 30)
    green = pygame.draw.circle(tela, (VERDE), (x_verde, y_verde), 30)
    coin = pygame.draw.circle(tela, (AMARELO), (x_coin, y_coin), 15)
    
    if red.colliderect(coin):
        x_coin = randint(40, 1240)
        y_coin = randint(50, 670)
        pnts_red = pnts_red + 1
        noise_collision.play()
        
    if green.colliderect(coin):
        x_coin = randint(40, 1240)
        y_coin = randint(50, 670)
        pnts_green = pnts_green + 1
        noise_collision.play()
        
    if pnts_red >= pnts_total:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'Vermeho ganhou! Pressione a tecla R para jogar novamente'
        txt_formt = fonte2.render(msg, True, (VERMELHO))
        ret_txt = txt_formt.get_rect()
        ganhou = True
        while ganhou:
            tela.fill(PRETO)
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
                        
    if pnts_green >= pnts_total:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'Verde ganhou! Pressione a tecla R para jogar novamente'
        txt_formt = fonte2.render(msg, True, (VERDE))
        ret_txt = txt_formt.get_rect()
        ganhou = True
        while ganhou:
            tela.fill(PRETO)
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
        
    if x_red > LARGURA:
        x_red = 0
    if x_red < 0:
        x_red = LARGURA
    if y_red > ALTURA:
        y_red = 0
    if y_red < 0:
        y_red = ALTURA
            
    if x_verde > LARGURA:
        x_verde = 0
    if x_verde < 0:
        x_verde = LARGURA
    if y_verde > ALTURA:
        y_verde = 0
    if y_verde < 0:
        y_verde = ALTURA        
    
    tela.blit(txt_formt, (40,40))
    tela.blit(txt_formt2, (40,90))
    pygame.display.update()