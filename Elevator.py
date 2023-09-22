
# Add required library
import pygame
from time import sleep

# Window size
WIDTH = 600
HEIGHT = 800
FPS = 60

# 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Specifications of checkboxes
checkbox_width = 20
checkbox_height = 20
checkbox_margin = 10
checkbox_x = WIDTH - checkbox_width - checkbox_margin
checkbox_y_start = checkbox_margin
checkbox_y_spacing = checkbox_height + checkbox_margin
checkbox_locked = False

# The size of the numbers
number_font_size = 30
number_spacing = 70
number_x = 10

# Elevator location
rect_width = 25
rect_height = 50
rect_x = (WIDTH - rect_width) // 2
rect_y = 615

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

numbers = ["5", "4", "3", "2", "1", "G"]

checkbox_labels = ["5", "4", "3", "2", "1", "G"]

# Create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

rect_speed = 1

checkbox_states = [False] * len(checkbox_labels)
d = {0:115 , 1:215 , 2:315 , 3:415 , 4:515 , 5:615}

outsaid = []
insaid = []

# The main ring of the elevator
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(checkbox_labels)):
                checkbox_rect = pygame.Rect(checkbox_x, checkbox_y_start + i * checkbox_y_spacing, checkbox_width, checkbox_height)
                if checkbox_rect.collidepoint(mouse_pos):
                    checkbox_states[i] = not checkbox_states[i]
                    try:
                        if rect_y > d[i] > d[min(outsaid)] or rect_y < d[i] < d[max(outsaid)]:
                            insaid.append(i)
                    except:
                        pass
                    if rect_y >= d[i] and i not in insaid:
                        outsaid.append(i)
                    elif rect_y <= d[i] and i not in insaid:
                        outsaid.append(i)


    screen.fill((48, 52, 69))

    number_y = (HEIGHT - number_font_size * len(numbers) - number_spacing * (len(numbers) - 1)) // 2
    for number in numbers:
        font = pygame.font.Font(None, number_font_size)
        number_text = font.render(number, True, (2, 170, 255))
        screen.blit(number_text, (number_x, number_y))
        number_y += number_font_size + number_spacing

    pygame.draw.rect(screen, (221, 144, 254), (rect_x, rect_y , rect_width, rect_height))

    # Movement part
    move_up = False
    move_down = False
    try:
        if len(outsaid) != 0:
            if d[outsaid[0]] < rect_y:
                move_up = True
                if len(insaid) != 0:
                    insaid.sort()
                    insaid.reverse()
                    if rect_y == d[insaid[0]]:
                        checkbox_states[insaid[0]] = not checkbox_states[insaid[0]]
                        insaid.remove(insaid[0])
                        sleep(2)
            elif d[outsaid[0]] == rect_y:
                checkbox_states[outsaid[0]] = not checkbox_states[outsaid[0]]
                outsaid.remove(outsaid[0])
                sleep(2)
    
        if len(outsaid) != 0:
            if d[outsaid[0]] > rect_y:
                move_down = True
                if len(insaid) != 0:
                    insaid.sort()
                    if rect_y == d[insaid[0]]:
                        checkbox_states[insaid[0]] = not checkbox_states[insaid[0]]
                        insaid.remove(insaid[0])
                        sleep(2)
            elif d[outsaid[0]] == rect_y:
                checkbox_states[outsaid[0]] = not checkbox_states[outsaid[0]]
                outsaid.remove(outsaid[0])
                sleep(2)
        if move_up:
            rect_y -= rect_speed
        elif move_down:
            rect_y += rect_speed
    except:
        pass
    

    for i in range(len(checkbox_labels)):
        checkbox_rect = pygame.Rect(checkbox_x, checkbox_y_start + i * checkbox_y_spacing, checkbox_width, checkbox_height)
        pygame.draw.rect(screen, WHITE, checkbox_rect)
        if checkbox_states[i]:
            pygame.draw.rect(screen, GREEN, checkbox_rect.inflate(-4, -4))
        checkbox_font = pygame.font.Font(None, 20)
        checkbox_text = checkbox_font.render(checkbox_labels[i], True, (255, 0, 81))
        screen.blit(checkbox_text, (checkbox_x - checkbox_text.get_width() - checkbox_margin, checkbox_y_start + i * checkbox_y_spacing))
    pygame.display.flip()
pygame.quit()
