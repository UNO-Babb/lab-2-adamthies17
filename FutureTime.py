#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 12
  currentMinute = now.minute 

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter hours: ")
  hours = int(hours)
  #Ask user for minutes
  minutes = input("Enter minutes: ")
  minutes =  int(minutes)
  #Calculate the time after the user-supplied time has passed.
 
  futureMinutes = currentMinute + minutes
  extraHours = futureMinutes // 60
  futureMin = futureMinutes % 60
  futureHours = (currentHour + hours + extraHours) % 12
  
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  strHour = str(futureHours)
  strMinute = str(futureMin)
  if futureMin < 10:
    strMinute = "0" + strMinute

  print(strHour + ":" + strMinute)
if __name__ == '__main__':
  main()