import pymysql


mydb = pymysql.connect(
    host="",
    user="",
    passwd="",
    database=""
)

mycursor= mydb.cursor()

mycursor.execute("Create table avoyatravel(id INT AUTO_INCREMENT PRIMARY KEY, title varchar(255), price varchar (255), company varchar (255), itinerary varchar (255), takenTime DATETIME)")

mydb.commit()