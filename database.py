###    database create and table create

import mysql.connector as mc
conn=mc.connect(host ='localhost' , user = 'root' , password = 'Aayush2211', database = "Customer_satisfaction")

if(conn.is_connected()):
    print('connection established')
else:
    print('unable to connect')


# import sqlite3
# conn = sqlite3.connect('bikedata.db)


query_to_create_table = """
CREATE TABLE Cust_details (
        age int,
        flight_distance int ,
        inflight_entertainment int,
        baggage_handling int ,
        cleanliness int ,
        departure_delay int ,
        arrival_delay int ,
        gender varchar(50),
        customer_type varchar(100),
        travel_type varchar(100),
        economy varchar(100),
        economy_plus varchar(100),
        PREDICTION  varchar(100)
        );
"""

cur = conn.cursor()
cur.execute(query_to_create_table)
print("database created")
cur.close()
conn.close()