import sys

sys.path.append("c:/Scripts/Utils/")
from fileutil import FileUtil 

f = FileUtil()
size = f.get_file_size('C:/Scripts/LICENSE')
print("LICENSE file size (KB): " + str(size))

my_files = f.get_files_in_folder('c:/Scripts')
print(my_files)

my_files = f.get_files_in_folder('c:/Scripts','py')
print(my_files)