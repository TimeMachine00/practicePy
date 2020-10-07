import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="ghij",passwd="ghij1234", database="ghij")

mycursor=mydb.cursor()
mycursor.execute("select * from stu")
result =mycursor.fetchone()
for i in result:
    print(i)