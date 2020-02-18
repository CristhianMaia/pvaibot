import mysql.connector
import auth
from colorama import Fore, Back
from colorama import Style

mydb = auth.db()
mycursor = mydb.cursor()

def corrigir ():

  print(".")
  # mycursor.execute("ALTER TABLE evento AUTO_INCREMENT = 1")
  # myresult = mycursor.fetchall()
  # print(myresult)
  # mydb.commit()
  # mycursor.execute("SHOW COLUMNS FROM pessoa_evento")

  # for x in mycursor:
  #   print(x) 
  


##EVENTOS
def get_eventos():
  sql = "SELECT * FROM evento ORDER BY data"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  return myresult

def create_evento(list):
  val = list
  sql = "INSERT INTO evento (nome, data, tweet_id) VALUES (%s, %s, %s)"
  mycursor.executemany(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

def update_tweet_evento(tt_id, id):
  val = id
  mycursor.execute("UPDATE evento SET tweet_id = {} WHERE id_evento = {}".format(tt_id, id))
  mydb.commit()


def destroy_evento(id):
  mycursor.execute("DELETE FROM pessoa_evento WHERE evento_id = {}".format(id))
  mycursor.execute("DELETE FROM evento WHERE id_evento = {}".format(id))
  mydb.commit()
  

##PESSOAS
def get_pessoas():
  sql = "SELECT * FROM pessoa"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  return myresult

def create_pessoa(list):
  # val = []
  # for i in list:
  #   val.append(tuple([i[1]]))
  for val in list:
    try:
      sql = "INSERT INTO pessoa(id_pessoa) VALUES ({})".format(val[1])
      mycursor.execute(sql)
      print(Fore.GREEN + "Pessoa cadastrada: {}".format(val[1]) + Style.RESET_ALL)  
      # mycursor.executemany(sql, val)
    except mysql.connector.Error as error:
      print("Pessoa: {}".format(error))
  mydb.commit()
  print(Back.GREEN + "Pessoas cadastradas" + Style.RESET_ALL)
    


##PESSOAS EVENTO
def get_pessoa_evento():
  sql = "SELECT * FROM pessoa_evento"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  return myresult

def get_pessoa_evento_count():
  ##Fazer receber uma lista, consultar todos e retornar uma lista para trabalhar no codigo com ela
  sql = "SELECT (evento_id) FROM pessoa_evento"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  return myresult



def confirmar_pessoa(list):
  create_pessoa(list)
  # val = []
  # for i in list:
  #   val.append(tuple(i))
  for val in list:
    try:
      sql = "INSERT INTO pessoa_evento(evento_id, pessoa_id) VALUES (%s, %s)"
      mycursor.execute(sql, val)
      print(Fore.GREEN + "Pessoa Evento cadastrado: {}".format(val) + Style.RESET_ALL) 
    except mysql.connector.Error as error:
      print("Confirmar ERRO: {}".format(error))
  mydb.commit()
  print(Back.GREEN + "Confirmações cadastradas" + Style.RESET_ALL)

def destroy_confirmar_pessoa(id):
  mycursor.execute("DELETE FROM pessoa_evento WHERE pessoa_id = {}".format(id))
  mydb.commit()


# mycursor.execute("CREATE TABLE evento(id_evento INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL, tweet_id VARCHAR(255))")
# mycursor.execute("ALTER TABLE eventos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
# mycursor.execute("ALTER TABLE evento ADD COLUMN data DATE NOT NULL after nome") 

# mycursor.execute("SHOW COLUMNS FROM evento")

# for x in mycursor:
#   print(x) 




# sql = "INSERT INTO evento (nome, data, tweet_id) VALUES (%s, %s, %s)"
# val = ('DJ Guuga em Paranavai', '2020-04-18', "1215425704453722114")
# mycursor.execute(sql, val)

# val = [
#   ('DJ Guuga em Paranavai', '2020-04-18', "1215425704453722114"),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)



# print(mycursor.rowcount, "record inserted.")

# sql = "SELECT * FROM evento"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# mydb.commit()






# CREATE TABLE IF NOT EXISTS pessoa (
#   id_pessoa VARCHAR(255) PRIMARY KEY,
# )

# CREATE TABLE IF NOT EXISTS evento (
#   id_evento INT AUTO_INCREMENT PRIMARY KEY,
#   nome VARCHAR(255) NOT NULL, 
#   data DATE NOT NULL,
#   tweet_id VARCHAR(255)
# )

# CREATE TABLE IF NOT EXISTS pessoa_evento (
#   evento_id INT NOT NULL, 
#   pessoa_id VARCHAR(255) NOT NULL, 
#   CONSTRAINT id_pessoa_evento PRIMARY KEY (evento_id, pessoa_id), 
#   CONSTRAINT id_pessoa_evento2 FOREIGN KEY (evento_id) REFERENCES evento (id_evento),
#   CONSTRAINT id_pessoa_evento3 FOREIGN KEY (pessoa_id) REFERENCES pessoa (id_pessoa)
# )