import pygame
import math
class Mouse():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xToIndex = 0
        self.yToIndex = 0
        self.press = False
        self.release = False
    def MousePosition(self, screenWidth, screenHeigth):
        if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= screenWidth and pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= screenHeigth:
            self.x = pygame.mouse.get_pos()[0]
            self.y = pygame.mouse.get_pos()[1]
    def MousePositionToIndex(self,cellWidth, cellHeigth):
        self.xToIndex =  math.trunc(abs(self.x / cellWidth))
        self.yToIndex = math.trunc(abs(self.y / cellHeigth))
    def MousePress(self):
        self.press = pygame.mouse.get_pressed()[0]
    def MouseRelease(self):
        self.release = not pygame.mouse.get_pressed()[0]
