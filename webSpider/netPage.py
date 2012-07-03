#!/usr/bin/python
# -*- coding:utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.
import os
import io
import sys
import urllib2
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
sys.path.insert(0,os.path.abspath(os.path.pardir))
import libs

__author__="ewentzh"
__date__="$2012-7-1 09:45:36$"


def requestPage(url):
    '''
    Request url link from the Internet.
    
    it is the Orignal HTML content.
    '''
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    content = response.read()
    response.close()

    return content

def utf8_encoding(content):
    '''
    hello
    '''
    return content.decode('gb2312').encode('utf8').replace('gb2312','utf-8')



def test__getPage():
    url = "http://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%86%B7%E5%BA%93&rsv_spt=1&issp=1&rsv_bp=0&ie=utf-8&tn=baiduhome_pg&inputT=2063"
    content = requestPage(url)
    print content
    content = utf8_encoding(content)
    print content

if __name__ == "__main__":
    libs.trace.info(" ============  Here Start the net Page Script Test ==============")
    libs.trace.info(" ==  1. test Request Page: ")
    libs.trace.info(" ==  2. test Encoding to utf-8:")
    test__getPage()


