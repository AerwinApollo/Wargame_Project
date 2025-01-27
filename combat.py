from damage_indicators import DamageIndicator

def player_attack_enemy(player_pos, enemy_pos, enemy_hp, player_attack, damage_indicators, cell_size):
    if abs(player_pos[0] - enemy_pos[0]) + abs(player_pos[1] - enemy_pos[1]) == 1:  # Check adjacency
        enemy_hp -= player_attack
        print(f"Player attacked! Enemy HP: {enemy_hp}")
        # Add a damage indicator
        pixel_pos = (enemy_pos[0] * cell_size, enemy_pos[1] * cell_size)
        damage_indicators.append(DamageIndicator(pixel_pos, f"-{player_attack}", (255, 0, 0)))
    return enemy_hp

def enemy_attack_player(player_pos, enemy_pos, player_hp, enemy_attack, damage_indicators, cell_size):
    if abs(player_pos[0] - enemy_pos[0]) + abs(player_pos[1] - enemy_pos[1]) == 1:  # Check adjacency
        player_hp -= enemy_attack
        print(f"Enemy attacked! Player HP: {player_hp}")
        # Add a damage indicator
        pixel_pos = (player_pos[0] * cell_size, player_pos[1] * cell_size)
        damage_indicators.append(DamageIndicator(pixel_pos, f"-{enemy_attack}", (255, 0, 0)))
    return player_hp

def check_game_over(player_hp, enemy_hp):
    if enemy_hp <= 0:
        print("You defeated the enemy! You win!")
        return True
    elif player_hp <= 0:
        print("The enemy defeated you! Game Over!")
        return True
    return False
