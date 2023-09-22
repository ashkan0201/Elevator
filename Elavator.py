import pygame
from time import sleep
WIDTH = 600
HEIGHT = 800
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

checkbox_width = 20
checkbox_height = 20
checkbox_margin = 10
checkbox_x = WIDTH - checkbox_width - checkbox_margin
checkbox_y_start = checkbox_margin
checkbox_y_spacing = checkbox_height + checkbox_margin
checkbox_locked = False

number_font_size = 30
number_spacing = 70
number_x = 10

rect_width = 25
rect_height = 50
rect_x = (WIDTH - rect_width) // 2
rect_y = 615

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

numbers = ["5", "4", "3", "2", "1", "G"]

checkbox_labels = ["5", "4", "3", "2", "1", "G"]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

rect_speed = 2

checkbox_states = [False] * len(checkbox_labels)
d = {0:115 , 1:215 , 2:315 , 3:415 , 4:515 , 5:615}
outsaid = []
insaid = []

pygame.quit()