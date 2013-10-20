# https://developer.apple.com/library/ios/documentation/CoreFoundation/Reference/CFPreferencesUtils/Reference/reference.html

import CoreFoundation
print CoreFoundation.CFPreferencesCopyAppValue("HomePage", "com.apple.Safari")

CoreFoundation.CFPreferencesSetAppValue("HomePage", "http://www.google.com", "com.apple.Safari")

print CoreFoundation.CFPreferencesCopyAppValue("HomePage", "com.apple.Safari")
