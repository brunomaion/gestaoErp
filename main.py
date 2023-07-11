import model
import controlUsuario
import controlTarefa


#ADD USUARIO
"""
 idUser = input("Digite o ID do usuário: ")
 nome = input("Digite o nome do usuário: ")
 cpf = input("Digite o cpf do usuário: ")
 email = input("Digite o email do usuário: ")
 usuario1 = model.Usuario(idUser, nome, cpf, email)
 controlUsuario.adicionarTabela(usuario1)

#RETORNAR OBJETO // ELEMENTOS
 elemento_procurado = 'brunosmaion@hotmail.com'
 coluna_procurada = 'email'
 resultado = controlUsuario.procurar_usuario(coluna_procurada, elemento_procurado)

 if resultado is not None:
     print(resultado.idUser, resultado.nomeUser, resultado.cpf, resultado.email)
 else:
     print("Usuário não encontrado.")
"""

"""
#ADD TAREFA
idTarefa = input("Digite o ID da tarefa: ")
nomeTarefa = input("Digite o nome da tarefa: ")
dataFinal = input("Digite a data final da tarefa: ")
descricao = input("Digite a descricao da tarefa: ")
tarefa1 = model.Tarefa(idTarefa, nomeTarefa, dataFinal, descricao)
controlTarefa.adicionarTabela(tarefa1)

# RETORNAR OBJETO // ELEMENTOS

elemento_procurado = 'balanco'
coluna_procurada = 'nomeTarefa'
resultado = controlTarefa.procurar_Tarefa(coluna_procurada, elemento_procurado)

if resultado is not None:
     print(resultado.idTarefa, resultado.nomeTarefa, resultado.dataFinal, resultado.descricao)
else:
     print("Tarefa não encontrada.")

"""