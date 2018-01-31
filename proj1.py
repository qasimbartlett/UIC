import sqlite3
import csv
conn=sqlite3.connect('Towed_Vehicles.db')
c=conn.cursor()
air = ' CREATE TABLE towed_vehicles (Tow_Date, Make, Style, Color, State)'
try:
    c.execute(air)
except:
    pass

#Importing the proper elements needed to help create the table


#f=open('Towed_Vehicles.csv', 'r')
#f.readline()
#for line in f:
 #   line=line.strip().split(',')
    #values=(Tow_Date, Make, Style, Color, State)
  #  c.execute("INSERT INTO towed_vehicles VALUES(?, ?, ?, ?,?)",line)
#f.close()
#conn.commit()

#conn.close()
