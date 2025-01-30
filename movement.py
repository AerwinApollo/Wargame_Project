def move_player(player_pos, direction, obstacles, grid_size):
    new_pos = list(player_pos)
    if direction == "UP":
        new_pos[1] -= 1
    elif direction == "DOWN":
        new_pos[1] += 1
    elif direction == "LEFT":
        new_pos[0] -= 1
    elif direction == "RIGHT":
        new_pos[0] += 1

    if new_pos not in obstacles and 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
        return new_pos
    return player_pos

def move_enemy(enemy_pos, player_pos, obstacles, grid_size):
    dx = 1 if enemy_pos[0] < player_pos[0] else -1 if enemy_pos[0] > player_pos[0] else 0
    dy = 1 if enemy_pos[1] < player_pos[1] else -1 if enemy_pos[1] > player_pos[1] else 0

    new_pos = [enemy_pos[0] + dx, enemy_pos[1] + dy]
    return new_pos if new_pos not in obstacles and new_pos != player_pos else enemy_pos
