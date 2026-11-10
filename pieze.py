import pygame
from enum import Enum
from pathlib import Path
from mouse import Mouse


class Color(Enum):
    blanco = 0
    negro = 1

class Nombre(Enum):
    peon = 0
    torre = 1
    caballo = 2
    alfil = 3
    reina = 4
    rey = 5

class Piece():
    def __init__(self, x,y,width,height,texture, color, nombre):
        self.x = x
        self.y = y
        self.width = width
        self.height = height        
        self.texture = texture
        self.color = color
        self.nombre = nombre
    def draw(self, screen):
        screen.blit(self.texture)
class Pawn(Piece):
   pass
class Rook(Piece):
    pass
class Knight(Piece):
   pass
class Bishop(Piece):
    pass
class Queen(Piece):
    pass
class King(Piece):
   pass

def CreatePieces(rows, cols, celWidth, celHeight, chipWidth, chipHeigth ):
    image_path = Path(__file__).resolve().parent / "img" / "SpritePieces.png"
    image_surface = pygame.image.load(str(image_path)).convert_alpha()

    #superficie es la imagen reescalada.
    surface = pygame.transform.scale(image_surface,(image_surface.get_width(),image_surface.get_height()))

    #creando tamaño del recorte
    recorte = pygame.Surface((celWidth, celHeight), pygame.SRCALPHA)   

    piezasEsquema = [Nombre.torre, Nombre.caballo, Nombre.alfil, Nombre.reina, Nombre.rey, Nombre.alfil, Nombre.caballo, Nombre.torre]
    pieces = []
    board = []
    for i in range (rows):
        for j in range(cols):
            if i == 0:
                recorte = pygame.Surface((celWidth, celHeight), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(j * celWidth,0,celWidth,celHeight))
                if(piezasEsquema[j] == Nombre.torre):
                    pieces.append(Rook(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, piezasEsquema[j]))
                elif (piezasEsquema[j] == Nombre.caballo):
                    pieces.append(Knight(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, piezasEsquema[j]))
                elif (piezasEsquema[j] == Nombre.alfil):
                    pieces.append(Bishop(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, piezasEsquema[j]  ))
                elif (piezasEsquema[j] == Nombre.reina):
                    pieces.append(Queen(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, piezasEsquema[j]))
                elif (piezasEsquema[j] == Nombre.rey):
                    pieces.append(King(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, piezasEsquema[j]))
            if i == 1:
                recorte = pygame.Surface((celWidth, celHeight), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(800,0,celWidth,celHeight))
                pieces.append(Pawn(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, Nombre.peon))
            if i == 2 or i ==  3 or i ==  4 or i == 5:
                pieces.append(None)
            if i == 6:
                recorte = pygame.Surface((celWidth, celHeight), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(800,celWidth,celWidth,celHeight))
                pieces.append(Pawn(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro,Nombre.peon))
            if i == 7:
                recorte = pygame.Surface((celWidth, celHeight), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(j * celWidth,100,celWidth,celHeight))
                if(piezasEsquema[j] == Nombre.torre):
                    pieces.append(Rook(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, piezasEsquema[j]))
                elif (piezasEsquema[j] == Nombre.caballo):
                    pieces.append(Knight(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, piezasEsquema[j]))
                elif (piezasEsquema[j] == Nombre.alfil):
                    pieces.append(Bishop(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, piezasEsquema[j]  ))
                elif (piezasEsquema[j] == Nombre.reina):
                    pieces.append(Queen(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, piezasEsquema[j]))
                elif (piezasEsquema[j] == Nombre.rey):
                    pieces.append(King(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, piezasEsquema[j]))
        board.append(pieces)
        pieces = []
    return board

def drawSprite():
    pass