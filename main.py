from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        #Get the user query
        query = self.manager.current_screen.ids.user_query.text
        #Fetches the wikipedia page corresponding to the {query}
        page = wikipedia.page(query)
        png_image = [img for img in page.images if img.lower().endswith('png')]
        image_url = png_image[0]
        #Downloading the image
        req = requests.get(image_url)
        image_path = 'images/image.png'
        with open(image_path, 'wb') as file:
            file.write(req.content)
        #Set the image in the image widget
        self.manager.current_screen.ids.img.source = image_path

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

