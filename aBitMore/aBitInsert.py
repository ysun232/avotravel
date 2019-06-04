#the working version of adding information into mysql database


import pymysql
from aBitMore.mySoupFinal import *

mydb = pymysql.connect(
    host="",
    user="",
    passwd="",
    database=""
)
mycursor = mydb.cursor()

sql1 = "Insert into avoyatravel(title, price, company, itinerary, takenTime) values (%s,%s,%s,%s,%s)"
val1 = newTuple
mycursor.executemany(sql1, val1)

mydb.commit()