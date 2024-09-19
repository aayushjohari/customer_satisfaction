import mysql.connector as mc
conn=mc.connect(host ='localhost' , user = 'root' , password = 'Aayush2211', database = "Customer_satisfaction")

cur = conn.cursor()
query ="select * from Cust_details"

cur.execute(query)
for record in cur.fetchall():
    print(record)

cur.close()
cur.close()