import pygame

class DamageIndicator:
    def __init__(self, position, text, color):
        self.x, self.y = position
        self.text = text
        self.color = color
        self.timer = 30  # Frames before the indicator disappears

    def is_expired(self):
        return self.timer <= 0

    def update(self):
        self.y -= 1  # Move indicator upward
        self.timer -= 1

    def draw(self, screen, font):
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))

def update_damage_indicators(damage_indicators):
    """Updates damage indicators, removing expired ones."""
    for indicator in damage_indicators:
        indicator.update()
    damage_indicators[:] = [indicator for indicator in damage_indicators if not indicator.is_expired()]

def draw_damage_indicators(screen, damage_indicators, font):
    """Renders all damage indicators on the screen."""
    for indicator in damage_indicators:
        indicator.draw(screen, font)
