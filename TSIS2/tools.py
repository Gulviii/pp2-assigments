import pygame

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x,y))
    if target_color == new_color: return
    stack = [(x,y)]
    while stack:
        px, py = stack.pop()
        if surface.get_at((px,py)) == target_color:
            surface.set_at((px,py), new_color)
            if px > 0: stack.append((px-1, py))
            if px < surface.get_width()-1: stack.append((px+1, py))
            if py > 0: stack.append((px, py-1))
            if py < surface.get_height()-1: stack.append((px, py+1))

def draw_line(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_rect(surface, start, end, color, size):
    rect = pygame.Rect(start, (end[0]-start[0], end[1]-start[1]))
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, center, radius, color, size):
    pygame.draw.circle(surface, color, center, radius, size)
