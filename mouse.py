import pygame
import math
class Mouse():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xToIndex = 0
        self.yToIndex = 0
        self.press = False
    def MousePosition(self):
        if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= 800 and pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 800:
            self.x = pygame.mouse.get_pos()[0]
            self.y = pygame.mouse.get_pos()[1]
    def MousePositionToIndex(self):
        self.xToIndex =  math.trunc(abs(self.x / 100))
        self.yToIndex = math.trunc(abs(self.y / 100))
    def MousePress(self):
        self.press = pygame.mouse.get_pressed()[0]
    
    
