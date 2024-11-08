from conexao import *


db = ConexaoDatabase(host="localhost", database="supermarket", user="root", password="#itus_00")

class CadastrarProduto:
    db.connect()
    db.disconnect()
class ScannearProduto:
    pass

class EmitirNotaFiscal:
    pass

class ControleEstoque:
    pass
