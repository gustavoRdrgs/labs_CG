import pygame
import sys
import math

def lineBres(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyMinusDx = 2 * (dy - dx)
    x, y = 0, 0

    if x1 > x2:
        x, y = x2, y2
        x2 = x1
    else:
        x, y = x1, y1

    setPixel(x, y)

    while x < x2:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyMinusDx
        setPixel(x, y)

def setPixel(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor do altura: "))
pygame.init()
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Algoritmo do Ponto Médio - Reta")
screen.fill((0, 0, 0))

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

lineBres(x1, y1, x2, y2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
