import pygame
import sys
from pygame.locals import *
from Puntos import *
from Tablero import *
from Jugador import *
from Agente import *

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
timer = pygame.font.match_font('times')


class TableroVisual():

    def __init__(self, fila, colum, pantalla, empieza):
        super(TableroVisual, self).__init__()
        self.fila = fila
        self.colum = colum
        self.jugador = Jugador()
        self.agente = Agente("Agente")
        self.puntos = []
        self.pantalla = pantalla
        self.empieza = empieza
        self.pantalla.fill(BLANCO)
        self.tablero = Tablero({}, self.fila, self.colum)
        self.tablero.crearTablero()
        self.agente.mundo = self.tablero
        self.iniciarPuntos()

    def iniciarPuntos(self):
        numEspF = numEspC = 0
        #Asignacion de numEspF
        if (self.fila >= 4 or self.fila <= 10) and self.colum == 4:
            numEspF = 260
        elif self.fila == 4 and self.colum == 5:
            numEspF = 220
        elif self.fila == 4 and self.colum == 6:
            numEspF = 185
        elif self.fila == 4 and self.colum == 7:
            numEspF = 160
        elif self.fila == 4 and self.colum == 8:
            numEspF = 145
        elif self.fila == 4 and self.colum == 9:
            numEspF = 130
        elif self.fila == 4 and self.colum == 10:
            numEspF = 120
        elif (self.fila >= 5 and self.fila <= 10) and self.colum == 5:
            numEspF = 220
        elif self.fila == 5 and self.colum == 6:
            numEspF = 185
        elif self.fila == 5 and self.colum == 7:
            numEspF = 160
        elif self.fila == 5 and self.colum == 8:
            numEspF = 145
        elif self.fila == 5 and self.colum == 9:
            numEspF = 130
        elif self.fila == 5 and self.colum == 10:
            numEspF = 120
        elif (self.fila >= 6 and self.fila <= 10) and self.colum == 6:
            numEspF = 185
        elif self.fila == 6 and self.colum == 7:
            numEspF = 160
        elif self.fila == 6 and self.colum == 8:
            numEspF = 145
        elif self.fila == 6 and self.colum == 9:
            numEspF = 130
        elif self.fila == 6 and self.colum == 10:
            numEspF = 120
        elif (self.fila >= 7 and self.fila <= 10) and self.colum == 7:
            numEspF = 160
        elif self.fila == 7 and self.colum == 8:
            numEspF = 145
        elif self.fila == 7 and self.colum == 9:
            numEspF = 130
        elif self.fila == 7 and self.colum == 10:
            numEspF = 120
        elif (self.fila >= 8 and self.fila <= 10) and self.colum == 8:
            numEspF = 145
        elif self.fila == 8 and self.colum == 9:
            numEspF = 130
        elif self.fila == 8 and self.colum == 10:
            numEspF = 120
        elif (self.fila >= 9 and self.fila <= 10) and self.colum == 9:
            numEspF = 130
        elif self.fila == 9 and self.colum == 10:
            numEspF = 120
        elif self.fila == 10:
            numEspF = 120

        #Asignacion de numEspC
        if (self.colum >= 4 and self.colum <= 10) and self.fila == 4:
            numEspC = 140
        elif self.colum == 4 and self.fila == 5:
            numEspC = 115
        elif self.colum == 4 and self.fila == 6:
            numEspC = 100
        elif self.colum == 4 and self.fila == 7:
            numEspC = 85
        elif self.colum == 4 and self.fila == 8:
            numEspC = 75
        elif self.colum == 4 and self.fila == 9:
            numEspC = 65
        elif self.colum == 4 and self.fila == 10:
            numEspC = 60
        elif (self.colum >= 5 and self.colum <= 10) and self.fila == 5:
            numEspC = 115
        elif self.colum == 5 and self.fila == 6:
            numEspC = 100
        elif self.colum == 5 and self.fila == 7:
            numEspC = 85
        elif self.colum == 5 and self.fila == 8:
            numEspC = 75
        elif self.colum == 5 and self.fila == 9:
            numEspC = 65
        elif self.colum == 5 and self.fila == 10:
            numEspC = 60
        elif (self.colum >= 6 and self.colum <= 10) and self.fila == 6:
            numEspC = 100
        elif self.colum == 6 and self.fila == 7:
            numEspC = 85
        elif self.colum == 6 and self.fila == 8:
            numEspC = 75
        elif self.colum == 6 and self.fila == 9:
            numEspC = 65
        elif self.colum == 6 and self.fila == 10:
            numEspC = 60
        elif (self.colum >= 7 and self.colum <= 10) and self.fila == 7:
            numEspC = 85
        elif self.colum == 7 and self.fila == 8:
            numEspC = 75
        elif self.colum == 7 and self.fila == 9:
            numEspC = 65
        elif self.colum == 7 and self.fila == 10:
            numEspC = 60
        elif (self.colum >= 8 and self.colum <= 10) and self.fila == 8:
            numEspC = 75
        elif self.colum == 8 and self.fila == 9:
            numEspC = 65
        elif self.colum == 8 and self.fila == 10:
            numEspC = 60
        elif (self.colum >= 9 and self.colum <= 10) and self.fila == 9:
            numEspC = 65
        elif self.colum == 9 and self.fila == 10:
            numEspC = 60
        elif self.colum == 10:
            numEspC = 60

        index = 0
        for j in range(1, self.colum + 1):
            aux = index
            for i in range(1, self.fila + 1):
                y = i * numEspC
                x = numEspF * j
                #print(index)
                self.puntos.append(Puntos(index, x, y, self.pantalla))
                index += (self.colum * 2 - 1) * 2
            index = aux + 2
        #print(index, self.tablero.tablero)
        #for i in range(1, self.fila + 1):
            #aux = index
            #for j in range(1, self.colum + 1):
                #x = i * numEspC
                #y = numEspF * j
                #print(index)
                #self.puntos.append(Puntos(index, x, y, self.pantalla))
                #index += (self.colum * 2 - 1) * 2
            #index = aux + 2

    def pintarTablero(self):
        encola = []
        turnoExtra = 0
        self.muestra_texto(self.pantalla, timer, "N° lazos de Jugador: "
        + str(self.tablero.getNumlazosJ()), ROJO, 17, 260, 20)
        self.muestra_texto(self.pantalla, timer, "N° lazos de Agente: "
        + str(self.tablero.getNumlazosA()), AZUL, 17, 80, 20)
        fin = False
        resultado = ""
        frame = 0
        movRealizado = []
        while True:
            if self.empieza == "Jugador":
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse = pygame.mouse.get_pos()
                        for c in self.puntos:
                            if(mouse[0] > c.circulo.topleft[0] and
                            mouse[1] > c.circulo.topleft[1] and
                            mouse[0] < c.circulo.bottomright[0] and
                            mouse[1] < c.circulo.bottomright[1]):
                                c.presionar()
                                if(len(list(filter(lambda i:
                                i.valor == c.valor, encola))) <= 0):
                                    encola.append(c)
                                else:
                                    encola.remove(c)
                if(len(encola) == 2 and
                (len(list(filter(lambda i:
                (i[0].valor == encola[0].valor and i[1].valor == encola[1].valor)
                or (i[0].valor == encola[1].valor
                and i[1].valor == encola[0].valor), movRealizado))) <= 0)):
                    #print(encola, movRealizado)
                    movRealizado.append(encola)
                    if turnoExtra > 0:
                        turnoExtra -= 1
                    result = self.jugador.realizarMov(encola,
                    self.tablero.tablero, self.pantalla, (self.colum * 2) - 1)
                    encola[0].presionar()
                    encola[1].presionar()
                    self.verificarMov(encola[0], encola[1], ROJO)
                    nlazoJ, self.agente.mundo.numlazosJ = self.tablero.turnosExtra(
                    encola[0], encola[1], self.agente.mundo.numlazosJ)
                    if self.agente.mundo.numlazosJ > nlazoJ:
                        turnoExtra += self.agente.mundo.numlazosJ - nlazoJ
                        self.muestra_texto(self.pantalla, timer, "N° lazos de Jugador: "
                        + str(nlazoJ), BLANCO, 17, 260, 20)
                        self.muestra_texto(self.pantalla, timer, "N° lazos de Jugador: "
                        + str(self.agente.mundo.numlazosJ), ROJO, 17, 260, 20)
                    if turnoExtra == 0:
                        self.empieza = "Agente"
                    encola = []
                elif(len(encola) == 2):
                    encola[0].presionar()
                    encola[1].presionar()
                    encola = []
            elif self.empieza == "Agente":
                if turnoExtra > 0:
                    turnoExtra -= 1
                nlazo = self.agente.mundo.numlazosA
                mov, result = self.agente.escogerMov()
                p1 = None
                p2 = None
                for punt in self.puntos:
                    if punt.valor == mov[0]:
                        p1 = punt
                    elif punt.valor == mov[1]:
                        p2 = punt
                #print(p1.valor, p2.valor)
                movRealizado.append([p1, p2])
                pygame.draw.line(self.pantalla, NEGRO, (p1.x, p1.y),
                (p2.x, p2.y), 10)
                self.verificarMov(p1, p2, AZUL)
                if self.agente.mundo.numlazosA > nlazo:
                    turnoExtra += self.agente.mundo.numlazosA - nlazo
                    self.muestra_texto(self.pantalla, timer, "N° lazos de Agente: "
                    + str(nlazo), BLANCO, 17, 80, 20)
                    self.muestra_texto(self.pantalla, timer, "N° lazos de Agente: "
                    + str(self.agente.mundo.numlazosA), AZUL, 17, 80, 20)
                if turnoExtra == 0:
                    self.empieza = "Jugador"

            if fin is False:
                ganador = self.agente.fin_del_juego()
                if ganador is not None:
                    resultado = ganador
                    fin = True
                    self.empieza = ""

                for p in self.puntos:
                    p.pintarPunto()
            else:
                self.pantalla.fill(VERDE)
                tipoletra = pygame.font.Font(timer, 55)
                if resultado == "Empate":
                    f = tipoletra.render("El resultado del juego fue que el Agente y el Jugador empataron",
                    True, (255, 255, 255))
                else:
                    f = tipoletra.render(
                    "El ganador del juego fue el " + resultado,
                    True, (255, 255, 255))
                self.pantalla.blit(f, (int((1300 - f.get_width()) / 2),
                int(680 / 2 - f.get_height())))
                if frame == 200:
                    sys.exit()
                frame += 1

            ##Para actualizar la ventana
            pygame.display.flip()

    def muestra_texto(self, pantalla, fuente, texto,
    color, dimensiones, x, y):
        #dimensiones el tamaño en pixeles de la
        #fuente
        tipo_letra = pygame.font.Font(fuente,
        dimensiones)
        superficie = tipo_letra.render(texto, False,
        color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (x, y)
        pantalla.blit(superficie, rectangulo)

    def buscarPunto(self, valor):
        for p in self.puntos:
            if valor == p.valor:
                return p
        return None

    def verificarMov(self, mov1, mov2, color):
        m1 = min(mov1.valor, mov2.valor)
        m2 = max(mov1.valor, mov2.valor)
        if m1 + 1 == m2 - 1:
            #Si el mov es horizontal, se evalua con el siguiente
            #fragmento de codigo hacia arriba
            if((m1 - self.colum * 2) + 1 > 0):
                if(self.tablero.tablero[(m1 -
                self.colum * 2) + 1] == "|"):
                    if(self.tablero.tablero[(m2
                    - self.colum * 2) + 1] == "|"):
                        if(self.tablero.tablero[m1 -
                        ((self.colum * 2) - 1)
                        * 2 + 1] == "-"):
                            enviar = min(m1, m1 -
                            ((self.colum * 2) - 1) * 2)
                            punt = self.buscarPunto(enviar)
                            if punt is not None:
                                pygame.draw.rect(self.pantalla, color, (
                                punt.x, punt.y, self.puntos[0].x,
                                self.puntos[0].y))
            #Si el mov es horizontal, se evalua con el siguiente
            #fragmento de codigo hacia abajo
            if(((m1 + self.colum * 2) - 1 <=
            (self.colum * 2 - 2) * self.fila * 2) and self.colum == self.fila):
                #print(1)
                if(self.tablero.tablero[(m1 + self.colum * 2) - 1] == "|"):
                    if(self.tablero.tablero[(m2 + self.colum * 2) - 1] == "|"):
                        if(self.tablero.tablero[m1 +
                        ((self.colum * 2) - 1) * 2 + 1] == "-"):
                            enviar = min(m1, m1 +
                            ((self.colum * 2) - 1) * 2)
                            punt = self.buscarPunto(enviar)
                            if punt is not None:
                                pygame.draw.rect(self.pantalla, color, (
                                punt.x, punt.y, self.puntos[0].x,
                                self.puntos[0].y))
            elif((m1 + (self.colum * 2) - 2) + 1 <= self.tablero.maxElem):
                #print(2, m1, self.tablero.tablero[(m1 + self.colum * 2) - 1])
                if(self.tablero.tablero[(m1 + (self.colum * 2) - 2) + 1] == "|"):
                    if(self.tablero.tablero[(m2 + (self.colum * 2) - 2) + 1] == "|"):
                        if(self.tablero.tablero[m1 +
                        ((self.colum * 2) - 1) * 2 + 1] == "-"):
                            enviar = min(m1, m1 +
                            ((self.colum * 2) - 1) * 2)
                            punt = self.buscarPunto(enviar)
                            #print(m1, punt)
                            if punt is not None:
                                pygame.draw.rect(self.pantalla, color, (
                                punt.x, punt.y, self.puntos[0].x,
                                self.puntos[0].y))
        elif(m1 + (self.colum * 2 - 1) == m2 - (self.colum * 2 - 1)):
            #Si el mov es vertical, se evalua con el siguiente
            #fragmento de codigo hacia la izquierda
            if((m1 - 2) // (self.colum * 2 - 1) ==
            m1 // (self.colum * 2 - 1)):
                if(self.tablero.tablero[m1 - 1] == "-"):
                    if(self.tablero.tablero[m2 - 1] == "-"):
                        if(self.tablero.tablero[m1 - 2 +
                        ((self.colum * 2) - 1)] == "|"):
                            punt = self.buscarPunto(m1 - 2)
                            if punt is not None:
                                pygame.draw.rect(self.pantalla, color, (
                                punt.x, punt.y, self.puntos[0].x,
                                self.puntos[0].y))
            #Si el mov es vertical, se evalua con el siguiente
            #fragmento de codigo hacia la derecha
            if((m1 + 2) // (self.colum * 2 - 1) ==
            m1 // (self.colum * 2 - 1)):
                if(self.tablero.tablero[m1 + 1] == "-"):
                    if(self.tablero.tablero[m2 + 1] == "-"):
                        if(self.tablero.tablero[m1 + 2 +
                        ((self.colum * 2) - 1)] == "|"):
                            enviar = min(m1, m1 + 2)
                            punt = self.buscarPunto(enviar)
                            if punt is not None:
                                pygame.draw.rect(self.pantalla, color, (
                                punt.x, punt.y, self.puntos[0].x,
                                self.puntos[0].y))

#t = TableroVisual(6, 5, "", "")
#p1 = None
#p2 = None
#for punt in self.puntos:
    #if punt.valor == 78:
        #p1 = punt
    #elif punt.valor == 96:
        #p2 = punt
#print(t.tablero.tablero)
#print(p1, p2)