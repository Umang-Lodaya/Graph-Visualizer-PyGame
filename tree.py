import pygame
import random
from constants import *
from node import Node

class Tree:
    def __init__(self, screen):
        self.root = None
        self.startx, self.starty = WIDTH // 2, HEIGHT*0.25//1
        self.screen = screen
    
    def addNode(self):
        value = random.randint(1, 100)
        if not self.root:
            self.root = Node(self.startx, self.starty, value, self.screen)
        else:
            x, y = self.startx, self.starty
            current = self.root
            while True:
                p = random.randint(0, 1)
                y += DISTANCE
                # GO LEFT
                if value <= current.value:
                    x -= DISTANCE
                    if not current.left:
                        current.left = Node(x, y, value, self.screen)
                        break
                    else:
                        current = current.left

                # GO RIGHT
                else:
                    x += DISTANCE
                    if not current.right:
                        current.right = Node(x, y, value, self.screen)
                        break
                    else:
                        current = current.right
    
    def draw(self):
        self.__dfs(self.root)
    
    def __dfs(self, node):
        if node:
            node.draw()
            self.__dfs(node.left)
            self.__dfs(node.right)