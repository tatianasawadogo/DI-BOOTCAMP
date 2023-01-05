# Installation de du module
#pip install psycopg2
#Import du module
import psycopg2

#Variable de connection à la base de donnée
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '11tati173'
DATABASE = 'ibam'

#Connection au serveur

try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD)
    print("conection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")


 #Validation des transaction

connection.autocommit = True
cursor = connection.cursor()

#Creation de la BD
cursor.execute('DROP DATABASE IF EXISTS {};'.format('ibam'))
cursor.execute("CREATE DATABASE ibam;")

#Coneection à la BD
try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    print("conection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")

#Creation de la table student

cursor.execute("CREATE TABLE if not EXISTS student (name VARCHAR(255), firstname VARCHAR(255), phone VARCHAR(255), address VARCHAR(255));")

#Insertion des données

values = [
      ('Peter', 'Grid', '77445511','Lowstreet 4'),
    ('All', 'Grid', '77445511','Lowstreet 4'),
    ('Vall', 'Grid', '77445511','Lowstreet 4'),
    ('Til', 'Grid', '77445511','Lowstreet 4'),
    ('TO', 'Grid', '77445511','Lowstreet 4'),
    ('KA', 'Grid', '77445511','Lowstreet 4'),
    ('DK', 'Grid', '77445511','Lowstreet 4'),
    ('SQAZ', 'Grid', '77445511','Lowstreet 4'),
    ('NAD', 'Grid', '77445511','Lowstreet 4'),
    ('AGe', 'Grid', '77445511','Lowstreet 4')
]
cursor.executemany("INSERT INTO student VALUES(%s,%s,%s,%s)", values)
connection.commit()
print(cursor.rowcount, "line was inserted.")


#Lecture ds données

sql1 = "SELECT * FROM student;"
cursor.execute(sql1)
#cursor.fetchall()
for data in cursor.fetchall():
    print(data)
