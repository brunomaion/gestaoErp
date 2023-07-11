import model
import controlUsuario







idUser = input("Digite o ID do usuário: ")
nome = input("Digite o nome do usuário: ")
cpf = input("Digite o cpf do usuário: ")
email = input("Digite o email do usuário: ")


usuario1 = model.Usuario(idUser, nome, cpf, email)

controlUsuario.adicionarTabela(usuario1)

##controlUsuario.printDf()

controlUsuario.printDf()