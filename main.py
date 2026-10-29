# Example file showing a basic pygame "game loop"
import pygame
import board
import pieze
from mouse import *
import math
pygame.init()

#variables
screenWidth = 800
screenHeight = screenWidth
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
rows = 8
cols = rows
pieceWidth = 100
pieceHeight = 100
cellWidth = 100
cellHeigth = 100
pieces = []
#######################




raton = Mouse()
boardArray = pieze.CreatePieces(rows,cols, cellWidth, cellHeigth, pieceWidth, pieceHeight)

def drawAllPieces():
    global boardArray
    global rows
    global cols
    for i in range (rows):
        for j in range (cols):
            if boardArray[i][j] != None:
                screen.blit(boardArray[i][j].texture, (boardArray[i][j].x, boardArray[i][j].y))

#bucle ######################
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    board.drawBoard(rows,cols,screen,pieceWidth,pieceHeight)
    
    drawAllPieces()
    raton.MousePosition()
    raton.MousePositionToIndex()
    if boardArray[raton.yToIndex][raton.xToIndex] != None:
        print(boardArray[raton.yToIndex][raton.xToIndex].nombre)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()