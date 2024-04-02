import pygame
import sys

def cpontomedio(raio, xc, yc):
    x = 0
    y = raio
    d = 5 / 4 - raio

    ponto_circulo(x, y, xc, yc)

    while y > x:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1

        x += 1
        ponto_circulo(x, y, xc, yc)

def ponto_circulo(x, y, xc, yc):
    pygame.draw.circle(tela, (255, 255, 255), (xc + x, yc + y), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc - x, yc + y), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc + x, yc - y), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc - x, yc - y), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc + y, yc + x), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc - y, yc + x), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc + y, yc - x), 1)
    pygame.draw.circle(tela, (255, 255, 255), (xc - y, yc - x), 1)

raio = int(input("Digite o valor do raio do círculo: "))
largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor do altura: "))
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Algoritmo do Ponto Médio - Circunferência")

tela.fill((0, 0, 0))

xc, yc = largura // 2, altura // 2

cpontomedio(raio, xc, yc)

pygame.display.flip()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
