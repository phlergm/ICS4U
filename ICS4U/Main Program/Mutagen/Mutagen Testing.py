#----------------------------------------------------------------
# Name: Humza Anwar
# Purpose: to find out how on earth mutagen works
#
# Refererences: 
#
# Author: Humza Anwar
# Created: 07/11/18
# Updated: 07/11/18
#-----------------------------------------------------------------------------
import mutagen, os
mp3 = open("mp3.txt", "w")
mp3.write(str(mutagen.File("Eden-drugs.mp3")))
'''
for root, dirs, files in os.walk("/home/humza/Music/DCIM"):
    for file in files:
        if file.endswith(".mp3"):
            mp3.write("\n")
            mp3.write(str(mutagen.File(file)))
'''

mp3.close