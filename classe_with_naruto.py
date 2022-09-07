class Aldeiadafolha:
    def __init__(self,nome,clan):
        self.nome = nome
        self.clan = clan

    def get_clan(self):
        return f"{self.nome} pertence ao clan {self.clan}"
        
class Ninja(Aldeiadafolha):
    def __init__(self, nome, clan,sonho,jutsu):
        self.sonho = sonho
        self.jutsu = jutsu
        super().__init__(nome, clan) 

    def get_sonho(self):
        return f"{self.nome}  tem o sonho de {self.sonho}"
    
    def get_jutsu(self):
        return f"{self.nome} usa muito o jutsu {self.jutsu}"

    def get_tipo_ninja(self):
        if self.nome == 'Naruto':
            return f"{self.nome} se tornou o 7 Hokage e é casado com Hinata e possui dois filhos. Ele foi treinado por Jiraya"
        if self.nome == 'Sasuke':
            return f"{self.nome} é um ninja com sede de vingança e é casado com a Sakura com quem teve uma filha. Ele foi treinado por Kakashi"
        if self.nome == 'Sakura':
            return f"{self.nome} é uma ninja inteligente e possui uma força incrivel e é casado com Sasuke. Ela foi treinada pela Tsunade" 

nome_ninja = Ninja('Naruto','Uzumaki','se tornar um Hokage','Multiplos clone das sombras')
print(nome_ninja.get_sonho())
print(nome_ninja.get_clan())
print(nome_ninja.get_jutsu())
print(nome_ninja.get_tipo_ninja())