#!/usr/bin/python

'''Uses Cocoa classes via PyObjC to set the desktop picture on all screens.
Tested on Mountain Lion.

See:
https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/classes/NSWorkspace_Class/Reference/Reference.html

https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html

https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/classes/NSScreen_Class/Reference/Reference.html
'''

from AppKit import NSWorkspace, NSScreen
from AppKit import NSWorkspaceDesktopImageScalingKey
from AppKit import NSImageScaleProportionallyUpOrDown
from AppKit import NSWorkspaceDesktopImageAllowClippingKey
from Foundation import NSURL

picture_path = "/Library/Desktop Pictures/Beach.jpg"

# generate a fileURL
file_url = NSURL.fileURLWithPath_(picture_path)

# make image options dictionary
options = {
    NSWorkspaceDesktopImageScalingKey: NSImageScaleProportionallyUpOrDown,
    NSWorkspaceDesktopImageAllowClippingKey: True
}

# get shared workspace
ws = NSWorkspace.sharedWorkspace()

# iterate over all screens
for screen in NSScreen.screens():
    # tell the workspace to set the desktop picture
    (result, error) = ws.setDesktopImageURL_forScreen_options_error_(
                file_url, screen, options, None)