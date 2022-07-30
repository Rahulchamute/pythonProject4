y import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="routerpasswords@123",
    database="python_video"
)
mycursor=mydb.cursor()

mycursor.execute('select * from emp_data')

emp_data=mycursor.fetchall()

# for user in emp_data:
#     print(user)

df=pd.read_excel("emp_data.xlsx")