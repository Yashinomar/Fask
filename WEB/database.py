import mysql.connector
def get_data():
    
    mydb = mysql.connector.connect(user='root',password='root',database='')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM employee')
    result = mycursor.fetchmany()
    mycursor.close()
    mydb.close()
    return result
