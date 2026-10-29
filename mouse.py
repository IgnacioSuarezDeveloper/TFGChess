import pygame
import math
class Mouse():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xToIndex = 0
        self.yToIndex = 0
    def MousePosition(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
    def MousePositionToIndex(self):
        self.xToIndex =  math.trunc(abs(self.x / 100))
        self.yToIndex = math.trunc(abs(self.y / 100))
    
