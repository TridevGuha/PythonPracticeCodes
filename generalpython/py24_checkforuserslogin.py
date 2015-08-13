#!/usr/bin/env python3
import pwd
try:
    pwd.getpwnam(user1)
except KeyError:
    print('User someusr does not exist.')