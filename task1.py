import pygame
from pygame.draw import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))

    yellow = (255, 255, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    rect(screen, white, (0, 0, 600, 600))  # белый фон
    circle(screen, yellow, (300, 300), 100)  # голова
    circle(screen, red, (260, 260), 25)  # глаза
    circle(screen, red, (340, 260), 20)
    circle(screen, black, (260, 260), 15)  # зрачки
    circle(screen, black, (340, 260), 10)
    rect(screen, black, (250, 340, 100, 10))  # рот
    line(screen, black, [310, 250], [380, 220], 5)  # брови
    line(screen, black, [300, 250], [220, 220], 5)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()


if __name__ == '__main__':
    main()
