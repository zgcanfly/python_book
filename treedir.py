import os
import os.path
#指明被遍历的文件夹
rootdir = './'
#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
for parent,dirnames,filenames in os.walk(rootdir):
        #输出文件夹信息
	for dirname in  dirnames:
		print ("parent is:" + parent)
		print  ("dirname is" + dirname)
		#输出文件信息
	for filename in filenames:
		print ("parent is:" + parent)
		print ("filename is:" + filename)
		#输出文件路径信息
		print ("the full name of the file is:" + os.path.join(parent,filename))