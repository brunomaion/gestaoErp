
class Usuario:
    def __init__(self, x1, x2, x3, x4):
        self.idUser = int(x1)
        self.nomeUser = str(x2)
        self.cpf = str(x3)
        self.email = str(x4)


class Tarefa:
    def __init__(self, x1, x2, x3):
        self.idTarefa = int(x1)
        self.nomeTarefa = x2
        self.dataFinal = x3
    

        