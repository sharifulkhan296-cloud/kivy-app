from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TasbeehApp(App):
    def build(self):
        self.count = 0

        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Title Label
        self.title_label = Label(
            text="ডিজিটাল তাসবীহ", 
            font_size='32sp', 
            bold=True
        )
        
        # Count Display
        self.count_label = Label(
            text=str(self.count), 
            font_size='72sp', 
            bold=True
        )

        # Count Button
        self.count_button = Button(
            text="গণনা করুন (Count)", 
            font_size='24sp', 
            size_hint=(1, 0.3)
        )
        self.count_button.bind(on_press=self.add_count)

        # Reset Button
        self.reset_button = Button(
            text="পুনরায় শুরু (Reset)", 
            font_size='18sp', 
            size_hint=(1, 0.15)
        )
        self.reset_button.bind(on_press=self.reset_count)

        # Adding widgets to layout
        layout.add_widget(self.title_label)
        layout.add_widget(self.count_label)
        layout.add_widget(self.count_button)
        layout.add_widget(self.reset_button)

        return layout

    def add_count(self, instance):
        self.count += 1
        self.count_label.text = str(self.count)

    def reset_count(self, instance):
        self.count = 0
        self.count_label.text = str(self.count)

if __name__ == '__main__':
    TasbeehApp().run()

