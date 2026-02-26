[app]
title = Muhammed System
package.name = muhammedsystem
package.domain = org.muhammed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf,doc,zip
version = 0.1
requirements = python3,kivy,pyTelegramBotAPI
orientation = portrait
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
[buildozer]
log_level = 2
warn_on_root = 1
