import pygame
import sys

def inp_to_ndc(input_coord, input_min, input_max):
    return ((input_coord + input_min) / (input_max - input_min)) - 1

def ndc_to_user(ndc_coord, user_min, user_max):
    return user_min + ndc_coord * (user_max - user_min)

def user_to_ndc(user_coord, user_min, user_max):
    return (user_coord - user_min) / (user_max - user_min)

def ndc_to_dc(ndc_coord, dc_min, dc_max):
    return dc_min + (ndc_coord + 1) * (dc_max - dc_min) / 2

pygame.init()

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

largura_led, altura_led = obter_dimensoes_led()

coord_x, xmin, xmax, coord_y, ymin, ymax = obter_valores_entrada()

ndc_coord_x = inp_to_ndc(coord_x, xmin, xmax)
ndc_coord_y = inp_to_ndc(coord_y, ymin, ymax)

print("Coordenada NDC (X):", ndc_coord_x)
print("Coordenada NDC (Y):", ndc_coord_y)

dc_coord_x = ndc_to_dc(ndc_coord_x, 0, largura_led)
dc_coord_y = ndc_to_dc(ndc_coord_y, 0, altura_led)

tela = pygame.display.set_mode((largura_led, altura_led))
tela.fill((0, 0, 0)) 

pygame.draw.circle(tela, (255, 0, 0), (int(dc_coord_x), int(dc_coord_y)), 5)

pygame.display.flip()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
