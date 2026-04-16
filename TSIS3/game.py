import pygame, random

CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = 40, 30

class Snake:
    def __init__(self, color):
        self.body = [(10,10)]
        self.length = 3
        self.direction = (1,0)
        self.color = color
        self.shield = False

    def move(self):
        head = (self.body[0][0]+self.direction[0], self.body[0][1]+self.direction[1])
        self.body.insert(0, head)
        if len(self.body) > self.length:
            self.body.pop()

    def eat_food(self, food_type):
        if food_type == "normal":
            self.length += 1
        elif food_type == "poison":
            self.length -= 2
            if self.length <= 1:
                return "gameover"
        return "ok"

class Food:
    def __init__(self, kind="normal", obstacles=[]):
        self.kind = kind
        while True:
            pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            if pos not in obstacles:
                self.pos = pos
                break

class Obstacle:
    def __init__(self, level):
        self.blocks = []
        if level >= 3:
            for _ in range(level*2):
                self.blocks.append((random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1)))
