#!/usr/bin/python


import sys
import trace



def test__trace():
    trace.error("Here is the Error Information!!")
    trace.warning("Here is the Warning Information")
    trace.info("Here is the Trace Information")
    trace.debug("Here is the Debug Information")


if __name__ == "__main__":
    test__trace()

