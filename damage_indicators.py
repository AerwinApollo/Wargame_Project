import pygame
import time

class DamageIndicator:
    def __init__(self, position, text, color):
        self.position = position
        self.text = text
        self.color = color
        self.timer = 30  # Frames before the indicator disappears

    def is_expired(self):
        self.timer -= 1
        return self.timer <= 0

    def draw(self, screen, font):
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, self.position)

