# https://developer.apple.com/library/mac/documentation/cocoa/Reference/Foundation/Classes/NSUserDefaults_Class/Reference/Reference.html

import Foundation
defaults = Foundation.NSUserDefaults.standardUserDefaults()
defaults.dictionaryRepresentation()
defaults.dictionaryForKey_("com.apple.ColorSync.Devices")
defaults.dictionaryForKey_("NSPreferredWebServices")

defaults.setBool_forKey_(False,"MyAppNameOpenSplashScreen")
defaults.objectForKey_("MyAppNameOpenSplashScreen")

defaults.valueForKey_("MyAppNameOpenSplashScreen")

defaults.setObject_forKey_("niceperson@niceland.com","MyAppUserEmail")
defaults.valueForKey_("MyAppUserEmail")
