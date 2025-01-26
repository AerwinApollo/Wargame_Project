import pygame
import sys
from rendering import draw_grid, draw_units_and_obstacles  # Import rendering functions
from movement import move_player, move_enemy  # Import movement functions

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_SIZE = 10  # Number of grid cells per row and column
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE  # Size of each grid cell

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wargame Grid")

# Initial positions for player and enemy (grid coordinates)
player_pos = [0, 0]  # Top-left corner
enemy_pos = [GRID_SIZE - 1, GRID_SIZE - 1]  # Bottom-right corner

# Health points and attack damage
player_hp = 10
enemy_hp = 10
player_attack = 3
enemy_attack = 2

# Hardcoded obstacle positions (grid coordinates)
obstacles = [(3, 3), (4, 4), (5, 2), (2, 5), (6, 6)]

# Turn tracker
current_turn = "player"  # Start with the player's turn

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player Turn Logic
        if current_turn == "player" and event.type == pygame.KEYDOWN:
            # Handle player movement
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

            # Player attack
            elif event.key == pygame.K_SPACE:
                if abs(player_pos[0] - enemy_pos[0]) + abs(player_pos[1] - enemy_pos[1]) == 1:
                    enemy_hp -= player_attack
                    print(f"Player attacked! Enemy HP: {enemy_hp}")
                    if enemy_hp <= 0:
                        print("You defeated the enemy! You win!")
                        running = False  # Stop the game immediately
                    else:
                        current_turn = "enemy"  # End turn after attacking

    # Enemy Turn Logic
    if current_turn == "enemy" and enemy_hp > 0:  # Ensure the enemy only acts if it’s alive
        if abs(enemy_pos[0] - player_pos[0]) + abs(enemy_pos[1] - player_pos[1]) == 1:
            player_hp -= enemy_attack
            print(f"Enemy attacked! Player HP: {player_hp}")
            if player_hp <= 0:
                print("The enemy defeated you! Game Over!")
                running = False  # Stop the game immediately
            else:
                current_turn = "player"  # End turn after attacking
        else:
            enemy_pos = move_enemy(enemy_pos, player_pos, obstacles, GRID_SIZE)
            current_turn = "player"  # End turn after moving

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
