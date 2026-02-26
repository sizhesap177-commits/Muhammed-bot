[app]
title = Muhammed System
package.name = muhammed_bot
package.domain = org.muhammed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Gereken kütüphaneleri buraya tam yazdım:
requirements = python3,kivy,pyTelegramBotAPI,requests,urllib3,certifi,chardet,idna,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android Ayarları
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
