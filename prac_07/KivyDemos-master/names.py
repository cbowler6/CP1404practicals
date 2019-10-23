from kivy.app import App
from kivy.lang import Builder


class Names(App):
    def build(self):
        self.names = ["bob", "steve", "james"]
        self.title = "names"
        self.root = Builder.load_file('names.kv')
        return self.root

    def create_widgets(self):
        for name in self.names:
            new_label = name
            self.root.ids.entries_box.add_label(new_label)

Names().run()
