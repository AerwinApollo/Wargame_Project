from damage_indicators import DamageIndicator

def player_attack_enemy(player_pos, enemies, player_attack, damage_indicators, cell_size):
    adjacent_enemies = [enemy for enemy in enemies if abs(enemy["pos"][0] - player_pos[0]) + abs(enemy["pos"][1] - player_pos[1]) == 1]
    if adjacent_enemies:
        target = adjacent_enemies[0]
        target["hp"] -= player_attack
        print(f"Player attacked! Enemy HP: {target['hp']}")

        # Add damage indicator
        pixel_pos = (target["pos"][0] * cell_size, target["pos"][1] * cell_size)
        damage_indicators.append(DamageIndicator(pixel_pos, f"-{player_attack}", (255, 0, 0)))

        if target["hp"] <= 0:
            enemies.remove(target)

def enemy_attack_player(player_pos, enemies, player_hp, damage_indicators, cell_size):
    for enemy in enemies:
        if abs(enemy["pos"][0] - player_pos[0]) + abs(enemy["pos"][1] - player_pos[1]) == 1:
            player_hp -= enemy["attack"]
            print(f"Enemy attacked! Player HP: {player_hp}")

            # Add damage indicator
            pixel_pos = (player_pos[0] * cell_size, player_pos[1] * cell_size)
            damage_indicators.append(DamageIndicator(pixel_pos, f"-{enemy['attack']}", (255, 0, 0)))
    return player_hp

def check_game_over(player_hp, enemies):
    if player_hp <= 0:
        print("The enemy defeated you! Game Over!")
        return True
    elif not enemies:
        print("You defeated all enemies! Victory!")
        return True
    return False
