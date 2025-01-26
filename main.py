import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 10  # Number of grid cells per row and column
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE  # Size of each grid cell

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # Player color
RED = (255, 0, 0)   # Enemy color
BROWN = (139, 69, 19)  # Obstacle color

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

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Function to draw units and obstacles on the grid
def draw_units_and_obstacles():
    # Draw obstacles
    for (ox, oy) in obstacles:
        obstacle_rect = pygame.Rect(ox * CELL_SIZE, oy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BROWN, obstacle_rect)

    # Draw player
    player_rect = pygame.Rect(player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Draw enemy
    enemy_rect = pygame.Rect(enemy_pos[0] * CELL_SIZE, enemy_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, enemy_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player Turn Logic
        if current_turn == "player" and event.type == pygame.KEYDOWN:
            # Player movement
            if event.key == pygame.K_UP and player_pos[1] > 0 and (player_pos[0], player_pos[1] - 1) not in obstacles:
                player_pos[1] -= 1
                current_turn = "enemy"  # End turn after movement
            elif event.key == pygame.K_DOWN and player_pos[1] < GRID_SIZE - 1 and (player_pos[0], player_pos[1] + 1) not in obstacles:
                player_pos[1] += 1
                current_turn = "enemy"  # End turn after movement
            elif event.key == pygame.K_LEFT and player_pos[0] > 0 and (player_pos[0] - 1, player_pos[1]) not in obstacles:
                player_pos[0] -= 1
                current_turn = "enemy"  # End turn after movement
            elif event.key == pygame.K_RIGHT and player_pos[0] < GRID_SIZE - 1 and (player_pos[0] + 1, player_pos[1]) not in obstacles:
                player_pos[0] += 1
                current_turn = "enemy"  # End turn after movement

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
        # Enemy checks if it can attack first
        if abs(enemy_pos[0] - player_pos[0]) + abs(enemy_pos[1] - player_pos[1]) == 1:
            player_hp -= enemy_attack
            print(f"Enemy attacked! Player HP: {player_hp}")
            if player_hp <= 0:
                print("The enemy defeated you! Game Over!")
                running = False  # Stop the game immediately
            else:
                current_turn = "player"  # End turn after attacking
        else:
            # Enemy movement toward the player if not adjacent
            if (enemy_pos[0] + 1, enemy_pos[1]) not in obstacles and enemy_pos[0] < player_pos[0]:
                enemy_pos[0] += 1
            elif (enemy_pos[0] - 1, enemy_pos[1]) not in obstacles and enemy_pos[0] > player_pos[0]:
                enemy_pos[0] -= 1

            if (enemy_pos[0], enemy_pos[1] + 1) not in obstacles and enemy_pos[1] < player_pos[1]:
                enemy_pos[1] += 1
            elif (enemy_pos[0], enemy_pos[1] - 1) not in obstacles and enemy_pos[1] > player_pos[1]:
                enemy_pos[1] -= 1

            current_turn = "player"  # End turn after moving

    # Rendering Section
    screen.fill(BLACK)
    draw_grid()
    draw_units_and_obstacles()

    # Display health points
    font = pygame.font.Font(None, 36)
    player_hp_text = font.render(f"Player HP: {player_hp}", True, WHITE)
    enemy_hp_text = font.render(f"Enemy HP: {enemy_hp}", True, WHITE)
    screen.blit(player_hp_text, (10, SCREEN_HEIGHT - 50))  # Bottom-left corner
    screen.blit(enemy_hp_text, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50))  # Bottom-right corner

    # Update the display
    pygame.display.flip()