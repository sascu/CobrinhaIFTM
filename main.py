import pygame, random
from pygame.locals import *

def colisao(obj1, obj2):
    return (obj1[0]==obj2[0] and (obj1[1]==obj2[1]))


pygame.init()
screen = pygame.display.set_mode((600, 600))   

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

skinBranco = pygame.Surface((10,10))
skinBranco.fill((255,255,255)) 

skinMaca = pygame.Surface((10,10))
skinMaca.fill((255,0,0))

posMaca = (random.randint(0, 59)*10, random.randint(0, 59)*10)

pygame.display.set_caption("Jogo da cobrinha")

cobra = [(200, 200), (210, 200), (220, 200)]

fps = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 20)
score = 0

direcao = CIMA

while True:
    fps.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if event.type == KEYDOWN:
        if event.key == K_UP and direcao != BAIXO:
            direcao = CIMA
        if event.key == K_DOWN and direcao != CIMA:
            direcao = BAIXO
        if event.key == K_LEFT and direcao != DIREITA:
            direcao = ESQUERDA
        if event.key == K_RIGHT and direcao != ESQUERDA:
            direcao = DIREITA

    if colisao(cobra[0], posMaca):
        cobra.append((0,0))
        posMaca = (random.randint(0, 59)*10, random.randint(0, 59)*10)
        score += 1

    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        pygame.quit()
        exit()
        
    for i in range(1, len(cobra)-1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            pygame.quit()
            exit()

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    if direcao == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == ESQUERDA:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    if direcao == DIREITA:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    
        
    screen.fill((0, 0, 0))
    screen.blit(skinMaca, posMaca)

    scoreText = fonte.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = scoreText.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(scoreText, score_rect)

    for posicao in cobra:
        screen.blit(skinBranco, posicao)
        
    pygame.display.update()
