# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:41:21 2020

@author: Administrator
"""

import PyPDF2 as pdf
import numpy as np

inputfile = "e:/1.pdf"
outputfile = "e:/2.pdf"
reader = pdf.PdfFileReader(inputfile)  # pdf 是个package，里面啥都有。PdfFileReader是其中一个Class，看不出返回的reader是个什么东西
# pages = [num1, num2, num3, ..., numn]
pages = [1, 3, 5, 7]
getpages = list()

for i in pages:
    page = reader.getPage(i - 1)  # page number starts with 0
    getpages.append(page)

writer = pdf.PdfFileWriter()
for page in getpages:
    writer.addPage(page)

with open(outputfile, 'wb') as fh:
    writer.write(fh)
