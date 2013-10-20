import plistlib
plistinfo = plistlib.readPlist("/Applications/Safari.app/Contents/Info.plist")
plistinfo["CFBundleGetInfoString"]

plist_version =  plistinfo["CFBundleShortVersionString"]
print plist_version

plistinfo = plistlib.readPlist("/Library/Preferences/com.apple.loginwindow.plist")
