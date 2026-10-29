import pygame

def drawBoard(rows,cols, screen, pieceWidth, pieceHeigth):
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen,"white", (j * pieceWidth, i * pieceHeigth, pieceWidth, pieceHeigth))
            else:
                pygame.draw.rect(screen,"blue", (j * pieceWidth, i * pieceHeigth, pieceWidth, pieceHeigth))

def InitBoard():
    global  board
    board = [[None for _ in range(8)] for _ in range(8)]
    