import model
import pandas as pd




def adicionarTabela(x):
    dfX = carregarDataframe()
    df2 = pd.DataFrame({
        'idUser': [x.idUser],
        'nomeUser': [x.nomeUser],
        'cpf': [x.cpf],
        'email': [x.email]
    })
    novaTabela = pd.concat([dfX, df2])
    salvarDataframe(novaTabela)



def printarUsuarioConsole(x):
    print(x.idUser)
    print(x.nomeUser)
    print(x.cpf)
    print(x.email)

def printDf():
    print(carregarDataframe())

def carregarDataframe():
    return (pd.read_csv('tabelas/usuario.csv', sep=';'))

def salvarDataframe(dx):
    dx.to_csv('tabelas/usuario.csv', sep=';', index=False)

    

