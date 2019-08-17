#Created Root class
#Will move validation process from get_path() to class root
import os


class Root():
    '''
    stores valid roots and verifies that they're valid moving on
    
    Attributes
    ----------
    
    Methods
    -------
    '''
    
    def __init__(self, path):
        self.Root = Root
        self.path = path
    
    def get_path():
        '''
        Asks the user for the targeted directory, then verifies that it
        is valid
        
        Parameters
        ----------
        
        Returns
        -------
        path : str
            The path inputted by the user, which has been confirmed to 
            be valid 
        
        Raises
        ------
        
        '''
        path = ""
        
        #loop used to control when path is returned
        while(True):
            path = input("Enter filepath of desired folders to sort: \n")
            if path == "t":  
                path = "/home/humza/Music/DCIM/Testings"
            #t short for test; for testing purposes
            if os.path.isdir(path): 
                print("\n Valid path \n")
                break
            
            else:
                print("\n Invalid path \n")
                    
        return path
    
class Target_Path(Root):
    '''
    a class to hold the filepaths that the user wants to use 
    
    Attributes
    ----------
    path : str
        The path to the directory
        
    Methods
    -------
    
    make_list()
    '''
    
    def __init__(self):
        '''
        Constructor to build filepath objects
    
        Parameters
        ----------
        path : str
            The path to the directory
    
        '''
        self.root = root

class Song_List():
    '''
    
    '''
    def make_new_list(path):
        '''
        Creates a new list of the mp3 files in a filepath, and stores in a .txt
        
        Parameters
        ----------
        path : str
            The path holding mp3 files to be listed in the txt
        
        Returns
        -------
        
        Raises
        ------
        
        '''
        print(path)
        txt_name = ("{}.txt").format(path)
        print(txt_name)
        
        song_list_w = open(txt_name, "w")    
        song_list_w.write("bad")
        song_list_w.close()
    #This will only be used to overwrite everything in the file so that 
    #the script can be run multiple times            
        song_list_a = open(txt_name, "a")
        
        for root, dirs, files in os.walk(path):
        #root returns filepaths separately
        #dirs is a list of folders and subfolders within them
        #files is a list of all files, divided based on their folder
            for file in files:  
                if file.endswith(".mp3"):
                    song_list_a.write("\n")
                    song_list_a.write(os.path.join(file))
                    #Loops through all mp3 files in the filepath and adds their
                    #filepath to song_list.txt
        song_list_a.close()


    def merge_list(path):
        #Sort list alphabetically so that it is easier to figure out if an item is already in the list
        '''
        
        Parameters
        ----------
        
        Returns
        -------
        '''
        
        song_list_a = open("{}.txt".format(path), "a")
        song_list_r = open("{}.txt".format(path), "r") 
        
        for root, dirs, files in os.walk(path):
        #root returns filepaths separately
        #dirs is a list of folders and subfolders within them
        #files is a list of all files, divided based on their folder
            for file in files:  
                if (file in song_list_r == True):
                    if file.endswith(".mp3"):
                        song_list_a.write("\n")
                        song_list_a.write(os.path.join(root, file))
                        #Loops through all mp3 files in the filepath and adds their
                        #filepath to song_list.txt
        song_list_a.close()
        print("e")
        for x in song_list_r:
            print(x)
        song_list_r.close()
        
        