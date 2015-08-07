# coding:utf-8

#对指定目录下的文件夹按大小排序

import os
import sys
def getDirSize(dir):
	sizes = 0L
	for root , dir , files in os.walk(dir):
		for file in files:
			size = os.path.getsize(os.path.join(root,file))
			sizes += size
	return sizes

def myCmp(dir1 , dir2):
	size1 = getDirSize(dir1)
	size2 = getDirSize(dir2)
	if size1 < size2:
		return -1
	elif size1 > size2:
		return 1
	else:
		return 0
	
def sortDirBySize(dir):
	dirs = []
	for root , dir , files in os.walk(dir):
		for d in dir:
			dirs.append(os.path.join(root,d))
		break
	dirs = sorted(dirs , cmp = myCmp)
	for dir in dirs:
		print(dir)
		
if __name__ == '__main__':
	sortDirBySize(sys.argv[1])
