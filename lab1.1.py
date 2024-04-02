import pygame
import sys

def user_to_ndc(user_coord, user_min, user_max):
    return (user_coord - user_min) / (user_max - user_min)

def ndc_to_user(ndc_coord, user_min, user_max):
    return user_min + ndc_coord * (user_max - user_min)

def ndc_to_unit(coord_ndc):
    return (coord_ndc + 1) / 2

def unit_to_ndc(coord_unit):
    return 2 * coord_unit - 1

def obter_dimensoes_led():
    largura = int(input("Digite a largura da janela do LED: "))
    altura = int(input("Digite a altura da janela do LED: "))
    return largura, altura

def obter_valores_entrada():
    x = float(input("Digite o valor de X: "))
    xmin = float(input("Digite o valor mínimo de X: "))
    xmax = float(input("Digite o valor máximo de X: "))
    y = float(input("Digite o valor de Y: "))
    ymin = float(input("Digite o valor mínimo de Y: "))
    ymax = float(input("Digite o valor máximo de Y: "))
    return x, xmin, xmax, y, ymin, ymax

pygame.init()

largura_led, altura_led = obter_dimensoes_led()

coord_x, xmin, xmax, coord_y, ymin, ymax = obter_valores_entrada()

ndc_coord_x = user_to_ndc(coord_x, xmin, xmax)
ndc_coord_y = user_to_ndc(coord_y, ymin, ymax)

coord_unit_x = ndc_to_unit(ndc_coord_x)
coord_unit_y = ndc_to_unit(ndc_coord_y)

ndc_coord_x_novo = unit_to_ndc(coord_unit_x)
ndc_coord_y_novo = unit_to_ndc(coord_unit_y)

print("Coordenada NDC (X):", ndc_coord_x)
print("Coordenada NDC (Y):", ndc_coord_y)

tela = pygame.display.set_mode((largura_led, altura_led))
pygame.display.set_caption("Computação Gráfica - LAB 01")
tela.fill((0, 0, 0)) 

pygame.draw.circle(tela, (255, 255, 255), (int(coord_unit_x * largura_led), int(coord_unit_y * altura_led)), 5)

pygame.display.flip()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
