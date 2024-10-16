from PyQt5 import uic , QtWidgets 
import mysql.connector
conexao = mysql.connector.connect (
host = '127.0.0.1',
user ='dev',
password = '102030',
database = 'cadastro_produtos'
)
numero_id=0
def excluir ():
    remover = lista.tableWidget.currentRow()
    lista.tableWidget.removeRow(remover)
    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM produtos')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [remover] [0]
    cursor.execute('DELETE FROM produtos WHERE id ='+str(valor_id))
    lista.close()
    formulario.show()
    conexao.commit()

def editar () :
    global numero_id
    dados = lista.tableWidget.currentRow()
    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM produtos')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [dados][0]
    cursor.execute('SELECT * FROM produtos WHERE id = '+str(valor_id))
    leitura_banco = cursor.fetchall()
  
    editar.show()
    numero_id = valor_id
    editar.txtAlterarId.setText(str(leitura_banco[0][0]))
    editar.txtAlterarProduto.setText(str(leitura_banco[0][1]))
    editar.txtAlterarPreco.setText(str(leitura_banco[0][2]))
    editar.txtAlterarQtd.setText(str(leitura_banco[0][3]))

def salvar_dados ():
    global numero_id

    id = editar.txtAlterarId.text()
    produto = editar.txtAlterarProduto.text()
    preco = editar.txtAlterarPreco.text()
    estoque = editar.txtAlterarQtd.text()

    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET id='{}', produto='{}', preco='{}', estoque='{}' WHERE id={}".format(id,produto,preco,estoque,numero_id))

    editar.close()
    lista.close()
    formulario.show()

    conexao.commit()

def lista ():
    lista.show()
    cursor = conexao.cursor()
    comando_mysql='SELECT*FROM produtos'
    cursor.execute (comando_mysql)
    leitura_banco = cursor.fetchall()

    lista.tableWidget.setRowCount(len(leitura_banco))
    lista.tableWidget.setColumnCount(4)
    for i in range (0,len(leitura_banco)):
        for j in range(0,4):
            lista.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))
  
def inserir () :
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text() 
    estoque=  formulario.txtEstoque.text()
  
    cursor = conexao.cursor()
    comando_mysql='INSERT INTO produtos (produto,preco,estoque) VALUES (%s,%s,%s)'
    dados = (str(produto),str(preco),str(estoque))
    cursor.execute(comando_mysql,dados)
    conexao.commit()

    formulario.txtProduto.setText('')
    formulario.txtPreco.setText('')
    formulario.txtEstoque.setText('')
    formulario.lblConfirmacao.setText('Sucesso !')

app =QtWidgets.QApplication ([])
formulario = uic.loadUi('formulario.ui')
formulario.btnCadastrar.clicked.connect(inserir)
formulario.btnRelatorio.clicked.connect(lista)
lista = uic.loadUi('lista.ui')
lista.btnAlterar.clicked.connect(editar)
lista.btnApagar.clicked.connect(excluir)
editar = uic.loadUi('editar.ui')
editar.btnConfirmar.clicked.connect(salvar_dados)

formulario.show()

app.exec()

