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

sender = "lp -d OKI_DATA_CORP_ML420 /tmp/temp.txt"


lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write(sender)
