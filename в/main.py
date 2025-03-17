from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.operators = set(['+', '-', '*', '/'])
        self.last_was_operator = None
        self.last_was_equal = False

        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="0", font_size=55, halign="right", valign="middle")
        self.label.bind(size=self.label.setter('text_size'))
        self.layout.add_widget(self.label)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'expand': True})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.layout.add_widget(h_layout)

        return self.layout

    def on_button_press(self, instance):
        current = self.label.text
        button_text = instance.text

        if button_text == 'C':
            self.label.text = "0"
            self.last_was_operator = None
            self.last_was_equal = False
        elif button_text == '=':
            if self.last_was_equal:
                return
            try:
                self.label.text = str(eval(current))
                self.last_was_equal = True
            except Exception:
                self.label.text = "Error"
        else:
            if current == "0" or self.last_was_equal:
                current = ""
            if button_text in self.operators:
                if self.last_was_operator:
                    return
                self.last_was_operator = True
            else:
                self.last_was_operator = False

            self.label.text = current + button_text
            self.last_was_equal = False

if __name__ == "__main__":
    CalculatorApp().run()