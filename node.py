import pygame
import random
from constants import *

class Node:
    def __init__(self, x, y, value, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.left = None
        self.right = None
        self.value = value
        self.FONT = pygame.font.Font(None, 50)
        self.color = "red"
    
    def draw(self):
        if self.left:
            pygame.draw.line(self.screen, "white", (self.x, self.y), (self.left.x, self.left.y), LINE_WIDTH)
        if self.right:
            pygame.draw.line(self.screen, "white", (self.x, self.y), (self.right.x, self.right.y), LINE_WIDTH)
        
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), OUTER_RADIUS)
        # pygame.draw.circle(self.screen, "blue", (self.x, self.y), INNER_RADIUS)
        text = self.FONT.render(f"{self.value}", True, "black")
        text_rect = text.get_rect(center = (self.x, self.y))
        self.screen.blit(text, text_rect)