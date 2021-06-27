class Torre:
    def __init__(self, torreid = 0, name = "", adress = ""):
        self.torreid = torreid
        self.name = name
        self.adress = adress


    def register(self, torreid, name, adress):
        self.torreid = torreid
        self.name = name
        self.adress = adress

    def print(self):
        print(f'''-----Dados da Torre-----
Id     ----> {self.torreid}
Nome   ----> {self.name}
Adress ----> {self.adress}''')