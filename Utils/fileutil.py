import os
import math 
import sys
from os import listdir
from os.path import isfile, join
import glob

class FileUtil:
    def __init__(self):
        pass

    def get_file_size(self,filename):
        '''Return file size in KB'''
        try:
            return math.floor(os.stat(filename).st_size / 1000)
        except FileNotFoundError:
            print('File not found!')
            sys.exit(-1)

    
    def get_files_in_folder(self,folder,file_extension='*'):
        '''Return list of files in indicated folder'''
        '''is possible to use filter to get list of files (file_extension) '''
        try:
            only_files = []
            only_files = [f for f in listdir(folder) if isfile(join(folder, f))]

            if(file_extension != '*'):
                only_files = glob.glob('*.' + file_extension)

            return only_files
        except FileNotFoundError:
            print('File not found!')
            sys.exit(-1)