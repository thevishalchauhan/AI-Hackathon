[‎9/‎20/‎2018 7:02 PM]  Sinha, Vishal:  
import sqlite3  #import the required module.

conn = sqlite3.connect("*Database_Name.db*")  
   #create the var. 'conn' and connect to a database the correct name.  If the 
   database does not exist, then one will be created with that name.
c = conn.cursor() 
   #Create a var. c to hold the cursor, which is used to interact with the 
   database.
c.execute("*SQL Code Here*")
   #Use the cursor var. to interact with the database.  Replace the fake 
   code with an actual SQL query.
conn.commit()  
   #Calling commit to that database connection is kind of like saving the 
   changes that were made to the database.
conn.close()
   #Be sure to close the connection to the database. 
import pymssql

conn = pymssql.connect(server=server, user=user, password=password, database=db)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(MemberID) as count FROM Members WHERE id = 1")
row = cursor.fetchone()

conn.close()

print(row) 
 
