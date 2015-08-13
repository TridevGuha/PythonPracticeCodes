#!/usr/bin/env python3
fobj = open("/proc/meminfo")
s = fobj.read().split("\n")
i = 0
while i < 3:
   f = s[i].split(":")
   x = f[1].split()
   print(f[0],end=' ')
   print(" : ",end=' ')
   print(int(x[0])/1024,end=' ')
   print("Mb")
   i+=1