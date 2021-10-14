import sys
import os

if len(sys.argv) != 2:
    raise ValueError('Please provide required arguments.')
 
var1 = sys.argv[1]
osenv_s1 = os.environ.get("osenv_s1")

print("hello world.")
print("1-Arg passed value = ", var1 )
print("2-OS Env passed value = ", osenv_s1 )



if (var1== "goodnight"):
    print("3-var1 is  gnight")

if (osenv_s1== "goodnight"):
    print("4-osenv_s1 is gnight")
