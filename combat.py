import random
from damage_indicators import DamageIndicator

def player_attack_enemy(player_pos, enemies, player_attack, damage_indicators, cell_size):
    adjacent_enemies = [enemy for enemy in enemies if abs(enemy["pos"][0] - player_pos[0]) + abs(enemy["pos"][1] - player_pos[1]) == 1]
    
    if adjacent_enemies:
        target = adjacent_enemies[0]
        target["hp"] -= player_attack
        print(f"Player attacked! {target['type'].capitalize()} HP: {target['hp']}")

        # Add damage indicator
        pixel_pos = (target["pos"][0] * cell_size, target["pos"][1] * cell_size)
        damage_indicators.append(DamageIndicator(pixel_pos, f"-{player_attack}", (255, 0, 0)))

        if target["hp"] <= 0:
            print(f"{target['type'].capitalize()} defeated!")
            enemies.remove(target)

        return target  # Return the targeted enemy
    
    return None

def enemy_attack_player(player_pos, enemies, player_hp, damage_indicators, cell_size):
    for enemy in enemies:
        if player_hp <= 0:
            return 0  # Ensure no negative HP values

        enemy_type = enemy["type"]

        # Adjust attack logic based on enemy type
        if enemy_type == "grunt":
            damage = enemy["attack"]
        elif enemy_type == "brute":
            damage = enemy["attack"] + 1  # Brutes deal extra damage
        elif enemy_type == "scout":
            damage = enemy["attack"] if random.random() > 0.3 else 0  # Scouts miss 30% of the time

        if abs(enemy["pos"][0] - player_pos[0]) + abs(enemy["pos"][1] - player_pos[1]) == 1:
            player_hp -= damage
            print(f"{enemy_type.capitalize()} attacked! Player HP: {player_hp}")

            # Add damage indicator
            pixel_pos = (player_pos[0] * cell_size, player_pos[1] * cell_size)
            damage_indicators.append(DamageIndicator(pixel_pos, f"-{damage}", (255, 0, 0)))

            if player_hp <= 0:
                print("The enemy defeated you! Game Over!")
                return 0  # Stop further damage calculations

    return player_hp

def check_game_over(player_hp, enemies):
    if player_hp <= 0:
        print("The enemy defeated you! Game Over!")
        return True
    elif not enemies:
        print("You defeated all enemies! Victory!")
        return True
    return False
