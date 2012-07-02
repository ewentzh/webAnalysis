#!/usr/bin/python
# -*- coding:utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

########################################################
##
##  Description: this file is used to parse the searching 
##               URL 
##  Author:  ewentzh
##  Date:    2012-7-1
##  History: 
##           1. 2012-7-1  fist revision.   ewentzh
##
########################################################
##################### import  ##########################
import urllib2
import sys
import os
import io

__author__="ewentzh"
__date__="$2012-7-1 09:45:36$"

req = urllib2.Request("http://www.baidu.com");
response = urllib2.urlopen(req);

content=response.read().decode("gb2312").encode("utf8")
content2=content.replace('gb2312', 'utf-8')

print content2



print "\n"
print "=================================================="
print __author__
print "\n"


