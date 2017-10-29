#-*- coding: gbk -*-

import os
import markdown
import codecs
def md2html(dir):
    filelist = os.listdir(dir)
    for files in filelist:
        #temppath = dir + '/' + files
        filetype = os.path.splitext(files)[1]
        filename = os.path.splitext(files)[0]  # 文件名
        if filetype != '.md':
            continue
        else:
            input_file = codecs.open(dir + '/' + files, mode= 'r', encoding='gbk')
            text = input_file.read()
            html = markdown.markdown(text)
            out_file = dir + '/' + filename + '.html'
            output_file = codecs.open(out_file, 'w', encoding='utf-8', errors='xmlcharrefreplace')
            output_file.write(html)
            input_file.close()
            output_file.close()

if __name__ ==  '__main__':
    md2html('.')


