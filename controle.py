from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cifras"
)  


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ''
    
    if formulario.radioButton.isChecked():        
        categoria ='Rock'

    elif formulario.radioButton_2.isChecked():       
        categoria ='MPB'

    elif formulario.radioButton_3.isChecked():        
        categoria ='Pagode'

    elif formulario.radioButton_4.isChecked():       
        categoria ='Reggae'
    
    elif formulario.radioButton_5.isChecked():        
        categoria ='Pop'

    elif formulario.radioButton_6.isChecked():        
        categoria ='Blues'

    elif formulario.radioButton_7.isChecked():      
        categoria ='Forro'

    elif formulario.radioButton_8.isChecked():       
        categoria ='Internacional'

    elif formulario.radioButton_9.isChecked():       
        categoria ='Axe'

    elif formulario.radioButton_10.isChecked():  
        categoria ='Samba'

    elif formulario.radioButton_11.isChecked():        
        categoria ='PopRock'

    elif formulario.radioButton_12.isChecked():    
        categoria ='Flashback'

    else:
        print('Nenhuma categoria foi selecionada')
        categoria ='sem categoria'
    
    print('Cifra adicionada!')
    print('Nome', linha1)
    print('Artista:', linha2)
    print('Tom:', linha3)
    print('Estilo:',categoria)

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO cifras (nome,artista,tom,estilo) VALUES (%s,%s,%s,%s)'
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()  

app=QtWidgets.QApplication([])
formulario=uic.loadUi("cifra.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
