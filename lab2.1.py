import pygame
import sys

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    steps = 0
    
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    
    for _ in range(steps):
        pygame.draw.circle(tela, (255, 255, 255), (int(x), int(y)), 1)
        x += x_increment
        y += y_increment

largura = int(input("Digite a largura da tela: "))
altura = int(input("Digite a altura da tela: "))

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Algoritmo DDA")

tela.fill((0, 0, 0))

DDA(x1, y1, x2, y2)

pygame.display.flip()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
