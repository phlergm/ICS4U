#----------------------------------------------------------------------
# Name: Humza Anwar
# Purpose: To sort music files by filetype & bitrate, then giving 
#           a list of files of each filetype
#
# Refererences: http://www.tutorialspoint.com/python/os_walk.htm
#
# Max code length: 80
# Max comment length: 72
#
# Author: Humza Anwar
# Created: 24/09/18
# Updated: 09/01/19
#----------------------------------------------------------------------
import os
import Classes

path = Classes.Target_Path.get_path()
print(path)
current_target_path = Classes.Target_Path(path)


option = input("n for new list or m for merge")
if (option == "n \n"): 
	Classes.Song_List.make_new_list(path)
elif (option == "m \n"):
	Classes.Song_List.merge_list(path)
	