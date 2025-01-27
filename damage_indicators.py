import pygame
import time

class DamageIndicator:
    def __init__(self, position, text, color, duration=1.0):
        self.position = position  # Position on the grid (in pixels)
        self.text = text  # Text to display (e.g., "-3")
        self.color = color  # Text color (e.g., red for damage)
        self.start_time = time.time()  # Time when the indicator was created
        self.duration = duration  # How long the indicator should last (in seconds)

    def is_expired(self):
        # Check if the indicator has expired
        return time.time() - self.start_time > self.duration

    def draw(self, screen, font):
        # Draw the text on the screen
        text_surface = font.render(self.text, True, self.color)
        x, y = self.position
        screen.blit(text_surface, (x, y - 20))  # Draw slightly above the position
