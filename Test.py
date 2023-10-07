import sys

sys.path.append("c:/Scripts/MyPythonToolBox/Utils/")
from fileutil import FileUtil 

f = FileUtil()
size = f.get_file_size('C:/Scripts/MyPythonToolBox/LICENSE')
print("LICENSE file size (KB): " + str(size))

last_access = f.get_file_last_access('C:/Scripts/MyPythonToolBox/LICENSE')
print("LICENSE file last logged on : " + str(last_access))

my_files = f.get_files_in_folder('c:/Scripts/MyPythonToolBox')
print(my_files)

my_files = f.get_files_in_folder('c:/Scripts/MyPythonToolBox','py')
print(my_files) 