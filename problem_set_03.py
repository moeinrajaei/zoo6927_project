#!/usr/bin/env python3


# I wrote them using Spyder(Python3.7). For runing them, copy and paste them in Spyder.

#Problem 1 (4 pts):

import csv
highest=open("C:/Users/moeinraja/Desktop/CO-OPS__8729108__wl.csv")
Water_Level=0.0
Date_Time=0.0
maxt=0.0
Water_Level_list=[]
Date_Time_list=[]
for line in highest:
  delimiter=','
  lines=(line.strip().split(delimiter))
  try:
        Water_Level=float(lines[1])
        Water_Level_list.append(Water_Level)
  except:
        pass
  Date_Time=lines[0]
  Date_Time_list.append(Date_Time)
maxt=max(Water_Level_list)
maxi=Water_Level_list.index(maxt)
maxf=Date_Time_list[maxi]
print("The highest water level is", maxi, "at", maxf)


#Problem 2 (4 pts):

import pandas as pd
df=pd.read_csv("C:/Users/moeinraja/Desktop/CO-OPS__8729108__wl.csv")
highest=df[" Water Level"].idxmax()
print(df.loc[highest, "Date Time" : " Water Level"])


#Problem 3 (4 pts):

import pandas as pd
df=pd.read_csv("C:/Users/moeinraja/Desktop/CO-OPS__8729108__wl.csv")
df['difference'] = df[" Water Level"].diff()
highest=df['difference'].idxmax()
print(df.iloc[highest,[0, 1, 8]])


#Problem 4: Grad students only (4 pts):

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:/Users/moeinraja/Desktop/CO-OPS__8729108__wl.csv")
x, y=df['Date Time'], df[' Water Level']
fig=plt.figure()
plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Water Level")
plt.legend()
plt.show()


#
# End of script
