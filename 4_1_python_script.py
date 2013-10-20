#!/usr/bin/env python
import sys

def sayOuch(num_times=1):
    """This function says OUCH! the given number of times
    """
    for i in range(0, num_times):
        print "OUCH!!"

def main():
    if len(sys.argv) > 1:
        num_times = int(sys.argv[1])
    else:
        num_times = 1
        
    sayOuch(num_times)

if __name__ == "__main__":
    main()
