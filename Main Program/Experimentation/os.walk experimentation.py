#------------------------------------------------------------------------------
# Syntax setup of os.walk = os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
#
#
#
#------------------------------------------------------------------------------


import os 

for root, dirs, files in os.walk("/home/humza/Music/DCIM"):
    print ("\n")
    #print(root) #prints the file path being searched and every filepath within
    print(dirs) # prints a list of every folder and then a blank list?
    #print(files) #prints every file in the directory searched for, then every file in a folder

#print (os.walk("/home/humza/Music/DCIM/Testings"))

