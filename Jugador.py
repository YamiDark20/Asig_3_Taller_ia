import pygame
from pygame.locals import *
from Puntos import *


class Jugador():

    def __init__(self):
        super(Jugador, self).__init__()

    def mover(self, move, numColum, tablero):
        if(move[0] + 1 == move[1] - 1):
            tablero[move[0] + 1] = "-"
        elif(move[0] + numColum == move[1] - numColum):
            tablero[move[0] + numColum] = "|"
        else:
            return "Error"

    def conectar(self, pantalla, x1, y1, x2, y2):
        pygame.draw.line(pantalla, (0, 0, 0),
        (x1, y1), (x2, y2), 10)

    def realizarMov(self, encola, tablero, pantalla, numCol):
        if(encola[0].valor > encola[1].valor):
            if(encola[0].valor - 1 == encola[1].valor + 1):
                if(tablero[encola[0].valor - 1] != "-"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor - 1] = "-"
                    return "Agente"
            elif(encola[0].valor - numCol == encola[1].valor + numCol):
                if(tablero[encola[0].valor - numCol] != "|"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor - numCol] = "|"
                    return "Agente"
        elif(encola[0].valor < encola[1].valor):
            if(encola[0].valor + 1 == encola[1].valor - 1):
                if(tablero[encola[0].valor + 1] != "-"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor + 1] = "-"
                    return "Agente"
            elif(encola[0].valor + numCol == encola[1].valor - numCol):
                if(tablero[encola[0].valor + numCol] != "|"):
                    self.conectar(pantalla, encola[0].x, encola[0].y,
                    encola[1].x, encola[1].y)
                    tablero[encola[0].valor + numCol] = "|"
                    return "Agente"

    def haylazo(self, puntos, numlazos):
        nlazoJ = numlazos
        if puntos >= 30:
            #nlazoJ = numlazos
            numlazos += 1
        return nlazoJ, numlazos  # [N° lazos anterior, N° lazos actual]