import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="smartroad"
# )


def insertAccelerometer(idAlat, x, y, z):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smartroad"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO accelerometer (idAlat, x, y, z) VALUES (%s, %s, %s, %s)"
    val = (idAlat, x, y, z)
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()

# def getConfig(name):
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smartroad"
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM config WHERE name="%s"' % 'accelerometer_record')

myresult = mycursor.fetchall()

print(myresult[0][1])