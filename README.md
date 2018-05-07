# basic-python-android #
The most basic Python Android App

# HOW TO DEPLOY TO ANDROID #
 ONLY COMPATIBLE WITH LINUX OR LINUX VIRTUAL MACHINES RIGHT NOW
 use oracle vm ware and download a vm box from the kivy website online
 if you are running windows. (https://kivy.org/#download)

 You will need the latest version of Kivy
>> pip install --upgrade Kivy

 And the latest version of Buildozer
>> pip install --upgrade buildozer

 Navigate to the main.py directory in your console
 If you do not have a "buildozer.spec" file in this directory
 use this command to create one, then modify it to suit you.

>> buildozer init

 Create the android .apk file with this command:

>> buildozer -v android debug

 The .apk file you just created will be in this directory by default "/home/Kivy/app/bin"
 Unless modified in the buildozer.spec file
 you can also add parameters such as;

>> buildozer -v android debug deploy run

 Which will automatically install the app on your phone
 if it is connected and has the appropriate drivers

 Otherwise, navigate to the bin.dir
 and manually move the .apk file onto your phone.
 when opened on your phone, the application will install and run.

 You may need to modify the buildozer.spec file.

 RECOMMENDED: change build.dir @ line 187
 in the buildozer.spec file to: "/home/ MY USER NAME /app/build"
 RECOMMENDED: change bin.dir @ line 189
 in the buildozer.spec file to: "/home/ MY USER NAME /app/bin"
