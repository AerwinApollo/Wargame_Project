# Function for player attacking the enemy
def player_attack_enemy(player_pos, enemy_pos, enemy_hp, player_attack):
    if abs(player_pos[0] - enemy_pos[0]) + abs(player_pos[1] - enemy_pos[1]) == 1:  # Check adjacency
        enemy_hp -= player_attack
        print(f"Player attacked! Enemy HP: {enemy_hp}")
    return enemy_hp

# Function for enemy attacking the player
def enemy_attack_player(player_pos, enemy_pos, player_hp, enemy_attack):
    if abs(player_pos[0] - enemy_pos[0]) + abs(player_pos[1] - enemy_pos[1]) == 1:  # Check adjacency
        player_hp -= enemy_attack
        print(f"Enemy attacked! Player HP: {player_hp}")
    return player_hp

# Function to check if the game has ended
def check_game_over(player_hp, enemy_hp):
    if enemy_hp <= 0:
        print("You defeated the enemy! You win!")
        return True
    elif player_hp <= 0:
        print("The enemy defeated you! Game Over!")
        return True
    return False
