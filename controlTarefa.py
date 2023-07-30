import model 
import pandas as pd




import pandas as pd

class Tarefa:
    def __init__(self, x1, x2, x3, x4):
        self.idTarefa = int(x1)
        self.nomeTarefa = str(x2)
        self.dataFinal = str(x3)
        self.descricao = str(x4)

def adicionarTabela(x):
    df = carregarDataframe()
    df2 = pd.DataFrame({
        'idTarefa': [x.idTarefa],
        'nomeTarefa': [x.nomeTarefa],
        'dataFinal': [x.dataFinal],
        'descricao': [x.descricao]
    })
    novaTabela = pd.concat([df, df2])
    salvarDataframe(novaTabela)

def printarTarefaConsole(x):
    print(x.idTarefa)
    print(x.nomeTarefa)
    print(x.dataFinal)
    print(x.descricao)

def printDf():
    df = carregarDataframe()
    print(df)

def carregarDataframe():
    return pd.read_csv('tabelas/tarefa.csv', sep=';')

def salvarDataframe(df):
    df.to_csv('tabelas/tarefa.csv', sep=';', index=False)

def procurar_Tarefa(coluna, elemento):
    df = carregarDataframe()
    row = df[df[coluna] == elemento]
    if len(row) > 0:
        row = row.iloc[0]
        tarefa = model.Tarefa(row['idTarefa'], row['nomeTarefa'], row['dataFinal'], row['descricao'])
        return tarefa
    else:
        return None

####################################################################



def excluirTarefa(x):
    print( 'usuario excluido')


