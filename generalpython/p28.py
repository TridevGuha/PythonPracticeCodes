#!/usr/bin/env python3
fobj = open('/etc/passwd')
f = fobj.read()
f = f.split('\n')
for x in f:
   if not x.endswith('nologin'):
       print(x)
fobj.close()
