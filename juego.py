import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana del juego
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego del Dinosaurio")

# Colores
WHITE = (255, 255, 255)

# Personaje (Dinosaurio)
dino_width, dino_height = 60, 80
dino_x, dino_y = 50, HEIGHT - dino_height
dino_vel = 5
jumping = False
jump_count = 10

# Obstáculos
obstacle_width, obstacle_height = 30, 60
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height

# Función para dibujar el dinosaurio
def draw_dino():
    pygame.draw.rect(win, WHITE, (dino_x, dino_y, dino_width, dino_height))

# Función para dibujar el obstáculo
def draw_obstacle():
    pygame.draw.rect(win, WHITE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control del dinosaurio
    keys = pygame.key.get_pressed()
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Movimiento del obstáculo
    obstacle_x -= 5
    if obstacle_x < 0:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - obstacle_height
        obstacle_height = random.randint(30, 100)

    # Colisiones
    if (
        dino_x + dino_width > obstacle_x
        and dino_x < obstacle_x + obstacle_width
        and dino_y + dino_height > obstacle_y
    ):
        print("¡Has perdido!")
        running = False

    # Dibujar todo
    win.fill((0, 0, 0))
    draw_dino()
    draw_obstacle()
    pygame.display.update()

pygame.quit()
sys.exit()

