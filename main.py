# Example file showing a basic pygame "game loop"
from enum import Enum
import pygame
import board
import pieze

from mouse import *
import math
pygame.init()

class Turno(Enum):
    black = 1
    white = 2
    
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
cellWidth = pieceWidth
cellHeigth = pieceHeight
pieces = []
gotIndex = False  
selectPiezeIndexX = 0
selectPiezeIndexY = 0         
initialized = False  
boardArray = pieze.CreatePieces(rows,cols, cellWidth, cellHeigth, pieceWidth, pieceHeight)
turno = Turno.white
raton = Mouse()
#######################




#Dibuja todas las piezas del ajedrez
def drawAllPieces():
    global boardArray
    global rows
    global cols
    for i in range (rows):
        for j in range (cols):
            if boardArray[i][j] != None:
                screen.blit(boardArray[i][j].texture, (boardArray[i][j].x, boardArray[i][j].y))


#funcion en desarrollo para mover piezas
def MoveChip():
    #variables globales
    global gotIndex
    global selectPiezeIndexX
    global selectPiezeIndexY
    global turno

    #si se presiona el click y no hay ninguna seleccionada.
    if raton.press == True  and not gotIndex:
        #se guarda la fila y la columna donde se hizo click
        selectPiezeIndexX = raton.xToIndex
        selectPiezeIndexY = raton.yToIndex

        #si hay una pieza en la fila y columna seleccionada y es del color del turno, se guarda que se ha seleccionado una pieza.
        if boardArray[selectPiezeIndexY][selectPiezeIndexX] != None and ((turno == Turno.white and boardArray[selectPiezeIndexY][selectPiezeIndexX].color == pieze.Color.blanco) or (turno == Turno.black and boardArray[selectPiezeIndexY][selectPiezeIndexX].color == pieze.Color.negro)) :
            #se ha seleccionado pieza
            gotIndex = True
    if raton.press and gotIndex:
            #la pieza seleccionada toma la posicion del raton.
            boardArray[selectPiezeIndexY][selectPiezeIndexX].x = raton.x - pieceWidth / 2
            boardArray[selectPiezeIndexY][selectPiezeIndexX].y = raton.y - pieceHeight / 2
    if raton.release and gotIndex:
            #si la pieza es soltada se guarda la fila y la columna donde se solto la pieza
            xindex = raton.xToIndex
            yindex = raton.yToIndex
           

            if boardArray[selectPiezeIndexY][selectPiezeIndexX].nombre == pieze.Nombre.peon:
                posiblesCasillas = [[selectPiezeIndexY + 1, selectPiezeIndexX], [selectPiezeIndexY + 1, selectPiezeIndexX - 1], [selectPiezeIndexY + 1, selectPiezeIndexX + 1]]  # Ejemplo de posiciones posibles para un peón
                #hacia delante 
                if boardArray[yindex][xindex] == None and posiblesCasillas[0][0] == yindex and posiblesCasillas[0][1] == xindex:
                    nuevaY = posiblesCasillas[0][0]
                    nuevaX = posiblesCasillas[0][1]
                    boardArray[nuevaY][nuevaX] = boardArray[selectPiezeIndexY][selectPiezeIndexX]
                    boardArray[nuevaY][nuevaX].x = nuevaX * 100 
                    boardArray[nuevaY][nuevaX].y = nuevaY * 100
                    boardArray[selectPiezeIndexY][selectPiezeIndexX] = None
                    gotIndex = False
                    if turno == Turno.white:
                        turno = Turno.black
                    else:
                        turno = Turno.white
                else : #si en la casilla donde se suelta la pieza hay otra pieza, se devuelve la pieza a su posicion original
                    boardArray[selectPiezeIndexY][selectPiezeIndexX].x = selectPiezeIndexX * pieceWidth
                    boardArray[selectPiezeIndexY][selectPiezeIndexX].y = selectPiezeIndexY *  pieceHeight
                    gotIndex = False   



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

    #dibuja todas las piezas
    drawAllPieces()

    #obtiene la posicion del raton en la pantalla
    raton.MousePosition(screenWidth,screenHeight)

    #obtiene el idice en y y en x en el que se encuentra el raton.
    raton.MousePositionToIndex(cellWidth,cellHeigth)

    #cuando se presiona el click
    raton.MousePress()

    #cuando se sueta el click
    raton.MouseRelease()

    #movimiento de las fichas
    MoveChip()





    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()