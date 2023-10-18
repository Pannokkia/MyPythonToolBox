import os
import math 
import sys
from os import listdir
from os.path import isfile, join
import glob
import datetime

class FileUtil:
    def __init__(self):
        pass

    def get_file_size(self,filename):
        """_summary_

        Args:
            filename (string): file for which you nees information about size

        Returns:
            int: File size in KB 
        """
        
        try:
            return math.floor(os.stat(filename).st_size / 1000)
        except FileNotFoundError:
            print('File not found!')
            sys.exit(-1)

    def get_file_last_access(self,filename):
        """_summary_
        Args:
            filename (string): file for which you want to obtain the las access information

        Returns:
            datetime.datetime: last access to the file, date and time in human readable format 
        """

        try:
            unix_epoch = os.stat(filename).st_atime
            return datetime.datetime.fromtimestamp(unix_epoch)
        except FileNotFoundError:
            print('File not found!')
            sys.exit(-1)

    def get_files_in_folder(self,folder,file_extension='*'):
        """_summary_

        Args:
            folder (string): destination folder to get files list
            file_extension (string, optional): is possible to use filter to get list of files. Defaults to '*'.

        Returns:
            List: list of files in indicated folder
        """
        try:
            only_files = []
            only_files = [f for f in listdir(folder) if isfile(join(folder, f))]

            if(file_extension != '*'):
                only_files = glob.glob('*.' + file_extension)

            return only_files
        except FileNotFoundError:
            print('File not found!')
            sys.exit(-1)

    def get_file_lines_number(self,filename):
        
        """_summary_
        Args:
            filename (string): file for which you want to know lines number

        Returns:
            int: number of lines read from file
        """
        
        try:
            line = 0
            
            with open(filename,'r') as f:
              lines = f.readlines()
              for l in lines:
                line = line + 1

            return line   
        except FileNotFoundError:
            print('File not found!')
    