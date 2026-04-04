import pygame, sys
from clock import draw_clock

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey's Clock")

# суретті жүктеу
hand_image = pygame.image.load(r"C:\Users\Lenovo\Desktop\g_abdigapbar\pp2-assigments\prac09\mickey.clock\images\sots\mickeyclock.jpeg")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # фон ақ
    draw_clock(screen, hand_image)

    pygame.display.flip()
    clock.tick(1)  # әр секунд сайын жаңарту
