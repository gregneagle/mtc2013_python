#!/usr/bin/python

import FoundationPlist

plistinfo = FoundationPlist.readPlist("/Library/Preferences/com.apple.loginwindow.plist")
print plistinfo