with open('/etc/passwd') as f:
    for x in f:
        if '/bin/bash' in x:
            print(x.split(':')[0]) 
