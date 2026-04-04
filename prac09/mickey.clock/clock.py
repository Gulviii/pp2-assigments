import pygame
from datetime import datetime

def draw_clock(screen, hand_image):
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # бұрыштарды есептеу (әр минут/секунд = 6°)
    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)

    # қолдарды айналдыру
    right_hand = pygame.transform.rotate(hand_image, minute_angle)
    left_hand = pygame.transform.rotate(hand_image, second_angle)

    # экранға шығару (ортаны өзің ыңғайлап қоясың)
    screen.blit(right_hand, (250, 250))
    screen.blit(left_hand, (250, 250))
