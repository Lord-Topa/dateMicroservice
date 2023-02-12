import time
from datetime import datetime

#change this variable if you plan to have the txt doc in a different location
PATH = "dateMicroservice.txt"

def writeToFile(msg):
    fileWrite = open(PATH, "w")
    fileWrite.write(msg)
    fileWrite.close()

def main():
    fileRead =  open(PATH, "r")
    dt = datetime.now()
    week = ["monday", "tuesday", "wendsday", "thursday", "friday", "saturday", "sunday"]
    print("\nDate Microservice    \n    By: Taijen Ave-Lallemant    \n")

    textInFile = ""
    previousOutput = ""
    while True:
        time.sleep(1.0)
        fileRead.seek(0,0)
        textInFile = fileRead.readline()

        if textInFile == "get date":
            date = dt.date()
            writeToFile(str(date))
            previousOutput =  str(date)
        elif textInFile == "get day":
            day = dt.weekday()
            writeToFile(week[day])
            previousOutput = week[day]
        elif textInFile == "get full date":
            date = dt.date()
            day = dt.weekday()
            message = str(date) + "," + week[day]
            writeToFile(message)
            previousOutput = message
        elif textInFile == "exit":
            print("EXITING")
            writeToFile("")
            break
        elif textInFile != previousOutput:
            writeToFile("ERROR INVALID INPUT")
            previousOutput = "ERROR INVALID INPUT"

main()       

