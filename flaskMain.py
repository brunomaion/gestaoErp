from flask import Flask, render_template, request, flash, redirect
import json
import os
import model
import controlUsuario
import controlTarefa
import os
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY']= "PALAVRA-SECRETA"
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('nome')
        senha = request.form.get('senha')

        # Verificar se o usuário existe no DataFrame e a senha está correta
        user_obj = controlUsuario.procurar_usuario('nomeUser', usuario)
        if user_obj and user_obj.senha == senha:
            return render_template("homepage.html", nomeUsuario=usuario)
        else:
            flash('Usuário ou senha inválidos.')
            return redirect("/")
    else:
        return render_template("login.html")




@app.route('/adicionarUsuario', methods=['POST'])
def enviar_formulario():
    nome = request.form['nome']
    senha = request.form['senha']
    email = request.form['email']

    idUser = 2
    usuario1 = model.Usuario(idUser, nome, senha, email)


    controlUsuario.adicionarTabela(usuario1)

    # Aqui você pode realizar as ações necessárias com os dados do formulário
    # Neste exemplo, apenas retornamos uma mensagem na página com os dados enviados
    return render_template("homepage.html")

@app.route('/logout', methods=['GET'])
def logout():
    # Limpar a sessão para fazer o logout
    return render_template("login.html")

@app.route("/addusuario", methods=['GET'])
def pagina1():
    return render_template("usuario.html")

@app.route("/homepage", methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html")

@app.route("/addtarefa", methods=['GET'])
def pagina2():
    return render_template("tarefa.html")

@app.route('/enviarTarefa', methods=['POST'])
def addTarefa():
    idTarefa = request.form['idTarefa']
    nomeTarefa = request.form['nomeTarefa']
    data = request.form['dataFinal']
    mensagem = request.form['descricao']

    tarefa = model.Tarefa(idTarefa, nomeTarefa, data, mensagem)
    controlTarefa.adicionarTabela(tarefa)

    return render_template("homepage.html")


@app.route('/excUsuario', methods=['GET', 'POST'])
def paginaExcluirUsuario():
    usuarios = controlUsuario.consultar_dataframe()
    df = pd.DataFrame([vars(usuario) for usuario in usuarios])
    objetos = df.to_dict(orient='records')
    return render_template("excluirUsuario.html", objetos=objetos)

@app.route("/botaoexcluirUsuario", methods=['GET', 'POST'])
def botaoExcluirUsuario():
    nome_usuario_excluido = request.form.get('nomeUsuarioExcluido')
    print("Nome do usuário a ser excluído:", nome_usuario_excluido)
    controlUsuario.excluir_usuario(nome_usuario_excluido)
    return render_template("homepage.html")



if __name__ in '__main__':
    app.run(debug=True)