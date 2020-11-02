# -*- coding: utf-8 -*-

import urllib2

def findkey(s):

try:
    result = urllib2.urlopen("http://dict-co.iciba.com/api/dictionary.php?w=take&key=E8CE4224DE2FDA5D47D115C1E0181BB0").read()
except urllib2.HTTPError,e:
    print e.code

#print result
