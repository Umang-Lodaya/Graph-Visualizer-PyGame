import sys
import pygame
from constants import *
from tree import Tree
from traversal import *

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.TREE = Tree(self.SCREEN)

    def run(self):
        print("RUNNING...")
        for _ in range(10):
            self.TREE.addNode()

        while True:
            self.SCREEN.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("QUIT!")
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        print("d")
                        dfs(self.TREE.root)

            pygame.display.set_caption(str(self.CLOCK.get_fps()))

            self.TREE.draw()
            pygame.display.update()
            self.CLOCK.tick(FPS)
    
if __name__ == "__main__":
    G = Game()
    G.run()