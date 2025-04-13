[app]
title = WhatsApp Scheduler
package.name = whatsappscheduler
package.domain = org.whatsappscheduler
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.0.0,pywhatkit==5.4,python-dateutil==2.8.2
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.0.0
fullscreen = 0
android.permissions = INTERNET
android.arch = arm64-v8a
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
android.gradle_dependencies = androidx.appcompat:appcompat:1.0.2,androidx.constraintlayout:constraintlayout:1.1.3,androidx.swiperefreshlayout:swiperefreshlayout:1.1.0

[buildozer]
log_level = 2
warn_on_root = 1
