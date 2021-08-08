import os
import subprocess

# def quotemaker():
#     return "This is a funny joke"
#
#
# file = open("/tmp/example.txt", "w")
# file.write("This is funny")
# print(file.read("/tmp/example.txt"))
# file.close()

sender = "This is a test of the program"


lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write(b"Printing from Python!")