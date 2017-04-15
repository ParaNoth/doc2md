#!/usr/bin/python
#-*- coding: gbk -*-

import re
def output(filename):
    txtnum = 0
    file1name = filename+'.txt'
    file2name = filename+'.files/name.txt'
    file1 = open(file1name, 'r')
    file2 = open(file2name, 'r')
    file3 = open('filetxt0.txt', 'w')
    txtbuf=[]
    myline=["",""]
    file3 = open('output.md', 'w')
    for eachline in file1:
        myline[0] = myline[1]
        myline[1] = eachline
        if myline[0] == "":
            continue
        myline[1] = myline[1].lstrip()
        myline[1] = myline[1].lstrip('\xa1')
        myline[1] = myline[1].rstrip('\n')
        myline[1] = myline[1].rstrip()
        myline[0] = myline[0].rstrip('\n')
        myline[0] = myline[0].rstrip()
        myline[0] = myline[0].lstrip('\xa1')
        print eachline[0:4] == '作者'
        if ('作者' in myline[1] or '来源' in myline[1]) and '来源' in myline[1] and '时间' in myline[1]:
            txttmp = '####<center>' +  myline[0] + '</center>  \n'
            txtbuf.append('\n')
            txtbuf.append(txttmp)
            continue
        elif ('作者' in myline[0] or '来源' in myline[0]) and '来源' in myline[0] and '时间' in myline[0]:
            txttmp = '<center><small>' + myline[0] + '</small></center>  \n'
            txtbuf.append(txttmp)
            continue
        elif myline[0] == '　　{{}}\n' or myline[0] == '{{}}\n' or myline[0] == '{{}}' or myline[0] == '　　{{}}' or "{{}}" in myline[0]:
            txtbuf.append(file2.readline())
            txtbuf.append('\n')
            continue
        elif '链接：' in myline[0] or '链接:' in myline[0]:
            txttmp = re.split('\n|：',myline[0])
            temptxt = '><small>' + txttmp[0] + ':' + '</small>   \n'
            print temptxt
            txtbuf.append(temptxt)
            if txttmp[1] != '':
                temptxt = '><small><' + txttmp[1]+'></small>  \n'
                print temptxt
                txtbuf.append(temptxt)
        elif 'http' in myline[0]:
            txttmp = re.split('\n', myline[0])
            temptxt = '><small><' + txttmp[0] + '></small>  \n'
            print temptxt
            txtbuf.append(temptxt)
        elif myline[0] == '' or myline[0] == '\n':
            continue
        else:
            temptxt = '&emsp;&emsp;' +  myline[0] + '  \n'
            txtbuf.append(temptxt)
            txtbuf.append('\n')
    if temptxt != '\n' or temptxt != '':
        temptxt = re.split('\n', myline[1])
        txttmp = '><small><' + temptxt[0] + '></small>  \n'
        txtbuf.append(txttmp)
    if file3.closed == False:
        file3.writelines(txtbuf)
        file3.close()
    file1.close()
    file2.close()

if __name__ == '__main__':
    output('第5周-博弈论')
