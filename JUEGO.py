from random import shuffle, seed

seed(1717)


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
    
    def __init__(self):
        self.robar = list() # 24 cartas
        self.vistas = list() # Destapadas después de robar
        self.tablero = list()
        self.colocadas = list()
        self.destapadas = list()
        
        
    def IniciarJuego(self):
        todas_cartas = Baraja()
        shuffle(todas_cartas)
        for i in todas_cartas: print(i)
        print()
        
        for pos in range(1,8):
            column = []

            for long_col in range(pos):
                column.append(todas_cartas.pop())
                
            for i in column:print(i)
            print()
            self.tablero.append(column)
            
        self.robar = todas_cartas
        print(len(self.robar))
        for i in self.robar:print(i)
        
J = Juego()
J.IniciarJuego()
        
        
#for i in Baraja():print(i)