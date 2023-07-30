import model 
import pandas as pd




def adicionarTabela(x):
    dfX = carregarDataframe()
    df2 = pd.DataFrame({
        'idUser': [x.idUser],
        'nomeUser': [x.nomeUser],
        'senha': [x.senha],
        'email': [x.email]
    })
    novaTabela = pd.concat([dfX, df2])

    if (duplicidadeNome(x.nomeUser) == True):
        print("Registro Feito!")
        salvarDataframe(novaTabela)
    else:
        print("Registro Cancelado (Duplicidade)!")
    

def duplicidadeNome(y):
    if (procurar_usuario('nomeUser',y)) == None: ##NONE Q NAO TEM
        return True
    return False


def printarUsuarioConsole(x):
    print(x.idUser)
    print(x.nomeUser)
    print(x.senha)
    print(x.email)

def printDf():
    print(carregarDataframe())

def carregarDataframe():
    return (pd.read_csv('tabelas/usuario.csv', sep=';'))

def salvarDataframe(dx):
    dx.to_csv('tabelas/usuario.csv', sep=';', index=False)

def procurar_usuario(coluna, elemento):
    df = carregarDataframe()
    row = df[df[coluna] == elemento]
    if len(row) > 0:
        row = row.iloc[0]
        usuario = model.Usuario(row['idUser'], row['nomeUser'], row['senha'], row['email'])
        return usuario
    else:
        return None
    
####################################################################


def excluir_usuario(nome):
    x = carregarDataframe()
    x = x.drop(x[x['nomeUser'] == nome].index)
    salvarDataframe(x)

def consultar_dataframe():
    df = carregarDataframe()
    usuarios = []
    for _, row in df.iterrows():
        usuario = model.Usuario(row['idUser'], row['nomeUser'], row['senha'], row['email'])
        usuarios.append(usuario)
    return usuarios