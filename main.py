import time
import os
import crack as cr
print("Cracker V2")

time.sleep(5)

print("""
 █▀▀█  █▀▀█  █▀▀█  █▀▀█  █ ▄▀  █▀▀▀  █▀▀█ 
 █     █▄▄▀  █▄▄█  █     █▀▄   █▀▀▀  █▄▄▀ 
 █▄▄█  █  █  █  █  █▄▄█  █  █  █▄▄▄  █  █ """, end='\n')

print("""
1: PYCHARM
2: IDE
3: VS-CODE""")
code = int(input("Enter Your Choice: "))
cr.check_type(code)


