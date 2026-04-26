import pygame, sys, datetime
from tools import flood_fill, draw_line, draw_rect, draw_circle

pygame.init()
screen = pygame.display.set_mode((800,600))   # создаём окно
pygame.display.set_caption("Paint")           # заголовок окна
canvas = pygame.Surface(screen.get_size())    # холст для рисования
canvas.fill((255,255,255))                    # заполняем белым цветом

color = (0,0,0)       # текущий цвет кисти
brush_size = 2        # размер кисти
tool = "pencil"       # выбранный инструмент
drawing = False       # флаг рисования
start_pos = None      # начальная точка для линии
last_pos = None       # последняя позиция мыши

font = pygame.font.SysFont("Arial", 24)            # шрифт для текста
instruction_font = pygame.font.SysFont("Arial", 18)# шрифт для инструкций

text_active = False   # активен ли режим ввода текста
text_buffer = ""      # буфер для текста
text_pos = (0,0)      # позиция текста

clock = pygame.time.Clock()  # таймер для FPS

# список инструментов и кнопки для них
tools_list = ["pencil", "line", "fill", "text"]
button_rects = {}
for i, t in enumerate(tools_list):
    button_rects[t] = pygame.Rect(10 + i*100, 10, 90, 30)

def draw_panel():
    # рисует панель инструментов
    for t in tools_list:
        rect = button_rects[t]
        pygame.draw.rect(screen, (200,200,200), rect)
        label = font.render(t, True, (0,0,0))
        screen.blit(label, (rect.x+10, rect.y+5))
        if tool == t:
            pygame.draw.rect(screen, (0,0,255), rect, 2) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        # обработка кликов мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # выбор инструмента
            for t, rect in button_rects.items():
                if rect.collidepoint(event.pos):
                    tool = t
                    text_active = False
                    print("Tool selected:", tool)

            # действия инструментов
            if tool == "pencil":
                drawing = True
                last_pos = event.pos
            elif tool == "line":
                drawing = True
                start_pos = event.pos
            elif tool == "fill":
                flood_fill(canvas, event.pos[0], event.pos[1], color)
            elif tool == "text":
                text_pos = event.pos
                text_active = True
                text_buffer = ""

        elif event.type == pygame.MOUSEBUTTONUP:
            if tool == "pencil":
                drawing = False
            elif tool == "line" and drawing:
                draw_line(canvas, start_pos, event.pos, color, brush_size)
                drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if tool == "pencil" and drawing:
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

        # обработка клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: brush_size = 2
            elif event.key == pygame.K_2: brush_size = 5
            elif event.key == pygame.K_3: brush_size = 10

            # сохранение холста
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = f"canvas_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # ввод текста
            if text_active:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_buffer, True, color)
                    canvas.blit(text_surface, text_pos)
                    text_active = False
                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                elif event.key == pygame.K_BACKSPACE:
                    text_buffer = text_buffer[:-1]
                elif event.key == pygame.K_DELETE:
                    pygame.draw.rect(canvas, (255,255,255), (text_pos[0], text_pos[1], 200, 30))
                    text_buffer = ""
                elif event.key == pygame.K_t and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    with open("text_log.txt", "a", encoding="utf-8") as f:
                        f.write(f"{text_buffer}\n")
                    print("Text saved:", text_buffer)
                else:
                    text_buffer += event.unicode

    # отрисовка холста и текста
    screen.blit(canvas, (0,0))
    if text_active:
        preview = font.render(text_buffer, True, color)
        screen.blit(preview, text_pos)

    draw_panel()  # панель инструментов

    # инструкции внизу экрана
    instructions = "Text tool: Enter – подтвердить, Esc – отмена, Backspace – удалить символ, Delete – очистить, Ctrl+T – сохранить текст"
    instr_surface = instruction_font.render(instructions, True, (0,0,0))
    screen.blit(instr_surface, (10, screen.get_height()-30))

    pygame.display.flip()
    clock.tick(60)  # ограничение FPS
