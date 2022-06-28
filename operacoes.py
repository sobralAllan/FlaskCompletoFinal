import conexaoBD
import mysql.connector
import this
this.msg = ""
db_connection = conexaoBD.conexao()
con = db_connection.cursor()

def inserir(nome, telefone, dataNascimento):
    try:
        sql = "Insert into pessoa(codigo, nome, telefone, dataDeNascimento) values('','{}','{}','{}')".format(nome, telefone, dataNascimento)
        con.execute(sql)
        db_connection.commit()
        return "{} Inserido!".format(con.rowcount)
    except Exception as erro:
        return erro

def consultar(codigo):
    try:
        sql = "Select * from pessoa where codigo = '{}'".format(codigo)
        con.execute(sql)

        for(codigo, nome, telefone, dataDeNascimento) in con:
            this.msg = "Código: '{}', Nome: '{}', Telefone: '{}', Data de Nascimento: '{}'".format(codigo, nome, telefone, dataDeNascimento)
        return this.msg

    except Exception as erro:
        return erro

def atualizar(codigo, campo, novoDado):
    try:
        sql = "Update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

def excluir(codigo):
    try:
        sql = "delete from pessoa where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        return "{} Excluído!".format(con.rowcount)
    except Exception as erro:
        return erro