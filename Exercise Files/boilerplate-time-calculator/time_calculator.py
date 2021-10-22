#!/usr/bin/env python3
#created by Regina Citra Pesela (reginapasela@gmail.com)

def add_time(start, duration, currentDay = ""):
    #clean start time data into variables
    startHour, startMinute, startAMPM = int(start.split(":")[0]), int(start.split(":")[1][:2]), start.split(" ")[1]

    #clean duration time data into variables
    addHour, addMinute = int(duration.split(":")[0]), int(duration.split(":")[1][:2])

    if startAMPM == "AM":
        dictAMPM = {0: startAMPM, 1: "PM"}
    else:
        dictAMPM = {0: startAMPM, 1: "AM"}

    tupDays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    
    if currentDay != "":
        currentDay = currentDay.title()
        dayIndex = (tupDays.index(currentDay))
    else:
        dayIndex = ""

    #calculate the time
    #calculate start minute plus duration minute
    resultMinute = startMinute + addMinute

    #if result minute bigger than 60 we should divide it and then add to result hour
    moreHour = 0
    if resultMinute > 60:
        moreHour = round(resultMinute/60)
        resultMinute = resultMinute % 60

    #fix minute < 10 to be 2 digits (02-09)
    if resultMinute < 10:
        resultMinute = "0" + str(resultMinute)

    #calculate start hour plus duration hour
    resultHour = startHour + addHour + moreHour

    #if result hour is bigger than 24 we should divide it and then add to result day
    if resultHour > 24:
        moreDay = round(resultHour / 24)
    elif startAMPM == "PM" and resultHour > 12:
        moreDay = 1
    else:
        moreDay = 0

    #determine AM or PM
    countAMPM = 0
    while resultHour >= 12:
        resultHour -= 12
        countAMPM += 1

    if countAMPM > 1:
        countAMPM = countAMPM % 2

    #IF function to check how many days passed, if there is > 0 put some text
    if moreDay == 0:
        resultDay = ""
    elif moreDay == 1:
        resultDay = " (next day)"
    else:
        resultDay = " (" + str(moreDay) + " days later)"

    if dayIndex != "":
        dayIndex += (moreDay % 7)
        dayIndex = dayIndex % 7

    print(dayIndex, moreDay)


    #change 24 hour format to AMPM format   
    if resultHour > 12:
        resultHour = resultHour % 12
    elif resultHour == 0:
        resultHour = 12

    #return the result into new_time variable
    if dayIndex == "":
        new_time = str(resultHour) + ":" + str(resultMinute) + " " + str(dictAMPM[countAMPM]) + str(resultDay)
    else:
        new_time = str(resultHour) + ":" + str(resultMinute) + " " + str(dictAMPM[countAMPM]) + ", " + str(tupDays[int(dayIndex)]) + str(resultDay)  
    
    return new_time