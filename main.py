# Press the green button in the gutter to run the script.
from flask import Flask, render_template, request
import this
import operacoes
this.codigo = 0
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

@calculadora.route('/atualizar.html', methods=['GET','POST'])
def atualizar():
    if request.method == 'POST':
       this.codigo = request.form.get("tCodigo")
       this.nome   = request.form.get("tNovoNome")
       this.telefone = request.form.get("tNovoTelefone")
       this.nascimento = request.form.get("tNovaDataDeNascimento")
       #Métodos para atualização dos dados
       this.dados  = operacoes.atualizar(this.codigo, 'nome', this.nome)
       this.dados  = operacoes.atualizar(this.codigo, 'telefone', this.telefone)
       this.dados  = operacoes.atualizar(this.codigo, 'DataDeNascimento', this.nascimento)
    return render_template('atualizar.html', titulo='Atualizar Dados', resultado=this.dados)

@calculadora.route('/excluir.html', methods=['GET','POST'])
def excluir():
    if request.method == 'POST':
        this.codigo = request.form.get("tCodigo")
        this.dados = operacoes.excluir(this.codigo)
    return render_template('excluir.html', titulo='Excluir Dados', resultado=this.dados)

@calculadora.route('/consultar.html', methods=['GET', 'POST'])
def consultarCodigo():
    if request.method == 'POST':
        this.codigo = request.form.get("tCodigo")
        this.dados = operacoes.consultar(this.codigo)
    return render_template('consultar.html', titulo='Consultar', resultado = this.dados)

if __name__ == '__main__':
    calculadora.run(debug=True, port=5000)
