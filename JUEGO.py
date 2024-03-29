from random import shuffle

palos = {"r":"rombo",
         "p":"picas",
         "c":"corazones",
         "t":"treboles"}

class Carta:
    """
    Los palos son:
        rombos: r
        picas: p
        corazones: c
        treboles: t
        
    Los colores son:
        rombos y corazones: rojo
        picas y treboles: negro
    """
    def __init__(self):
        self.numero:int()
        self.palo:str()
        self.color:str()
        
    def __str__(self):
        if self.numero == 11:
            s = "J"
        elif self.numero == 12:
            s = "Q"
        elif self.numero == 13:
            s = "K"
        elif self.numero == 1:
            s = "A"
        else:
            s = str(self.numero)
        
        s += " " + palos[self.palo] + " " + self.color
        
        return s
        
        
def AsignarColor(c:Carta):
    if c.palo in ("r", "c"):
        c.color = "rojo"
    
    if c.palo in ("p", "t"):
        c.color = "negro"
        
    return
        
def Baraja() -> list:
    baraja = []
    for pl in ("r", "c", "p", "t"):
        for num in range(1, 14):
            c = Carta()
            c.palo = pl
            c.numero = num
            AsignarColor(c)
            baraja.append(c)
    
    return baraja

class Juego:
    """
    Posibles movimientos:
        De robar destapar a vistas
        De tablero destapar a destapadas
        De vistas mover a destapadas
        De destapadas mover a destapadas
        De colocadas mover a destapadas
        De destapadas subir a colocadas
        De vistas subir a colocadas
    """
    
    def __init__(self):
        self.robar = list() # 24 cartas
        self.vistas = list() # Destapadas después de robar
        self.tablero = list()
        self.colocadas = list()
        self.destapadas = list()
        
        
    def IniciarJuego(self):
        todas_cartas = Baraja()
        shuffle(todas_cartas)
        
        for pos in range(1,8):
            column = []

            for long_col in range(pos):
                column.append(todas_cartas.pop())
            
            destapa = [column.pop()]
                
            self.tablero.append(column)
            self.destapadas.append(destapa)
            
        self.robar = todas_cartas
        
        for posi in range(4):
            self.colocadas.append([])
        
        return
    

    def Mover(self, c:Carta, col:int):
        
        dest = self.destapadas[col] #Columna destino del tablero

        if c.numero == 13:
            if not len(dest) and not len(self.tablero[col]):
                self.destapadas[col].append(c)
                return True
            
        top = dest[len(dest) - 1] #Ultima carta columna
        if top.color != c.color and top.numero == c.numero + 1:
            self.destapadas[col].append(c)
            return True
        
        return False
    
    
    def Subir(self, c:Carta, col:int):
        
        dest = self.colocadas[col] #Columna destino para colocar
        if not len(dest):
            if c.numero == 1:
                dest.append(c)
                return True
            return False
            
        top = dest[len(dest) - 1] #Ultima carta columna
        
        if top.palo == c.palo and top.numero == c.numero - 1:
            self.colocadas[col].append(c)
            return True
        return False
    
    
    def DestaparRobar(self):
        
        if len(self.robar):
            self.vistas.append(self.robar.pop())
        else:
            while len(self.vistas):
                self.robar.append(self.vistas.pop())
                
        return
    
    
    def DestaparTablero(self, col:int):
        
        if (not len(self.destapadas[col])) and len(self.tablero[col]):
            self.destapadas[col].append(self.tablero[col].pop())
        
        return
    
    
    def MoverVistasDestapadas(self, col:int):
        carta = self.vistas[-1]
        if self.Mover(carta, col):
            self.vistas.pop()
            
        return
    
    
    def MoverColocadasDestapadas(self, ccol:int, dcol:int):
        carta = self.colocadas[ccol][-1]
        if self.Mover(carta, dcol):
            self.colocadas[ccol].pop()
    
        return
    
    
    def MoverEntreDestapadas(self, ocol:int, pos:int, dcol:int):
        carta = self.destapadas[ocol][pos]
        if self.Mover(carta, dcol):
            movidas = 1
            while pos + movidas < len(self.destapadas[ocol]):
                carta = self.destapadas[ocol][pos + movidas]
                self.Mover(carta, dcol)
                movidas += 1
                
            for _ in range(movidas):
                self.destapadas[ocol].pop()
        
        self.DestaparTablero(ocol)
        
        return
    
    
    def SubirDestapadasColocadas(self, ocol, dcol):
        carta = self.destapadas[ocol][-1]
        if self.Subir(carta, dcol):
            self.destapadas[ocol].pop()
            
        self.DestaparTablero(ocol)
        
        return
    
    
    def SubirVistasColocadas(self, dcol):
        carta = self.vistas[-1]
        if self.Subir(carta, dcol):
            self.vistas.pop()
            
        return
        
    
    def Mostrar(self):
        
        for i in self.robar:print(i)
        print()
        for m in self.vistas:print(m)
        print()
        
        for col in range(4):
            for l in self.colocadas[col]:print(l)
            print()
        print()
        for col in range(7):
            print(col)
            for j in self.tablero[col]: print(j)
            print()
            for k in self.destapadas[col]: print(k)
            print()