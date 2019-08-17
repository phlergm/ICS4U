#-----------------------------------------------------------------------------
# Name: Humza Anwar
# Purpose: To sort music files by filetype & bitrate, then giving 
#				a list of files of each filetype
#
# Refererences: http://www.tutorialspoint.com/python/os_walk.htm
#
# Author: Humza Anwar
# Created: 24/09/18
# Updated: 27/11/18
#-----------------------------------------------------------------------------
import os, spotipy, mutagen

song_list_w = open("song_list.txt", "w")    
song_list_w.write("bad")
song_list_w.close()
#This will only be used to overwrite everything in the file so that the script 
#can be run multiple times

song_list_a = open("song_list.txt", "a")



class Filepath():
    '''
    a class to hold the filepaths that the user wants to use 
    
    Attributes
    ----------
    path : str
        The path to the directory
    
    exists : bool
        Defines whether or not the directory is real
    
    Methods
    -------
    get_path() -> str 
    is_real () -> bool
    '''
    
    def __init__(self, path, exists)
    '''
    Constructor to build filepath objects
    
    Attributes
    ----------
    path : str
        The path to the directory
    
    exists : bool
        Defines whether or not the directory is real
    
    Methods
    -------
    get_path() -> str 
    is_real () -> bool
    
    
    '''
    
    
def get_path():
    filepath = input("Enter filepath of desired folders to sort: \n")
    if (filepath == "t"):   #t short for test; for testing purposes
        filepath = "/home/humza/Music/DCIM/Testings"

if os.path.isdir(filepath):
    

for root, dirs, files in os.walk(filepath):
#root is filepath, dirs is a list of 
    #Testings folder used as a sample for testing; delete/replace later
    for file in files:  
        if file.endswith(".mp3"):
            song_list_a.write("\n")
            song_list_a.write(os.path.join(root, file))
            #Loops through all mp3 files in the filepath and adds their 
            #filepath to song_list.txt


song_list_a.close()
