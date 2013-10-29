#!/usr/bin/python
"""Calls system_profiler and prints hardware info about
the current machine"""

import plistlib
import subprocess

def main():
    '''Main routine'''
    cmd = ['/usr/sbin/system_profiler', 'SPHardwareDataType', '-xml']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, error) = proc.communicate()

    info = plistlib.readPlistFromString(output)

    hardware_info = info[0]['_items'][0]
    for key, value in hardware_info.items():
        if not key.startswith('_'):
            print "%s: %s" % (key, value)


if __name__ == "__main__":
    main()