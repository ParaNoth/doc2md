import testdoc
import outputtxt
import renamepic
import sys
import os
import md2html

def main(dir):

    testdoc.wordsToHtml(dir)
    filelist = testdoc.wordsTotxt(dir)
    print filelist
    filelist1 = []
    for files in filelist:
        filelist1.append(os.path.splitext(files)[0])
    print filelist1
    for files in filelist1:
        temppath = files + '.files'
        print temppath
        renamepic.renamepic(temppath)
        renamepic.outputtxt(temppath)
    for files in filelist1:
        outputtxt.output(files)
    md2html.md2html(dir)

if __name__ == '__main__':
    ddir = sys.path[0]
    print ddir
    main(ddir)