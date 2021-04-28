import random
import pygame
import time


pygame.init()

green = (76, 153, 0 )
grey = (69, 69, 69)
red = (204, 0, 0)
brown = (150, 70, 0)

window_height = 420
window_width = 420

# funkcja jako argument pobiera roździelczość w nawiasie
dis = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('SZNEK.exe')


clock = pygame.time.Clock()

dim_sznek = 15
sznek_speed = 15




font_style = pygame.font.SysFont('calibri', 30)

def score(score):
    value = font_style.render('Masz Scora: ' + str(score), 1, red)
    dis.blit(value, [0, 0])

def sznek(dim_sznek, sznek_list):
    for i in sznek_list:
        pygame.draw.rect(dis, green, [i[0], i[1], dim_sznek, dim_sznek])  # kolor rbg, pozycja, wymiary szneka


def message(msg,color):
    msg = font_style.render(msg, 1, color)
    dis.blit(msg, [window_width / 6, window_height / 3])

def game_loop():
    game_over = 0
    game_close = 0

    x_sznek = window_width / 2
    y_sznek = window_height / 2

    x_change = 0
    y_change = 0

    sznek_List = []
    sznek_length = 1

    x_jedzonko = round(random.randrange(0, window_width - dim_sznek) / 15) * 15
    y_jedznko = round(random.randrange(0, window_height - dim_sznek) / 15) * 15

    while not game_over:

        while game_close == 1:
            dis.fill(grey)
            message('You Died', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        game_over = 1
                        game_close = 0
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -dim_sznek
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = dim_sznek
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -dim_sznek
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = dim_sznek
                    x_change = 0




        if x_sznek < 0 or x_sznek >= window_width or y_sznek < 0 or y_sznek >= window_height:
            game_close = 1

        x_sznek += x_change
        y_sznek += y_change

        dis.fill(grey)
        pygame.draw.rect(dis,brown,[x_jedzonko,y_jedznko,dim_sznek,dim_sznek])

        sznek_head = []
        sznek_head.append(x_sznek)
        sznek_head.append(y_sznek)
        sznek_List.append(sznek_head)
        if len(sznek_List) > sznek_length:
            del sznek_List[0]

        for i in sznek_List[:-1]:
             if i == sznek_head:
                   game_close = 1

        sznek(dim_sznek, sznek_List)
        score(sznek_length)

        pygame.display.update()
            # wprowadzanie zmian na ekranie

        if x_sznek == x_jedzonko and y_sznek == y_jedznko:
            x_jedzonko = round(random.randrange(0, window_width - dim_sznek) / 15) * 15
            y_jedznko = round(random.randrange(0, window_height - dim_sznek) / 15) * 15
            sznek_length += 1

        clock.tick(sznek_speed)

    #zamyka program
    pygame.quit()
    quit()

game_loop()