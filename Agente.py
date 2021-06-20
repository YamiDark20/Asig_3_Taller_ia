import copy
from Tablero import *
from Jugador import *


class Agente():

    def __init__(self, color):
        super(Agente, self).__init__()
        self.color = color
        self.valor = 0
        self.profundidad = 0
        self.siguienteEstado = None
        self.mejorEstado = None
        self.alpha = -9999
        self.beta = 9999
        self.mundo = None

    def mover(self, mov):
        aux = (self.mundo.getNumColum() * 2) - 1
        if(mov[0] + 1 == mov[1] - 1):
            self.mundo.tablero[mov[0] + 1] = "-"
        elif(mov[0] + aux == mov[1] - aux):
            self.mundo.tablero[mov[0] + aux] = "|"
        else:
            return "Error"

    def puntuacion(self, mov, jugador):
        #Aqui vemos si el movimiento es horizontal, se revisara
        #de izquierda a derecha de este, para ver cuantos puntos
        #produce, lo mismo ocurre si el movimiento fuera vertical, lo
        #que cambiaria es que se revisaria de arriba hacia abajo. Si el
        #movimiento produce una puntuacion de 30 en unas de las condiciones,
        #es decir entra en una condicion que la puntuacion que se da es 30,
        #entonces se diria que se formo un lazo, a partir de este movimiento
        #asi que se le suma 1 al numero de lazos del jugador
        puntos = 0
        if(mov[0] + 1 == mov[1] - 1):
            #Si el mov es horizontal, se evalua con el siguiente
            #fragmento de codigo hacia arriba
            if((mov[0] - self.mundo.getNumColum() * 2) + 1 > 0):
                if(self.mundo.tablero[(mov[0] -
                self.mundo.getNumColum() * 2) + 1] == "|"):
                    if(self.mundo.tablero[(mov[1]
                    - self.mundo.getNumColum() * 2) + 1] == "|"):
                        if(self.mundo.tablero[mov[0] -
                        ((self.mundo.getNumColum() * 2) - 1)
                        * 2 + 1] == "-"):
                            puntos = 30
                            if jugador == "Agente":
                                self.mundo.numlazosA += 1
                            else:
                                self.mundo.numlazosJ += 1
                        else:
                            puntos = 5
                    else:
                        if(self.mundo.tablero[mov[0] -
                        ((self.mundo.getNumColum() * 2) - 1)
                        * 2 + 1] == "-"):
                            puntos = 5
                        else:
                            puntos = 20
            if(mov[1] - (self.mundo.getNumColum() * 2) + 1 > 0 and puntos == 0):
                if(self.mundo.tablero[(mov[1]
                    - self.mundo.getNumColum() * 2) + 1] == "|"):
                    if(self.mundo.tablero[mov[0] -
                    ((self.mundo.getNumColum() * 2) - 1)
                    * 2 + 1] == "-"):
                        puntos = 5
                    else:
                        puntos = 20
                else:
                    if(self.mundo.tablero[mov[0] -
                    ((self.mundo.getNumColum() * 2) - 1)
                    * 2 + 1] == "-"):
                        puntos = 20
                    else:
                        puntos = 10

            #Si el mov es horizontal, se evalua con el siguiente
            #fragmento de codigo hacia abajo
            if((mov[0] + self.mundo.getNumColum() * 2) - 1 <=
            (self.mundo.getNumColum() * 2 - 2) * self.mundo.getNumfilas() * 2):
                if(self.mundo.tablero[(mov[0] +
                self.mundo.getNumColum() * 2) - 1] == "|"):
                    if(self.mundo.tablero[(mov[1]
                    + self.mundo.getNumColum() * 2) - 1] == "|"):
                        if(self.mundo.tablero[mov[0] +
                        ((self.mundo.getNumColum() * 2) - 1) * 2 + 1] == "-"):
                            if jugador == "Agente" and puntos != 30:
                                self.mundo.numlazosA += 1
                            else:
                                self.mundo.numlazosJ += 1
                            if(puntos == 10):
                                puntos = 30
                            else:
                                puntos += 30
                        else:
                            if(puntos == 10):
                                puntos = 5
                            else:
                                if puntos == 20:
                                    puntos -= 5
                                else:
                                    puntos += 5
                    else:
                        if(self.mundo.tablero[mov[0] +
                        ((self.mundo.getNumColum() * 2) - 1)
                        * 2 + 1] == "-"):
                            if(puntos == 10):
                                puntos = 5
                            else:
                                if puntos == 20:
                                    puntos -= 5
                                else:
                                    puntos += 5
                        else:
                            if(puntos == 10):
                                puntos = 20
                            else:
                                if puntos == 5:
                                    puntos = 20 - puntos
                                else:
                                    puntos += 20
                else:
                    if(self.mundo.tablero[(mov[1]
                    + self.mundo.getNumColum() * 2) - 1] == "|"):
                        if(self.mundo.tablero[mov[0] +
                        ((self.mundo.getNumColum() * 2) - 1) * 2 + 1] == "-"):
                            if(puntos == 10):
                                puntos = 5
                            else:
                                if puntos == 20:
                                    puntos -= 5
                                else:
                                    puntos += 5
                        else:
                            if(puntos == 10):
                                puntos = 20
                            else:
                                if puntos == 5:
                                    puntos = 20 - puntos
                                else:
                                    puntos += 20
                    else:
                        if(self.mundo.tablero[mov[0] +
                        ((self.mundo.getNumColum() * 2) - 1)
                        * 2 + 1] == "-"):
                            if(puntos == 10):
                                puntos = 20
                            else:
                                if puntos == 5:
                                    puntos = 20 - puntos
                                else:
                                    puntos += 20
                        else:
                            if puntos == 0:
                                puntos = 10
                return puntos
            if(mov[1] + (self.mundo.getNumColum() * 2) + 1 <=
            (self.mundo.getNumColum() * 2 - 2) * self.mundo.getNumfilas() * 2):
                if(self.mundo.tablero[(
                mov[1] + self.mundo.getNumColum() * 2) - 1] == "|"):
                    if(self.mundo.tablero[mov[0] +
                    ((self.mundo.getNumColum() * 2) + 1)
                    * 2 + 1] == "-"):
                        if(puntos == 10):
                            puntos = 5
                        else:
                            if puntos == 20:
                                puntos -= 5
                            else:
                                puntos += 5
                    else:
                        if(puntos == 10):
                            puntos = 20
                        else:
                            if puntos == 5:
                                puntos = 20 - puntos
                            else:
                                puntos += 20

        elif(mov[0] + (self.mundo.getNumColum() * 2 - 1) ==
        mov[1] - (self.mundo.getNumColum() * 2 - 1)):
            #Si el mov es vertical, se evalua con el siguiente
            #fragmento de codigo hacia la izquierda
            if((mov[0] - 2) // (self.mundo.getNumColum() * 2 - 1) ==
            mov[0] // (self.mundo.getNumColum() * 2 - 1)):
                if(self.mundo.tablero[mov[0] - 1] == "-"):
                    if(self.mundo.tablero[mov[1] - 1] == "-"):
                        if(self.mundo.tablero[mov[0] - 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            puntos = 30
                            if jugador == "Agente":
                                self.mundo.numlazosA += 1
                            else:
                                self.mundo.numlazosJ += 1
                        else:
                            puntos = 5
                    else:
                        if(self.mundo.tablero[mov[0] - 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            puntos = 5
                        else:
                            puntos = 20
                else:
                    if(self.mundo.tablero[mov[1] - 1] == "-"):
                        if(self.mundo.tablero[mov[0] - 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            puntos = 5
                        else:
                            puntos = 20
                    else:
                        if(self.mundo.tablero[mov[0] - 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            puntos = 20
                        else:
                            puntos = 10

            #Si el mov es vertical, se evalua con el siguiente
            #fragmento de codigo hacia la derecha
            if((mov[0] + 2) // (self.mundo.getNumColum() * 2 - 1) ==
            mov[0] // (self.mundo.getNumColum() * 2 - 1)):
                if(self.mundo.tablero[mov[0] + 1] == "-"):
                    if(self.mundo.tablero[mov[1] + 1] == "-"):
                        if(self.mundo.tablero[mov[0] + 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            if jugador == "Agente" and puntos != 30:
                                self.mundo.numlazosA += 1
                            else:
                                self.mundo.numlazosJ += 1
                            if puntos == 10:
                                puntos = 30
                            else:
                                puntos += 30
                        else:
                            if puntos == 10:
                                puntos = 5
                            else:
                                if puntos == 20:
                                    puntos -= 5
                                else:
                                    puntos += 5
                    else:
                        if(self.mundo.tablero[mov[0] + 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            if puntos == 10:
                                puntos = 5
                            else:
                                if puntos == 20:
                                    puntos -= 5
                                else:
                                    puntos += 5
                        else:
                            if puntos == 10:
                                puntos = 20
                            else:
                                if puntos == 5:
                                    puntos = 20 - puntos
                                else:
                                    puntos += 20
                else:
                    if(self.mundo.tablero[mov[1] + 1] == "-"):
                        if(self.mundo.tablero[mov[0] + 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            if puntos == 10:
                                puntos = 5
                            else:
                                if puntos == 20:
                                    puntos -= 5
                                else:
                                    puntos += 5
                        else:
                            if puntos == 10:
                                puntos = 20
                            else:
                                if puntos == 5:
                                    puntos = 20 - puntos
                                else:
                                    puntos += 20
                    else:
                        if(self.mundo.tablero[mov[0] + 2 +
                        ((self.mundo.getNumColum() * 2) - 1)] == "|"):
                            if puntos == 10:
                                puntos = 20
                            else:
                                if puntos == 5:
                                    puntos = 20 - puntos
                                else:
                                    puntos += 20
                        else:
                            if puntos == 0:
                                puntos = 10
        return puntos

    def fin_del_juego(self):
        #En esta funcion solo se retornara el ganador del juego, donde
        #se sabe que se acabo el juego cuando ya no hay mas movimiento
        #por hacer, y se pasa entonces a verificar quien es el que ha
        #hecho mas lazo, y se retornara el mayor.
        cont = 1
        while cont < (((self.mundo.getNumfilas() * 2) - 2) *
        ((self.mundo.getNumColum() * 2) - 1)) + (
        (self.mundo.getNumColum() * 2) - 2):
            if self.mundo.tablero[cont] == "" and cont % 2 != 0:
                return None
            else:
                cont += 2
        if self.mundo.numlazosA > self.mundo.numlazosJ:
            return "Agente"
        elif self.mundo.numlazosA < self.mundo.numlazosJ:
            return "Jugador"
        else:
            return "Empate"

    def movValidos(self, jugador):
        mov = []
        i = 1
        index = 1
        tipoMov = "H"
        while(i < (((self.mundo.getNumfilas() * 2) - 2) *
        ((self.mundo.getNumColum() * 2) - 1)) + (
        (self.mundo.getNumColum() * 2) - 2)):
            if(self.mundo.tablero[i] == "" and tipoMov == "H"):
                mov.append([i - 1, i + 1])
            elif(self.mundo.tablero[i] == "" and tipoMov == "V"):
                valorC = (self.mundo.getNumColum() * 2) - 1
                if valorC >= i:
                    mov.append([valorC - i, i + valorC])
                else:
                    mov.append([i - valorC, i + valorC])
            if(index + 2 >= (
                self.mundo.getNumColum() * 2) - 1) and tipoMov == "H":
                if(tipoMov == "H"):
                    tipoMov = "V"
                else:
                    tipoMov = "H"
                index = - 1
            elif(index + 2 > (
            self.mundo.getNumColum() * 2) - 1) and tipoMov == "V":
                if(tipoMov == "H"):
                    tipoMov = "V"
                else:
                    tipoMov = "H"
                index = - 1
            if(index == - 1 and tipoMov == "V"):
                i += 2
            else:
                i += 2
            index += 2
        return mov

    def escogerMov(self):
        agente2 = Agente(self.color)
        agente2.mundo = copy.copy(self.mundo)
        agente2.mundo.tablero = copy.copy(self.mundo.tablero)
        agente2 = self.alfa_beta(agente2, "Jugador",
        {"Agente": "Jugador", "Jugador": "Agente"}, maxProf=4)
        movVal = self.movValidos(self.color)
        verificar = True
        while(agente2.mejorEstado is not None):
            if(agente2.color == self.color):
                for elem in movVal:
                    if elem == agente2.mejorEstado:
                        verificar = False
                if(verificar is True):
                    pass
                elif(verificar is False):
                    self.mover(agente2.mejorEstado)
                    #Se realiza la funcion puntuacion para aumentar o no
                    #el numlazos del agente
                    self.puntuacion(agente2.mejorEstado, "Agente")
                    return agente2.mejorEstado, agente2.valor
            agente2 = agente2.siguienteEstado

    def alfa_beta(self, agente, jugador, oponente, maxProf=5):
        alpha, beta = (agente.alpha, agente.beta)
        ganador = agente.fin_del_juego()
        movVal = agente.movValidos(agente.color)

        if(agente.profundidad < maxProf and (ganador is None or movVal != [])):
            for move in movVal:
                nextAgente = Agente(agente.color)
                nextAgente.profundidad = agente.profundidad + 1
                nextAgente.mundo = copy.copy(agente.mundo)
                nextAgente.mundo.tablero = copy.copy(self.mundo.tablero)
                nextAgente.mover(move)
                nextAgente.color = oponente[agente.color]
                ganador = nextAgente.fin_del_juego()
                puntos = nextAgente.puntuacion(move, oponente[agente.color])
                if nextAgente.color == "Agente":
                    nextAgente.valor = puntos
                else:
                    nextAgente.valor = puntos
                nextAgente.alpha = alpha
                nextAgente.beta = beta

                self.alfa_beta(nextAgente, jugador, oponente, maxProf)

                if(agente.color == "Agente"):
                    if((agente.siguienteEstado is None)
                    or nextAgente.valor > agente.valor):
                        agente.valor = nextAgente.valor
                        agente.siguienteEstado = nextAgente
                        agente.mejorEstado = move

                        alpha = max(alpha, agente.valor)
                        if(agente.valor >= beta):
                            return agente
                else:
                    if((agente.siguienteEstado is None)
                    or nextAgente.valor < agente.valor):
                        agente.siguienteEstado = nextAgente
                        agente.mejorEstado = move

                        beta = min(beta, agente.valor)
                        if(agente.valor <= alpha):
                            return agente
        return agente

    def dibujarTablero(self):
        acumulador = ""
        i = 0
        for key in self.mundo.tablero.keys():
            if(i < (self.mundo.getNumColum() * 2) - 1):
                if (self.mundo.tablero[key] == "|"
                or self.mundo.tablero[key] == "-"):
                    acumulador += " " + self.mundo.tablero[key]
                elif(self.mundo.tablero[key] == ""):
                    acumulador += "  "
                else:
                    acumulador += self.mundo.tablero[key]
                i += 1
            else:
                acumulador += "\n"
                i = 1
                acumulador += self.mundo.tablero[key]
        print(acumulador)

#a = Agente("Agente")
#t = Tablero({}, 6, 5)
#t.crearTablero()
#a.mundo = t
#Lo que esta comentado es para que el jugador comience primero
#while(True):
    #a.dibujarTablero()
    #mov1 = int(input("Movimiento de usuario del primer elemento: "))
    #mov2 = int(input("Movimiento de usuario del segundo elemento: "))
    #a.mover(list(sorted([mov1, mov2])))
    #punt = a.puntuacion(list(sorted([mov1, mov2])), "Jugador")
    #nlazoJ = 0
    #if punt >= 30:
        #nlazoJ = a.mundo.numlazosJ
        #a.mundo.numlazosJ += 1
    #while a.mundo.numlazosJ > nlazoJ:
        #a.dibujarTablero()
        #mov1 = int(input("Movimiento de usuario del primer elemento: "))
        #mov2 = int(input("Movimiento de usuario del segundo elemento: "))
        #a.mover(list(sorted([mov1, mov2])))
        #punt = a.puntuacion(list(sorted([mov1, mov2])), "Jugador")
        #nlazoJ = 0
        #if punt >= 30:
            #nlazoJ = a.mundo.numlazosJ
            #a.mundo.numlazosJ += 1
    #nlazo = a.mundo.numlazosA
    #a.escogerMov()
    #print(a.mundo.numlazosA, a.mundo.numlazosJ)
    #while a.mundo.numlazosA > nlazo:
        #a.dibujarTablero()
        #es = input("Espera: ")
        #nlazo = a.mundo.numlazosA
        #a.escogerMov()

#Lo siguiente es para que el agente comience primero
#j = Jugador()
#while(True):
    #a.dibujarTablero()
    #nlazo = a.mundo.numlazosA
    #a.escogerMov()
    #print(a.mundo.numlazosA, a.mundo.numlazosJ)
    #a.dibujarTablero()
    #while a.mundo.numlazosA > nlazo:
        #a.dibujarTablero()
        #es = input("Espera: ")
        #nlazo = a.mundo.numlazosA
        #a.escogerMov()

    #mov1 = int(input("Movimiento de usuario del primer elemento: "))
    #mov2 = int(input("Movimiento de usuario del segundo elemento: "))
    #j.mover(list(sorted([mov1, mov2])), (a.mundo.getNumColum() * 2) - 1,
    #a.mundo.tablero)
    #punt = a.puntuacion(list(sorted([mov1, mov2])), "Jugador")
    #nlazoJ, a.mundo.numlazosJ = j.haylazo(punt, a.mundo.numlazosJ)
    #while a.mundo.numlazosJ > nlazoJ:
        #a.dibujarTablero()
        #mov1 = int(input("Movimiento de usuario del primer elemento: "))
        #mov2 = int(input("Movimiento de usuario del segundo elemento: "))
        #j.mover(list(sorted([mov1, mov2])), (a.mundo.getNumColum() * 2) - 1,
        #a.mundo.tablero)
        #punt = a.puntuacion(list(sorted([mov1, mov2])), "Jugador")
        #nlazoJ, a.mundo.numlazosJ = j.haylazo(punt, a.mundo.numlazosJ)