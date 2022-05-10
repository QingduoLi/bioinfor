# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:41:21 2020

@author: Administrator
"""

import PyPDF2 as pdf

inputfile = "d:/aaa.pdf"
outputfile = "d:/bbb.pdf"
reader = pdf.PdfFileReader(inputfile)
#pages = [num1, num2, num3, ..., numn]
pages = [18,19,20,21,22,23,24,33,34,44,45,46,85,86,87,88,89,147,148,149,150,151,152,153,154,155,156,157,158]
getpages = list()

for i in pages:
    page = reader.getPage(i-1) #page number starts with 0
    getpages.append(page)
	
writer = pdf.PdfFileWriter()
for page in getpages:
    writer.addPage(page)

with open(outputfile,'wb') as fh:
    writer.write(fh)