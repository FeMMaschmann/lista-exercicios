from Torre import Torre

class Apartamento(Torre):
    def __init__(self, torreid, name, adress, apartamentoid = 0, number = "", vaga = 0):
        self.torre = Torre(torreid, name, adress)
        self.apartamentoid = apartamentoid
        self.number = number
        self.vaga = vaga
        self.next = None

    def register(self, apartamentoid, number, vaga):
        self.apartamentoid = apartamentoid
        self.number = number
        self.vaga = vaga

    def print(self):
        print(f'''-----Dados do apartamento-----
Id     ----> {self.apartamentoid}
Numero ----> {self.number}
Vaga   ----> {self.vaga}
Torre  ----> {self.torre.name}''')