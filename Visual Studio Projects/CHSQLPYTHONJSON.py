'''
NOTE IF mysql.connector error shows up, it is because you havn't install
mysql.connector. RUN CMD there write pip install mysql.connector
'''

#importing module to connect mysql with python as mysql for ease
import mysql.connector as mysql

#connecting to the database using 'connect()' method
#it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
host = "localhost", #please check your host name
user = "root", #please check your user name
passwd = "001990", #use your password
database = "world_x", #Read the paragraph given below
)


print(db) #print the details of the connection

#creating an instance of 'cursor' class which is used to execute queries
cursor = db.cursor()

"""These QUERIES ARE SAME LIKE THE SQL"""

'''
#executing the query using 'execute()' method
cursor.execute("SHOW DATABASES")

#'fetchall()' method fetches all the rows from the last executed statement in list
databases = cursor.fetchall()

#printing the list of databases
print(databases)

AFTER READING THIS
ADD DATABASE IN THE CONNECTION PARANETHESIS database = "world_x" 
'''

#query to get all the tables from world_x database
cursor.execute("SHOW TABLES")

tables = cursor.fetchall() #returns list of tables present in the database

print(tables) #query to get all the tables from world_x database


"""Uncomment this code block if the query is executed in mysql"""

'''Incase the question queries are not executed in mysql'''

cursor.execute("ALTER TABLE world_x.city DROP COLUMN Population")
cursor.execute("ALTER TABLE world_x.city ADD COLUMN Population DOUBLE NULL DEFAULT NULL AFTER Info")


"""BLOCK END"""

#Query to extract the population before increament
cursor.execute("SELECT info->'$.Population' from city")

#printing the population info from the city table before increment
population_records_json = cursor.fetchall()
for r in population_records_json:
    print(r)

#adding the population values of json file into the population column
for i in range (0,len(population_records_json)):
    sql_update_query = "UPDATE world_x.city SET Population = %s WHERE ID = " + str(i+1)
    cursor.execute(sql_update_query, population_records_json[i])
    
#Query to update the population by 10%
cursor.execute("UPDATE world_x.city SET Population = Population + (Population * 0.1)")

#Query to extract the population before increament
cursor.execute("SELECT Population from city")
population_10_increment = cursor.fetchall()
#printing the population info from the city table after increment
for r in population_10_increment:
    print(r)

db.commit()
