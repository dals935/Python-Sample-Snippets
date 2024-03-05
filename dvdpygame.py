import time
import random
import pygame
 
# Initialize Pygame
pygame.init()
 
# Get native screen resolution and aspect ratio
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Screensaver Clock")
 
# Font and text size
font = pygame.font.SysFont("Arial", 84, bold=True)
 
# Rainbow color list
rainbow_colors = [
    (255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)
]
 
# Color change index
color_index = 0
 
# Clock position and movement variables
x, y = random.randint(0, width - 100), random.randint(0, height - 100)
x_vel, y_vel = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)
 
# Flag to control display mode (clock or date)
is_clock_mode = True
 
running = True
while running:
    # Handle events (excluding mouse movement)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_clock_mode = not is_clock_mode
 
    # Update time or date based on display mode
    if is_clock_mode:
        current_time = time.strftime("%I:%M:%S %p")
        #current_time = time.strftime("%H:%M:%S")
    else:
        current_date = time.strftime("%d/%m/%Y")
 
    # Render text
    if is_clock_mode:
        text = font.render(current_time, True, rainbow_colors[color_index])
    else:
        text = font.render(current_date, True, rainbow_colors[color_index])
    text_rect = text.get_rect()
 
    # Update position
    x += x_vel
    y += y_vel
 
    # Check for edge collisions and bounce with color change
    if x < 0:
        x = 0
        x_vel *= -1
        color_index = (color_index + 1) % len(rainbow_colors)
    elif x + text_rect.width > width:
        x = width - text_rect.width
        x_vel *= -1
        color_index = (color_index + 1) % len(rainbow_colors)
 
    if y < 0:
        y = 0
        y_vel *= -1
        color_index = (color_index + 1) % len(rainbow_colors)
    elif y + text_rect.height > height:
        y = height - text_rect.height
        y_vel *= -1
        color_index = (color_index + 1) % len(rainbow_colors)
 
    # Fill screen with black
    screen.fill((0, 0, 0))
 
    # Draw text
    screen.blit(text, (x, y))
 
    # Update display
    pygame.display.flip()
 
    # Hide mouse cursor
    pygame.mouse.set_visible(False)
 
# Quit Pygame
pygame.quit()