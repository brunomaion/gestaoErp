import model
import controlUsuario
import controlTarefa
import os



#ADD USUARIO
"""
idUser = input("Digite o ID do usuário: ")
nome = input("Digite o nome do usuário: ")
senha = input("Digite a senha do usuário: ")
email = input("Digite o email do usuário: ")
usuario1 = model.Usuario(idUser, nome, senha, email)


controlUsuario.adicionarTabela(usuario1)
"""

"""
1
#RETORNAR OBJETO // ELEMENTOS
elemento_procurado = 'brunosmaion@hotmail.com'
coluna_procurada = 'email'
resultado = controlUsuario.procurar_usuario(coluna_procurada, elemento_procurado)

if resultado is not None:
    print(resultado.idUser, resultado.nomeUser, resultado.senha, resultado.email)
else:
    print("Usuário não encontrado.")


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

#a = 'Bruno'
#controlUsuario.excluir_usuario(a)



def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_opcoes():
    print("Escolha uma opção:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")

def escolha():
    while True:
        limpar_console()
        listar_opcoes()
        escolha = input("Digite o número da opção desejada (ou 's' para sair): ")

        if escolha.lower() == 's':
            break

        try:
            escolha = int(escolha)
            if escolha in [1, 2, 3]:
                limpar_console()
                print(f"Você escolheu a opção {escolha}.")
                input("Pressione Enter para continuar...")
            else:
                print("Opção inválida. Digite um número válido (1, 2 ou 3).")
        except ValueError:
            print("Entrada inválida. Digite um número válido (1, 2 ou 3).")

if __name__ == "__main__":
    escolha()