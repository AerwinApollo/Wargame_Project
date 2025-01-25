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

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wargame Grid")

# Initial positions for player and enemy (grid coordinates)
player_pos = [0, 0]  # Top-left corner
enemy_pos = [GRID_SIZE - 1, GRID_SIZE - 1]  # Bottom-right corner

# Turn tracker
current_turn = "player"  # Start with the player's turn

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Function to draw units on the grid
def draw_units():
    # Draw player
    player_rect = pygame.Rect(player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Draw enemy
    enemy_rect = pygame.Rect(enemy_pos[0] * CELL_SIZE, enemy_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, enemy_rect)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player Turn Logic
        if current_turn == "player" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_pos[1] > 0:
                player_pos[1] -= 1
            if event.key == pygame.K_DOWN and player_pos[1] < GRID_SIZE - 1:
                player_pos[1] += 1
            if event.key == pygame.K_LEFT and player_pos[0] > 0:
                player_pos[0] -= 1
            if event.key == pygame.K_RIGHT and player_pos[0] < GRID_SIZE - 1:
                player_pos[0] += 1

            # Check for game over
            if player_pos == enemy_pos:
                print("Game Over! The enemy caught you!")
                running = False

            # End the player's turn
            current_turn = "enemy"

    # Enemy Turn Logic
    if current_turn == "enemy":
        # Render the "Enemy Turn" message and grid before the enemy moves
        screen.fill(BLACK)
        draw_grid()
        draw_units()

        # Display "Enemy Turn"
        font = pygame.font.Font(None, 36)
        turn_text = font.render("Enemy Turn", True, WHITE)
        screen.blit(turn_text, (10, 10))
        pygame.display.flip()

        # Pause for 1 second to show "Enemy Turn" before moving
        pygame.time.delay(1000)

        # Enemy movement logic (basic AI)
        if enemy_pos[0] < player_pos[0]:
            enemy_pos[0] += 1
        elif enemy_pos[0] > player_pos[0]:
            enemy_pos[0] -= 1

        if enemy_pos[1] < player_pos[1]:
            enemy_pos[1] += 1
        elif enemy_pos[1] > player_pos[1]:
            enemy_pos[1] -= 1

        # Check for game over
        if player_pos == enemy_pos:
            print("Game Over! The enemy caught you!")
            running = False

        # End the enemy's turn
        current_turn = "player"

        # Render the screen immediately for "Player Turn"
        screen.fill(BLACK)
        draw_grid()
        draw_units()

        # Update the turn indicator to "Player Turn"
        font = pygame.font.Font(None, 36)
        turn_text = font.render("Player Turn", True, WHITE)
        screen.blit(turn_text, (10, 10))
        pygame.display.flip()

    # Rendering Section
    screen.fill(BLACK)
    draw_grid()
    draw_units()

    # Render turn indicator
    font = pygame.font.Font(None, 36)
    if current_turn == "player":
        turn_text = font.render("Player Turn", True, WHITE)
    else:
        turn_text = font.render("Enemy Turn", True, WHITE)
    screen.blit(turn_text, (10, 10))

    pygame.display.flip()