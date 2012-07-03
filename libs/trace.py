#!/usr/bin/python

###############################################################
import sys
import os
import os.path
import types
import time
import traceback
###############################################################
__author__="ewentzh"
__date__="$2012-7-1 19:45:36$"
###############################################################

debug_on = "on"
current_level=1
debug_info={   1:  "DEBUG",
               2:  "TRACE",
               3:  "WRANING",
               4:  "ERROR"
            }

def set_debug_level(lvl):
    if type(lvl) == type(1):
        current_level = lvl
        return
    print_trace("Set Debug Level Error, incorrect Data Type!!")


def __debug(info):
    global debug_on
    if debug_on == "on":
        print >> sys.stdout, "[DEBUG]: "+info+"\n"

def print_trace(level,msg):
    if not debug_info.has_key(level):
        print>>sys.stderr,"Missing........\n"
        return
    if level < current_level:
        __debug("Current Level:"+str(current_level)+",can not display message!!");
        return
    formatMsg = header(level,msg)
    if level == 4:
        print >> sys.stderr, formatMsg
    else:
        print >> sys.stdout, formatMsg


def header(lvl,msg):
    timeNow = time.strftime('%H:%M:%S',time.localtime(time.time()))
    stack = traceback.extract_stack()[-4]
    return "[%s %s %s:%d %s]: %s" % (debug_info[lvl].ljust(7),os.path.basename(stack[0]),stack[2], stack[1], timeNow,msg)


def error(msg):
    print_trace(4,msg)

def warning(msg):
    print_trace(3,msg)

def info(msg):
    print_trace(2,msg)


def debug(msg):
    print_trace(1,msg)



if __name__ == "__main__":
#    global current_level
    current_level=1
    print_trace(1,"hello")
    print_trace(2,"MyGod")
    print_trace(3,"aksdfjskladf")
    print_trace(4,"safsadfasdfsadfasdf")

    current_level=0
    error("Here is The Error!!!!!")
    warning("Here is the Warning !!!")
    info("Here is the Info")
    debug("Here is debug Info")



