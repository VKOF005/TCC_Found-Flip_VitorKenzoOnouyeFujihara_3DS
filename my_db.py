from kivy.lang import Builder
from kivymd.app import MDApp

import mysql.connector



class MyDb(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"



        mydb = mysql.connector.connect(         # O mydb pode ser substituido por outros nomes, mas lembre-se de renomear todas
                                                # as instancias para o mesmo nome.
                                                # Lembrar de criar uma classe para habilitar seu uso global em outras partes
                                                # do codigo.
            host="localhost",
            user="root",
            password="",
            database="found_flip"
        )



        c = mydb.cursor()
        # ---------------------------------
        # aqui vai os commandos em sql para a criação do banco


        c.execute("CREATE DATABASE IF NOT EXISTS found_flip") # use # para comentar após criar o banco.

        c.execute("USE found_flip")

        c.execute("") # aqui vem o resto do codigo sql.

        c.execute("")

    #abre e fecha a conexao
        mydb.commit()

        mydb.close()


        return Builder.load_file("") # carrega para o arquivo kv que vai estar dentro das aspas

        # ---------------------------------

    def submit(self):



        mydb = mysql.connector.connect( # apagar essa parte após criar a classe

            host="localhost",
            user="root",
            password="",
            database="found_flip"
        )

        c = mydb.cursor()

        sql_command = "INSERT INTO minhaTabela (coluna) VALUES (%s)" # n vi o nome das tabelas que vou usar .
        values = (self.root.ids.word_input.text,)

        c.execute(sql_command, values)

        mydb.commit()

        mydb.close()


    def show_records(self):

        # aqui vai vir os commandos de fetch (requisição de dados do banco).

        mydb = mysql.connector.connect( # apagar essa parte após criar a classe

            host="localhost",
            user="root",
            password="",
            database="found_flip"
        )

        c = mydb.cursor()

        c.execute("SELECT * FROM minhaTabela")
        records = c.fetchall()

#--------------------------------

        # aqui é para colocar commandos mais especificos
        # ex: um loop para mostrar dados em uma tabela

#--------------------------------
        mydb.commit()
        mydb.close()
