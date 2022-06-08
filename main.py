# Press the green button in the gutter to run the script.
from flask import Flask, render_template, request
import this
import operacoes

this.nome = ""
this.telefone = ""
this.nascimento = ""
this.dados = ""

calculadora = Flask(__name__)

@calculadora.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.nascimento = request.form['tNovaDataDeNascimento']
        this.dados = operacoes.inserir(this.nome, this.telefone, this.nascimento)
    return render_template('index.html', titulo='Página Principal', resultado=this.dados)

if __name__ == '__main__':
    calculadora.run(debug=True, port=5000)
