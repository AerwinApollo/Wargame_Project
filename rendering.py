import pygame

def draw_grid(screen, cell_size, grid_size):
    for x in range(0, grid_size * cell_size, cell_size):
        for y in range(0, grid_size * cell_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

def draw_units_and_obstacles(screen, player_pos, enemies, obstacles, cell_size):
    # Draw obstacles
    for (ox, oy) in obstacles:
        obstacle_rect = pygame.Rect(ox * cell_size, oy * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (139, 69, 19), obstacle_rect)

    # Draw player
    player_rect = pygame.Rect(player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)

    # Draw all enemies
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy["pos"][0] * cell_size, enemy["pos"][1] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), enemy_rect)
