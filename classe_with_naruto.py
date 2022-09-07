class Aldeiadafolha:
    def __init__(self,nome,clan):
        self.nome = nome
        self.clan = clan
    
class Ninja(Aldeiadafolha):
    def __init__(self, nome, clan,sonho,jutsu):
        self.sonho = sonho
        self.jutsu = jutsu
        super().__init__(nome, clan)  
                                                                                                        
    def tipo_ninja(self):
        if self.nome == 'Naruto':
            return f"{self.nome},é um ninja da Aldeia da folha que pertence ao clan {self.clan}.Ele sempre usa o jutsu {self.jutsu} e o seu grande sonho è {self.sonho}"
        if self.nome == 'Sasuke':
            return f"{self.nome},é um ninja da Aldeia da folha que pertence ao clan {self.clan}.Ele sempre usa o jutsu {self.jutsu} e o seu grande sonho è {self.sonho}"
        if self.nome == 'Sakura':
            return f"{self.nome},é um ninja da Aldeia da folha que pertence ao clan {self.clan}.Ele sempre usa o jutsu {self.jutsu} e o seu grande sonho è {self.sonho}"

nome_ninja = Ninja('Naruto','Uzumaki','se tornar um Hokage','Multiplos clone das sombras')
print(nome_ninja.tipo_ninja())