class Tablero():

    def __init__(self, t, fila, colum):
        super(Tablero, self).__init__()
        self.tablero = t
        self.numlazosJ = 0
        self.numlazosA = 0
        self.numfilas = fila
        self.numColum = colum

    def getNumlazosA(self):
        return self.numlazosA

    def getNumlazosJ(self):
        return self.numlazosJ

    def getNumfilas(self):
        return self.numfilas

    def getNumColum(self):
        return self.numColum

    def setNumlazosA(self, nA):
        self.numlazosA = nA

    def setNumlazosJ(self, nJ):
        self.numlazosJ = nJ

    def setNumfilas(self, f):
        self.numfilas = f

    def crearTablero(self):
        i = cont = 0
        lineaPunto = True
        while(i <= (((self.getNumfilas() * 2) - 2) *
        ((self.getNumColum() * 2) - 1)) + ((self.getNumColum() * 2) - 2)):
            if i % 2 == 0 and lineaPunto is True:
                self.tablero[i] = "*"
            else:
                self.tablero[i] = ""
            if cont == ((self.getNumColum() * 2) - 2):
                if lineaPunto is True:
                    lineaPunto = False
                else:
                    lineaPunto = True
                cont = - 1
            i += 1
            cont += 1

    def turnosExtra(self, mov1, mov2, numlazos):
        nlazo = numlazos
        #print(mov1.valor, mov2.valor, "SSSSSs")
        m1 = min(mov1.valor, mov2.valor)
        m2 = max(mov1.valor, mov2.valor)
        if m1 + 1 == m2 - 1:
            #print(mov1.valor, mov2.valor)
            #Si el mov es horizontal, se evalua con el siguiente
            #fragmento de codigo hacia arriba
            if((m1 - self.numColum * 2) + 1 > 0):
                #print(mov1.valor, mov2.valor)
                if(self.tablero[(m1 - self.numColum * 2) + 1] == "|"):
                    if(self.tablero[(m2 - self.numColum * 2) + 1] == "|"):
                        if(self.tablero[m1 - ((self.numColum * 2) - 1)
                        * 2 + 1] == "-"):
                            nlazo += 1
            #Si el mov es horizontal, se evalua con el siguiente
            #fragmento de codigo hacia abajo
            if((m1 + self.numColum * 2) - 1 <=
            (self.numColum * 2 - 2) * self.numfilas * 2):
                if(self.tablero[(m1 + self.numColum * 2) - 1] == "|"):
                    if(self.tablero[(m2 + self.numColum * 2) - 1] == "|"):
                        if(self.tablero[m1 +
                        ((self.numColum * 2) - 1) * 2 + 1] == "-"):
                            nlazo += 1
            return [numlazos, nlazo]
        elif(m1 + (self.numColum * 2 - 1) == m2 - (self.numColum * 2 - 1)):
            #Si el mov es vertical, se evalua con el siguiente
            #fragmento de codigo hacia la izquierda
            if((m1 - 2) // (self.numColum * 2 - 1) ==
            m1 // (self.numColum * 2 - 1)):
                if(self.tablero[m1 - 1] == "-"):
                    if(self.tablero[m2 - 1] == "-"):
                        if(self.tablero[m1 - 2 +
                        ((self.numColum * 2) - 1)] == "|"):
                            nlazo += 1
            #Si el mov es vertical, se evalua con el siguiente
            #fragmento de codigo hacia la derecha
            if((m1 + 2) // (self.numColum * 2 - 1) ==
            m1 // (self.numColum * 2 - 1)):
                if(self.tablero[m1 + 1] == "-"):
                    if(self.tablero[m2 + 1] == "-"):
                        if(self.tablero[m1 + 2 +
                        ((self.numColum * 2) - 1)] == "|"):
                            nlazo += 1
            return [numlazos, nlazo]