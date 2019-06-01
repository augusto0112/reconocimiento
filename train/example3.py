import pymysql

############### CONFIGURAR ESTO ###################
# Open database connection
db = pymysql.connect("localhost","root","Augusto0112","pythontest")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO test(id, name, email) \
   VALUES (NULL,'{0}','{1}')".format("cosme","testmail@sever.com")
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


# desconectar del servidor
db.close()
