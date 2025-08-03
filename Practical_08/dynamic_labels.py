"""
CP1404/CP5632 Practical
Dynamic Labels GUI program
Author: Amir Askhatov
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

# Model (data)
NAMES = ["Amir", "John", "Sara", "Alex", "Alexandr"]

class DynamicLabelsApp(App):
    """A kivy app that dynamically creates labels for a list of names"""
    def build(self):
        """Build the GUI from KV file and add dynamic labels."""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add Label widgets for each name."""
        for name in NAMES:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)

if __name__ == '__main__':
    DynamicLabelsApp().run()