#!/usr/bin/env python3
fobj = open('/proc/meminfo')
for i in fobj.readlines():
    if 'MemTotal' in i:
        j = i.split()
        print("MemTotal: %d MB" %(int(j[1])/1024))
    if 'MemFree' in i:
        j = i.split()
        print("MemFree : %d MB" %(int(j[1])/1024))
    if 'MemAvailable' in i:
        j = i.split()
        print("MemAvailable: %d MB" %(int(j[1])/1024))