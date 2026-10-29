import pygame
from enum import Enum

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

def CreatePieces(rows, cols, celWidth, celHeight, chipWidth, chipHeigth ):
    img = pygame.image.load("img/SpritePieces.png")


   #imagen
    image_surface = pygame.image.load("img/SpritePieces.png").convert_alpha()

    #superficie es la imagen reescalada.
    surface = pygame.transform.scale(image_surface,(image_surface.get_width(),image_surface.get_height()))

    #creando tamaño del recorte
    recorte = pygame.Surface((100, 100), pygame.SRCALPHA)   

    piezasEsquema = [Nombre.torre, Nombre.caballo, Nombre.alfil, Nombre.reina, Nombre.rey, Nombre.alfil, Nombre.caballo, Nombre.torre]
    pieces = []
    board = []
    for i in range (rows):
        for j in range(cols):
            if i == 0:
                recorte = pygame.Surface((100, 100), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(j * 100,0,100,100))
                pieces.append(Piece(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, piezasEsquema[j]))
            if i == 1:
                recorte = pygame.Surface((100, 100), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(800,0,100,100))
                pieces.append(Piece(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.blanco, Nombre.peon))
            if i == 2 or i ==  3 or i ==  4 or i == 5:
                pieces.append(None)
            if i == 6:
                recorte = pygame.Surface((100, 100), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(800,100,100,100))
                pieces.append(Piece(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, Nombre.peon))
            if i == 7:
                recorte = pygame.Surface((100, 100), pygame.SRCALPHA) 
                recorte.blit(surface,(0,0),pygame.Rect(j * 100,100,100,100))
                pieces.append(Piece(j * celWidth, i * celHeight, chipWidth,chipHeigth,recorte, Color.negro, piezasEsquema[j]))


        
        board.append(pieces)
        pieces = []
    return board

def drawSprite():
    pass