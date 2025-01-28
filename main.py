import pygame
import sys
from rendering import draw_grid, draw_units_and_obstacles
from movement import move_player, move_enemy
from combat import player_attack_enemy, enemy_attack_player, check_game_over
from damage_indicators import DamageIndicator

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 850  # Increased height for HUD
GRID_SIZE = 10
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wargame Grid")

# Font for text
font_size = min(SCREEN_WIDTH // 20, 48)  # Scale font dynamically
font = pygame.font.Font(None, font_size)

# Function to reset game state
def reset_game():
    global player_pos, enemies, player_hp, damage_indicators, current_turn, obstacles, turn_counter
    player_pos = [0, 0]
    player_hp = 10
    obstacles = [(3, 3), (4, 4), (5, 2), (2, 5), (6, 6)]

    # Define multiple enemies
    enemies = [
        {"pos": [9, 9], "hp": 10, "attack": 2},
        {"pos": [5, 5], "hp": 8, "attack": 3},
        {"pos": [7, 2], "hp": 12, "attack": 1}
    ]

    damage_indicators = []
    current_turn = "player"
    turn_counter = 0  # Reset turn counter

# Initialize game variables
reset_game()

# Game loop
running = True
game_over = False
targeted_enemy = None  # Store currently targeted enemy

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()
            game_over = False

        if not game_over and current_turn == "player" and event.type == pygame.KEYDOWN:
            targeted_enemy = None  # Reset targeted enemy each turn
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                direction = {pygame.K_UP: "UP", pygame.K_DOWN: "DOWN", pygame.K_LEFT: "LEFT", pygame.K_RIGHT: "RIGHT"}[event.key]
                player_pos = move_player(player_pos, direction, obstacles, GRID_SIZE)
                current_turn = "enemy"
            elif event.key == pygame.K_SPACE:
                targeted_enemy = player_attack_enemy(player_pos, enemies, 3, damage_indicators, CELL_SIZE)
                if check_game_over(player_hp, enemies):
                    game_over = True
                else:
                    current_turn = "enemy"

    if not game_over and current_turn == "enemy":
        for enemy in enemies:
            if abs(enemy["pos"][0] - player_pos[0]) + abs(enemy["pos"][1] - player_pos[1]) == 1:
                player_hp = enemy_attack_player(player_pos, [enemy], player_hp, damage_indicators, CELL_SIZE)
            else:
                enemy["pos"] = move_enemy(enemy["pos"], player_pos, obstacles + [e["pos"] for e in enemies if e != enemy], GRID_SIZE)

        if check_game_over(player_hp, enemies):
            game_over = True
        else:
            turn_counter += 1  # Increment turn counter after enemy turn
            current_turn = "player"

    screen.fill(BLACK)

    if game_over:
        message = font.render("Game Over! Press R to Restart", True, WHITE)
        screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 2 - message.get_height() // 2))
    else:
        draw_grid(screen, CELL_SIZE, GRID_SIZE)
        draw_units_and_obstacles(screen, player_pos, enemies, obstacles, CELL_SIZE, targeted_enemy)

        # Render health points and turn counter
        player_hp_text = font.render(f"Player HP: {player_hp}", True, WHITE)
        turn_counter_text = font.render(f"Turns: {turn_counter}", True, WHITE)
        screen.blit(player_hp_text, (10, SCREEN_HEIGHT - 80))
        screen.blit(turn_counter_text, (10, SCREEN_HEIGHT - 120))

        # Render Enemy HP for all enemies
        if enemies:
            for index, enemy in enumerate(enemies):
                enemy_hp_text = font.render(f"Enemy {index + 1} HP: {enemy['hp']}", True, WHITE)
                screen.blit(enemy_hp_text, (SCREEN_WIDTH - 250, 50 + (index * 30)))

        enemy_turn_text = font.render("Enemy Turn", True, WHITE)
        screen.blit(enemy_turn_text, (SCREEN_WIDTH // 2 - enemy_turn_text.get_width() // 2, SCREEN_HEIGHT - 150))

    pygame.display.flip()
