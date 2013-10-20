#!/usr/bin/python

import plistlib
import subprocess

cmd = ['/usr/sbin/system_profiler', 'SPHardwareDataType', '-xml']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error) = proc.communicate()

info = plistlib.readPlistFromString(output)

hardware_info = info[0]['_items'][0]
for key, value in hardware_info.items():
	print "%s: %s" % (key, value)
