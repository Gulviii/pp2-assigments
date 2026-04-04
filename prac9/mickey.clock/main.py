import pygame, sys
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey's Clock")

hand_image = pygame.image.load(
    r"C:\Users\Lenovo\Desktop\g_abdigapbar\pp2-assigments\prac9\mickey.clock\images\sots\mickeyclock.jpeg"
)


clock = pygame.time.Clock()

def draw_clock(screen, hand_image):
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)

    
    right_hand = pygame.transform.rotate(hand_image, minute_angle)
    left_hand = pygame.transform.rotate(hand_image, second_angle)

    
    screen.blit(right_hand, (250, 250))
    screen.blit(left_hand, (250, 250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  
    draw_clock(screen, hand_image)

    pygame.display.flip()
    clock.tick(1)  
