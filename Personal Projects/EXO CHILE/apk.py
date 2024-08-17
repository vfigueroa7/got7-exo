import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.uix.image import Image

class TextProcessorApp(App):
    def build(self):
        self.title = 'Text Processor'
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Agregar imagen
        self.image = Image(source='sehun.jpg')  # Asegúrate de que 'imagen.jpg' esté en la misma carpeta
        layout.add_widget(self.image)
        
        self.input_label = Label(text='Hola, pon aquí el texto que quieras editar:')
        layout.add_widget(self.input_label)
        
        self.input_text = TextInput(multiline=False)
        layout.add_widget(self.input_text)
        
        self.process_button = Button(text='Procesar')
        self.process_button.bind(on_press=self.process_text)
        layout.add_widget(self.process_button)
        
        self.result_text = TextInput(readonly=True)
        layout.add_widget(self.result_text)
        
        self.copy_button = Button(text='Copiar al portapapeles')
        self.copy_button.bind(on_press=self.copy_to_clipboard)
        layout.add_widget(self.copy_button)
        
        return layout

    def process_text(self, instance):
        descripcion = self.input_text.text

        date_pattern = r'(\d{6})'
        final_pattern = r'\[ EXO Chile \]'

        emoji = []
        if "Video" in descripcion:
            emoji.append("🎥")
        if "Imagen" in descripcion:
            emoji.append("📸")
        if "Info" in descripcion:
            emoji.append("🌐")
        if "Trad" in descripcion:
            emoji.append("📝")
        if "◆" in descripcion and emoji:
            descripcion = descripcion.replace("◆", emoji[0])

        # Reemplazar las llaves en la descripción
        if "{" in descripcion or "}" in descripcion:
            descripcion = descripcion.replace("{", "").replace("}", "")

        match = re.search(date_pattern, descripcion)
        match_dos = re.search(final_pattern, descripcion)

        if match:
            date = match.group(0)
            date_index = descripcion.index(date)
            descripcion = descripcion[date_index:]

            if match_dos:
                final_text = match_dos.group(0)
                final_index = descripcion.index(final_text) + len(final_text)
                descripcion = descripcion[:final_index]
                if "#Chen" in descripcion:
                    descripcion = descripcion + "\n @weareoneEXO @CHEN_INB100 #EXO #엑소"
                elif "#Baekhyun" in descripcion:
                    descripcion = descripcion + "\n @weareoneEXO @B_hundred_Hyun #EXO #엑소"
                elif "#Xiumin" in descripcion:
                    descripcion = descripcion + "\n @weareoneEXO @XIUMIN_INB100 #EXO #엑소"
                elif "#Lay" in descripcion:
                    descripcion = descripcion + "\n @weareoneEXO @layzhang #EXO #엑소"
                else:
                    descripcion = descripcion + "\n @weareoneEXO #EXO #엑소"

                self.result_text.text = descripcion
            else:
                self.result_text.text = "No se encontró 'EXO Chile' en el texto."
        else:
            self.result_text.text = "El formato no es correcto."

    def copy_to_clipboard(self, instance):
        Clipboard.copy(self.result_text.text)

if __name__ == '__main__':
    TextProcessorApp().run()

