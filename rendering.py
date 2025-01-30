import pygame

def draw_grid(screen, cell_size, grid_size):
    """Draws the grid on the screen."""
    for x in range(0, grid_size * cell_size, cell_size):
        for y in range(0, grid_size * cell_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

def draw_units_and_obstacles(screen, player_pos, enemies, obstacles, cell_size, targeted_enemy=None):
    font = pygame.font.Font(None, 24)  # Small font for labels

    # Draw obstacles
    for (ox, oy) in obstacles:
        obstacle_rect = pygame.Rect(ox * cell_size, oy * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (139, 69, 19), obstacle_rect)

    # Draw player
    player_rect = pygame.Rect(player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)

    # Draw enemies with different colors based on type
    for enemy in enemies:
        enemy_color = (255, 0, 0)  # Default Red
        if enemy["type"] == "Tank":
            enemy_color = (128, 0, 0)  # Darker Red
        elif enemy["type"] == "Fast":
            enemy_color = (255, 165, 0)  # Orange
        elif enemy["type"] == "Ranged":
            enemy_color = (0, 255, 0)  # Green
        elif enemy["type"] == "Unpredictable":
            enemy_color = (255, 255, 0)  # Yellow

        enemy_rect = pygame.Rect(enemy["pos"][0] * cell_size, enemy["pos"][1] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, enemy_color, enemy_rect)

def draw_damage_indicators(screen, damage_indicators, font):
    """Draws floating damage indicators on the screen."""
    for indicator in damage_indicators:
        indicator.draw(screen, font)
