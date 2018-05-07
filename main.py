# ==================== HOW TO DEPLOY TO ANDROID ========================= #
# ONLY COMPATIBLE WITH LINUX OF LINUX VIRTUAL MACHINES RIGHT NOW
# use oracle vm ware and download a vm box from the kivy website online
# if you are running windows. https://kivy.org/#download
#
# You will need the latest version of Kivy
# >> pip install --upgrade Kivy
#
# And the latest version of Buildozer
# >> pip install --upgrade buildozer
#
# Navigate to the main.py directory in your console
# If you do not have a "buildozer.spec" file in this directory
# use this command to create one, (then modify it to suit you)
#
# >> buildozer init
#
# Create the android .apk file with this command:
#
# >> buildozer -v android debug
#
# The .apk file you just created will be in this directory by default "/home/Kivy/app/bin"
# Unless modified in the buildozer.spec file
# You can also add parameters such as;
#
# >> buildozer -v android debug deploy run
#
# Which will automatically install the app on your phone
# if it is connected and has the appropriate drivers
#
# Otherwise, navigate to the bin.dir
# and manually move the .apk file onto your phone.
# when opened on your phone, the application will install and run.
#
# You may need to modify the buildozer.spec file.
#
# RECOMMENDED: change build.dir @ line 187
# in the buildozer.spec file to: "/home/ MY USER NAME /app/build"
# RECOMMENDED: change bin.dir @ line 189
# in the buildozer.spec file to: "/home/ MY USER NAME /app/bin"
# ======================================================================= #

# Import Essential Kivy Modules
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window


# MAIN GAME CLASS
# Stores the core app functions
class mainGame(Widget):

    # Step Function
    def gameStep(self, *args):

        # UPDATE Variables
        self.variable.text = str(int(self.variable.text) + 1)
        # UPDATE Widget Position
        self.variable.x, self.variable.y = Window.width/2, Window.height/2

    # INIT mainGame()
    def __init__(self, **kwargs):
        # SUPER the mainGame() class
        super(mainGame, self).__init__(**kwargs)
        # CREATE WIDGET
        self.variable = Label(text='0', halign='left')
        # ADD WIDGET TO WINDOW
        self.add_widget(self.variable)
        # RUN THIS FUNCTION
        # at 60 frames per 1 second
        Clock.schedule_interval(self.gameStep, 1/60)


# KIVY LAUNCHER - ESSENTIAL
# Used to run the application
class coreApp(App):

    # RUN()
    def build(self):
        # Return the main game class on run()
        return mainGame()


# RUN THE APP
# launches the application
if __name__ == "__main__":
    coreApp().run()
