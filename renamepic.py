#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os
from PIL import Image
import time
pictype=[".png", ".gif", ".jpg", ".jpeg"]
def renamepic(dir):
    timedir = time.strftime('%m%d%H%M%S',time.localtime(time.time()))
    filelist = os.listdir(dir)

    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(dir, files);  # 原来的文件路径
        filename = os.path.splitext(files)[0]  # 文件名
        filetype = os.path.splitext(files)[1]  # 文件扩展名
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        if filetype not in pictype:
            continue
        Newdir = os.path.join(dir, timedir + filename + filetype);  # 新的文件路径
        os.rename(Olddir, Newdir)  #
def outputtxt(dir):
    temptxtpath = dir + '/name.txt'
    file1 = open(temptxtpath, 'w')
    filelist = os.listdir(dir)
    print filelist
    nametxt = []
    for files in filelist:
        temppath = dir + '/' + files
        filetype = os.path.splitext(files)[1]
        filename = os.path.splitext(files)[0]  # 文件名
        if filetype not in pictype:
            continue
        pic = Image.open(temppath)
        height = pic.size[1]
        width = pic.size[0]
        #<p style="text-align: left;"><img class="alignnone size-full wp-image-1345" src="http://fd.lidongpeng.com.cn/wp-content/uploads/2017/01/5-5-1.png" alt="5-5" width="889" height="218" /></p>
        #temptxt = "weith = " + str(weith) + "height = " + str(height) + "\n"
        #http://sii.fudan.edu.cn/wp-content/uploads/2017/03/0327150313image003.jpg
        temptxt = r'<center>![](http://sii.fudan.edu.cn/wp-content/uploads/2017/04/'+ files + ')</center>' + '\n'
        nametxt.append(temptxt)
    file1.writelines(nametxt)
    file1.close()

if __name__ == '__main__':
    #renamepic('.')
    outputtxt('.')
