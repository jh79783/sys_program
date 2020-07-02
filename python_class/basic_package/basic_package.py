import os
import glob
curfile = os.path.abspath(__file__)
curdirpath = os.path.dirname(curfile)
print(curdirpath)
curdirpath = os.path.dirname(curdirpath)
print(curdirpath)
files = os.listdir(curdirpath)
print(files)

search_pattern = os.path.join(curdirpath, "*")
print("search pattern:", search_pattern)
filelist = glob.glob(search_pattern)
print("file list:", filelist)

filelist1 = [name for name in filelist if os.path.isfile(name)]
dirlist1 = [name for name in filelist if os.path.isdir(name)]
print("dir list", dirlist1)
print("file list", filelist1)

