#!/usr/bin/python
# -*- coding: cp936 -*-
#
# site: www.ahlinux.com
# -*-coding:utf-8 -*-
from win32com import client as wc
import os
import glob
import sys



def wordsToHtml(dir):
    word = wc.Dispatch('Word.Application')
    # �õ�Ҫ�����word��׺Ϊdoc�ļ��б�
    filelist1 = glob.glob(dir + '/*.doc')
    # print (filelist1)
    for wardfullName in filelist1:
        doc = word.Documents.Open(wardfullName)
        htmlfullName = wardfullName[:-3] + 'html'
        txtfullName = wardfullName[:-3] + 'txt'

        print('���ڴ���ͼƬ----------' + htmlfullName)
        print('���ڴ�������----------' + txtfullName)

        doc.SaveAs(htmlfullName, 10)
        doc.SaveAs(txtfullName, 5)

        os.remove(htmlfullName)
        print('����ɾ��html�ļ�----------' + htmlfullName)
        doc.Close()
        # �õ�Ҫ�����word��׺Ϊdocx�ļ��б�
    filelist2 = glob.glob(dir + '/*.docx')
    # print (filelist2)
    for wardfullName in filelist2:
        doc = word.Documents.Open(wardfullName)
        htmlfullName = wardfullName[:-4] + 'html'
        txtfullName = wardfullName[:-4] + 'txt'

        print('���ڴ���ͼƬ----------' + htmlfullName)
        print('���ڴ�������----------' + txtfullName)

        doc.SaveAs(htmlfullName, 10)
        doc.SaveAs(txtfullName, 5)

        os.remove(htmlfullName)
        print('����ɾ��html�ļ�----------' + htmlfullName)
        doc.Close()
    word.Quit()
    return filelist1+filelist2
def wordsTotxt(dir):
    word = wc.Dispatch('Word.Application')
    # �õ�Ҫ�����word��׺Ϊdoc�ļ��б�
    filelist1 = glob.glob(dir + '/*.doc')
    # print (filelist1)
    for wardfullName in filelist1:
        doc = word.Documents.Open(wardfullName)
        word.Selection.Find.ClearFormatting()
        word.Selection.Find.Replacement.ClearFormatting()
        word.Selection.Find.Execute('^g', False, False, False, False, False, True, 1, True, '{{}}', 2)
        word.Selection.Find.Execute('^t', False, False, False, False, False, True, 1, True, '', 2)
        htmlfullName = wardfullName[:-3] + 'html'
        txtfullName = wardfullName[:-3] + 'txt'

        print('���ڴ�������----------' + txtfullName)


        doc.SaveAs(txtfullName, 5)


        doc.Close()
        # �õ�Ҫ�����word��׺Ϊdocx�ļ��б�
    filelist2 = glob.glob(dir + '/*.docx')
    # print (filelist2)
    for wardfullName in filelist2:
        doc = word.Documents.Open(wardfullName)
        word.Selection.Find.ClearFormatting()
        word.Selection.Find.Replacement.ClearFormatting()
        word.Selection.Find.Execute('^g', False, False, False, False, False, True, 1, True, '{{}}', 2)
        word.Selection.Find.Execute('^t', False, False, False, False, False, True, 1, True, '', 2)
        word.Selection.Find.Execute('��', False, False, False, False, False, True, 1, True, '', 2)
        htmlfullName = wardfullName[:-4] + 'html'
        txtfullName = wardfullName[:-4] + 'txt'


        print('���ڴ�������----------' + txtfullName)


        doc.SaveAs(txtfullName, 5)

        doc.Close()
    word.Quit()
    return filelist1 + filelist2

if __name__ == '__main__':
    ddir = sys.path[0]
    wordsToHtml(ddir)
    wordsTotxt(ddir)
