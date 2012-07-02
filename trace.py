#!/usr/bin/python

###############################################################
import sys
import types
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
        sys.stdout.write("[DEBUG]: "+info+"\n")

def print_trace(level,parm):
    if not debug_info.has_key(level):
        sys.stderr.write("Missing........\n")
        return
    if level < current_level:
        __debug("Current Level:"+str(current_level)+",can not display message!!");
        return

    sys.stdout.write("["+debug_info[level]+"]:"+parm+"\n")


if __name__ == "__main__":
#    global current_level
    current_level=1
    print_trace(1,"hello")
    print_trace(2,"MyGod")
    print_trace(3,"aksdfjskladf")
    print_trace(4,"safsadfasdfsadfasdf")



