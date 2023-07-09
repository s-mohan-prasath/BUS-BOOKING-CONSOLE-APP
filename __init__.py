from DB.connect import connectToDB
from CLASSES.auth import Auth

mydb = connectToDB();
mycursor = mydb.cursor();
auth = Auth(mydb,mycursor);