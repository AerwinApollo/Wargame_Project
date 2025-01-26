# Function to move the player
def move_player(player_pos, direction, obstacles, grid_size):
    if direction == "UP" and player_pos[1] > 0 and (player_pos[0], player_pos[1] - 1) not in obstacles:
        player_pos[1] -= 1
    elif direction == "DOWN" and player_pos[1] < grid_size - 1 and (player_pos[0], player_pos[1] + 1) not in obstacles:
        player_pos[1] += 1
    elif direction == "LEFT" and player_pos[0] > 0 and (player_pos[0] - 1, player_pos[1]) not in obstacles:
        player_pos[0] -= 1
    elif direction == "RIGHT" and player_pos[0] < grid_size - 1 and (player_pos[0] + 1, player_pos[1]) not in obstacles:
        player_pos[0] += 1
    return player_pos

# Function to move the enemy
def move_enemy(enemy_pos, player_pos, obstacles, grid_size):
    if (enemy_pos[0] + 1, enemy_pos[1]) not in obstacles and enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += 1
    elif (enemy_pos[0] - 1, enemy_pos[1]) not in obstacles and enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= 1

    if (enemy_pos[0], enemy_pos[1] + 1) not in obstacles and enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += 1
    elif (enemy_pos[0], enemy_pos[1] - 1) not in obstacles and enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= 1
    return enemy_pos
