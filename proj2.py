sql='SELECT COUNT (DISTINCT State) FROM towed_vehicles'
c.execute(sql).fetchall()
print(c.execute(sql).fetchall())

#Writing the SQL Command




import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy.polynomial.polynomial as poly

from scipy.interpolate import *
from numpy import *
from matplotlib.pyplot import *

#importing all the elements necessary to conduct the project



f=open('RedLight.csv')
csv_f=csv.reader(f)
l=[]
AllMonths=[]
AllViolations=[]
#opening the file and defining the two lists

for row in csv_f:
if row[3] == 'VIOLATION DATE':
continue
datex=row[3].split('/')
#Splitting the date from the rest of the elements
month=datex[0]
#Defining the month, getting rid of the date and year
violations=row[4]
#Telling the program what element violations are under
AllMonths.append(int(month))
AllViolations.append(int(violations))
#Putting both characterisitcs into lists

x=np.array(AllMonths)
y=np.array(AllViolations)
#Creating arrays for both elements

coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
ys = polynomial(x)
print (coefficients)
print (polynomial)

#Creating the slope intercept equation plus printing the formula
fig, ax = plt.subplots()
fit = np.polyfit(x, y, deg=1)
ax.plot(x, fit[0] * x + fit[1], color='red')
ax.scatter(x, y)

plt.show()
#Graphing the data

f.close

