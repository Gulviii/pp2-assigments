import pygame, random, sys

pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game Extended")

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

import os
os.chdir(os.path.dirname(__file__)) 

road = pygame.image.load("png/background.png")
car = pygame.image.load("png/player.png")
enemy = pygame.image.load("png/enemy.png")
coin = pygame.image.load("png/coin.png")

# Масштабтау
road = pygame.transform.scale(road, (WIDTH, HEIGHT))
car = pygame.transform.scale(car, (50, 100))
enemy = pygame.transform.scale(enemy, (50, 100))
coin = pygame.transform.scale(coin, (30, 30))

# Ойыншы
player_rect = car.get_rect(center=(WIDTH//2, HEIGHT-100))

# Қарсылас
enemy_rect = enemy.get_rect(center=(random.randint(50, WIDTH-50), -100))
enemy_speed = 5

# Монета (әртүрлі салмақпен)
def random_coin():
    rect = coin.get_rect(center=(random.randint(50, WIDTH-50), -50))
    weight = random.choice([1, 2, 5])  # монета салмағы (ұпай мәні)
    return rect, weight

coin_rect, coin_weight = random_coin()

# Ұпай
score = 0
font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.blit(road, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Басқару
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += 5

    # Enemy қозғалысы
    enemy_rect.y += enemy_speed
    if enemy_rect.top > HEIGHT:
        enemy_rect.center = (random.randint(50, WIDTH-50), -100)

    # Coin қозғалысы
    coin_rect.y += 5
    if coin_rect.top > HEIGHT:
        coin_rect, coin_weight = random_coin()

    # Қақтығыстар
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if player_rect.colliderect(coin_rect):
        score += coin_weight  # монета салмағына байланысты ұпай қосылады
        coin_rect, coin_weight = random_coin()

        # N монета жинағанда enemy жылдамдығы артады
        if score % 10 == 0:  # әр 10 ұпай сайын жылдамдық артады
            enemy_speed += 1

    # Сызу
    screen.blit(car, player_rect)
    screen.blit(enemy, enemy_rect)
    screen.blit(coin, coin_rect)

    # Ұпай көрсету
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
