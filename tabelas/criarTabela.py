import pandas as pd

usuario = pd.DataFrame(columns=['idUser', 'nomeUser', 'cpf'])
usuario.to_csv('usuario.csv', sep=';', index=False)


tarefa = pd.DataFrame(columns=['idTarefa', 'nomeTarefa', 'dataFinal'])
usuario.to_csv('tarefa.csv', sep=';', index=False)