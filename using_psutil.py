#! /usr/bin/env python3

#In this program, I will demonstrate some of the cool applications
#of using the psutil module!

import psutil
import socket #To check connectivity and dns

def system_check():

    disk_space = psutil.disk_usage('/').percent
    print('You have used {}% of your hard drive'.format(disk_space))
    #setting an alert if you have less than 20%
    if disk_space > 80:
        print("Your disk is over 80% full!")


    threshold = 100 * 1024 * 1024 #100MB
    mem = psutil.virtual_memory()
    print("You have {} of virtual memory available, which is {}%".format(mem.available, mem.percent))
    #setting an alert if you have less than the threshold
    if mem.available < threshold:
        print("You have less than 100MB of virtual memory left!")

    #Checking out core temps
    temp = psutil.sensors_temperatures()
    print(temp)

    #Checking current cpu usage, over a 1 second interval
    p = psutil.cpu_percent(interval=1)
    print("Current CPU usage: {}".format(p))
    #raise alert if over 80%
    if p > 80:
        print("Your cpu usage is over 80%")

if __name__ == '__main__':
    system_check()
