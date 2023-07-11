import pandas as pd

usuario = pd.DataFrame(columns=['idUser', 'nomeUser', 'cpf', 'email'])
usuario.to_csv('tabelas/usuario.csv', sep=';', index=False)


tarefa = pd.DataFrame(columns=['idTarefa', 'nomeTarefa', 'dataFinal', 'descricao'])
tarefa.to_csv('tabelas/tarefa.csv', sep=';', index=False)