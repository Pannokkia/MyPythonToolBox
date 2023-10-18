import sys
import datetime

sys.path.append("c:/Scripts/MyPythonToolBox/Utils/")
from fileutil import FileUtil 
from dateutil import DateUtil

f = FileUtil()
size = f.get_file_size('C:/Scripts/MyPythonToolBox/LICENSE')
print("LICENSE file size (KB): " + str(size))

last_access = f.get_file_last_access('C:/Scripts/MyPythonToolBox/LICENSE')
print("LICENSE file last logged on : " + str(last_access))

my_files = f.get_files_in_folder('c:/Scripts/MyPythonToolBox')
print(my_files)

my_files = f.get_files_in_folder('c:/Scripts/MyPythonToolBox','py')
print(my_files) 

lines_count = f.get_file_lines_number('C:/Scripts/MyPythonToolBox/LICENSE')
print(str(lines_count)) 

d = DateUtil()
date_time = datetime.datetime.now()

today = d.set_date_format(date_time,'%Y/%m/%d')
print(type(today))
print(today)