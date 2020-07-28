#Go home alarm
#Version 1.1
#Date: 29/05/20
#Author: Wee


#Get necessary modules
import webbrowser, time
from termcolor import colored


####### Initial Resources #######

#Catch wrong input error, input must be the whole hour in 24 time
#Lazy I know, but _day solves next day issue, will ammend in later versions

print("Go home alarm \nAuthor: Wee \nVersion: 1.1 \nLast updated: 29/05/20 \n\n\nRead prompts carefully and be sure to have your sound on\n\n\n")

while True:
    t = time.localtime()
    current_time = time.strftime("%H", t)   #get current time in hours
    _time = input("What time would you like to leave? \nPlease write in whole hours in 24 hour time only (e.g 5pm = 17) \n")
    _day = input("Is this time the same day? (Before midnight tonight? (y/n) ")
    try:
        _time = int(_time)
        if _day == "y":
            if _time < int(current_time):            #catch and print error message if user inputs a bad time, 5 for 5pm = NO
                print("Please check your input, \ntime must be written in 24 hour time with whole hours (e.g. 5pm = 17 ")
                continue
            else:
                _countdown = (int(current_time) - _time)^-2
                break
        else:
            _countdown = (24 - int(current_time)) + _time
            print(_countdown)
            break
       
    except:     #catch 
        print("Please input time as the whole hour written in 24 hour clock (e.g. 5pm = 17 ")
        continue


####### Start Main Script #######

#loop function, if local time is equal to requested alarm time, open "go home" video
while True:
    t = time.localtime()
    current_time = time.strftime("%H", t)
    if int(current_time) == _time:
        print("Time to go home \nIt is "+str(_time))
        #open 2 (two) tabs with "go home", not essential, but slightly more annoying = slightly more effective
        for x in range(2):                 
            webbrowser.open('https://www.youtube.com/watch?v=d8pvD_4Pd1A',1)
        #asks if user agrees to leave before ending program
        #if the user disagrees, script restarts
        _listen = input("have you left yet? (y/n)")
        if _listen == "y":
            break
        else:
            continue
    else:
        print("Not Yet, " + str(_countdown), "hour(s) left")
        time.sleep(60)
        continue

####### END #######