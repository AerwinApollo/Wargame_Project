import pygame

def draw_grid(screen, cell_size, grid_size):
    """Draws the grid on the screen."""
    for x in range(0, grid_size * cell_size, cell_size):
        for y in range(0, grid_size * cell_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

def draw_units_and_obstacles(screen, player_pos, enemies, obstacles, cell_size, targeted_enemy=None):
    """Draws the player, enemies, obstacles, and highlights targeted enemy."""
    font = pygame.font.Font(None, 24)  # Small font for labels

    # Draw obstacles
    for (ox, oy) in obstacles:
        obstacle_rect = pygame.Rect(ox * cell_size, oy * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (139, 69, 19), obstacle_rect)  # Brown for obstacles

    # Draw player
    player_rect = pygame.Rect(player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (0, 0, 255), player_rect)  # Blue for player

    # Draw all enemies
    for index, enemy in enumerate(enemies):
        enemy_rect = pygame.Rect(enemy["pos"][0] * cell_size, enemy["pos"][1] * cell_size, cell_size, cell_size)
        
        # Highlight targeted enemy with a yellow border
        if targeted_enemy and enemy == targeted_enemy:
            pygame.draw.rect(screen, (255, 255, 0), enemy_rect, 3)  # Yellow highlight
        
        pygame.draw.rect(screen, (255, 0, 0), enemy_rect)  # Red for enemies

        # Enemy label
        label = font.render(f"Enemy {index + 1}", True, (255, 255, 255))
        screen.blit(label, (enemy["pos"][0] * cell_size, enemy["pos"][1] * cell_size - 20))  # Label above enemy

def draw_damage_indicators(screen, damage_indicators, font):
    """Draws floating damage indicators on the screen."""
    for indicator in damage_indicators:
        indicator.draw(screen, font)
