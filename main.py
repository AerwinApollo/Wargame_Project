import pygame
import sys
from rendering import draw_grid, draw_units_and_obstacles
from movement import move_player, move_enemy
from combat import player_attack_enemy, enemy_attack_player, check_game_over

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_SIZE = 10
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wargame Grid")

# Initial positions and stats
player_pos = [0, 0]
enemy_pos = [GRID_SIZE - 1, GRID_SIZE - 1]
player_hp = 10
enemy_hp = 10
player_attack = 3
enemy_attack = 2
obstacles = [(3, 3), (4, 4), (5, 2), (2, 5), (6, 6)]
current_turn = "player"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player Turn Logic
        if current_turn == "player" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_pos = move_player(player_pos, "UP", obstacles, GRID_SIZE)
                current_turn = "enemy"
            elif event.key == pygame.K_DOWN:
                player_pos = move_player(player_pos, "DOWN", obstacles, GRID_SIZE)
                current_turn = "enemy"
            elif event.key == pygame.K_LEFT:
                player_pos = move_player(player_pos, "LEFT", obstacles, GRID_SIZE)
                current_turn = "enemy"
            elif event.key == pygame.K_RIGHT:
                player_pos = move_player(player_pos, "RIGHT", obstacles, GRID_SIZE)
                current_turn = "enemy"
            elif event.key == pygame.K_SPACE:
                enemy_hp = player_attack_enemy(player_pos, enemy_pos, enemy_hp, player_attack)
                if check_game_over(player_hp, enemy_hp):
                    running = False
                else:
                    current_turn = "enemy"

    # Enemy Turn Logic
    if current_turn == "enemy" and enemy_hp > 0:
        if abs(enemy_pos[0] - player_pos[0]) + abs(enemy_pos[1] - player_pos[1]) == 1:
            player_hp = enemy_attack_player(player_pos, enemy_pos, player_hp, enemy_attack)
            if check_game_over(player_hp, enemy_hp):
                running = False
            else:
                current_turn = "player"
        else:
            enemy_pos = move_enemy(enemy_pos, player_pos, obstacles, GRID_SIZE)
            current_turn = "player"

    # Rendering Section
    screen.fill(BLACK)
    draw_grid(screen, CELL_SIZE, GRID_SIZE)
    draw_units_and_obstacles(screen, player_pos, enemy_pos, obstacles, CELL_SIZE)

    # Display health points
    font = pygame.font.Font(None, 36)
    player_hp_text = font.render(f"Player HP: {player_hp}", True, WHITE)
    enemy_hp_text = font.render(f"Enemy HP: {enemy_hp}", True, WHITE)
    screen.blit(player_hp_text, (10, SCREEN_HEIGHT - 60))  # Bottom-left corner
    screen.blit(enemy_hp_text, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 60))  # Bottom-right corner

    # Update the display
    pygame.display.flip()
