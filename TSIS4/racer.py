import pygame, random

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

class Enemy(GameObject):
    def __init__(self, image, speed, width):
        super().__init__(image, random.randint(50, width-50), -100)
        self.speed = speed
    def update(self):
        self.rect.y += self.speed