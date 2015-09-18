from datetime import datetime


Time1 = "10:00 PM"
Dur1 = 90

Time2 = "11:29 PM"
Dur2 = 90

def checkTimingClash(Time1 , Time2):
    print Time1.strip()
    print Time2.strip()
    x1 = Time1.split(" ")
    x2 = x1[0].split(":")
    
    y1 = Time2.split(" ")
    y2 = y1[0].split(":")
    
    
    if x1[1]=="AM" and int(x2[0]) == 12:
        hr1 = 0
    elif x1[1]=="PM" and int(x2[0]) <= 12:
        hr1 = (12 + int(x2[0]))*60
    else:
        hr1 = int(x2[0])*60
    min1 = int(x2[1])
    TotalMinStart1 = hr1 + min1
    TotalMinEnd1 = TotalMinStart1 + Dur1
    
    if y1[1]=="AM" and int(y2[0]) == 12:
        hr2 = 0
    elif y1[1]=="PM" and int(y2[0]) <= 12:
        hr2 = (12 + int(y2[0]))*60
    else:
        hr2 = int(y2[0])*60
    min2 = int(y2[1])
    TotalMinStart2 = hr2 + min2
    TotalMinEnd2 = TotalMinStart2 + Dur2
    
    if TotalMinStart2 > TotalMinEnd1 and TotalMinStart2 < TotalMinStart1:
        print "There is clash -1"
    if TotalMinEnd1 > TotalMinStart2 and TotalMinEnd1 < TotalMinEnd2:
        print "There is clash -2"
    
 

def main():
    checkTimingClash(Time1, Time2)
    


main()