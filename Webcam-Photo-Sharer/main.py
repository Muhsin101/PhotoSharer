# --- Imports -----------------------------------------------------------------

from kivy.app import App
#    App is the base class for your Kivy application. You subclass this to
#    define your app’s behavior and UI entry point.

from kivy.uix.screenmanager import ScreenManager, Screen
#    ScreenManager is a widget that lets you switch between different screens.
#    Screen is the base class you subclass for each individual “page” in your app.

from kivy.lang import Builder
#    Builder is Kivy’s KV-language loader; it parses and creates widgets defined
#    in .kv files so you can separate presentation from logic.


# --- Load your KV layout file ------------------------------------------------

Builder.load_file('frontend.kv')
#    Reads and applies the rules in frontend.kv at import time. Any <WidgetName>
#    definitions in that file become available to the Python code.

class CameraScreen(Screen):
    pass

class ImageScreen(Screen):
    pass

# --- Define the root widget ---------------------------------------------------
class RootWidget(ScreenManager):
    pass
#    This class ties into your KV file: if you have a <RootWidget> rule
#    in frontend.kv, it will configure this ScreenManager (e.g. adding Screens).


# --- Define your App class ----------------------------------------------------

class MainApp(App):

    def build(self):
        # build() is called when the app starts.
        # It must return the root widget of your UI tree.
        return RootWidget()


# --- Run the application ------------------------------------------------------

if __name__ == '__main__':
    MainApp().run()
#    Creates an instance of MainApp and starts the Kivy event loop.
#    .run() sets up the window, processes touch/keyboard, and renders frames.
