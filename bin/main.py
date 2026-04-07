from bin.notifier import checker
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import asyncio

class mangaNotifierApp(App):
    def build(self):
        layout = GridLayout(cols=3)
        # Widgets
        self.interval_widget = TextInput(text="Write the interval here in seconds", multiline=False)
        self.manga_id = TextInput(text="Write the manga_id", multiline=False)
        self.manga_name = TextInput(text="Write the manga name in original language", multiline=False)
        
        # Event binds
        self.interval_widget.bind(on_text_validate=self.return_interval)
        self.manga_id.bind(on_text_validate=self.return_id)
        self.manga_name.bind(on_text_validate=self.return_name)
        
        # Add Widgets
        layout.add_widget(self.interval_widget)
        layout.add_widget(self.manga_id)
        layout.add_widget(self.manga_name)
        
        
        
        return layout
    
    def return_id(self, instance):
        """
        Returns the manga-id
        """
        self.mangaId = instance.text
        print(self.mangaId)
        try:
            asyncio.run(checker(self.mangaInterval, self.mangaId, self.mangaName))
            print("Sucess")
        except (NameError, AttributeError):
            print("Unsucessful")
    
    def return_name(self, instance):
        """
        Returns the name
        """
        self.mangaName = instance.text
        print(self.mangaName)
        try:
            asyncio.run(checker(self.mangaInterval, self.mangaId, self.mangaName))
            print("Sucess")
        except (NameError, AttributeError):
            print("Unsucessful")

    def return_interval(self, instance):
        """
        Returns the interval
        """
        try:
            self.mangaInterval = int(instance.text)
        except ValueError:
            print("Interval cannot be non-numeric.")
        print(self.mangaInterval)
        try:
            asyncio.run(checker(self.mangaInterval, self.mangaId, self.mangaName))
            print("Sucess")
        except (NameError, AttributeError):
            print("Unsucessful")
    
    
    
    
    
if __name__ == "__main__":
    mangaNotifierApp().run()