import sys
import re
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtGui import QPixmap, QClipboard

class TextProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Processor')
        self.setGeometry(100, 100, 300, 300) 
        self.image_label = QLabel(self) 

        layout = QVBoxLayout()
    
        self.input_label = QLabel('Hola, pon aquí el texto que quieras editar:')
        layout.addWidget(self.input_label)


        self.input_text = QLineEdit(self)
        layout.addWidget(self.input_text)

        self.process_button = QPushButton('Procesar', self)
        self.process_button.clicked.connect(self.process_text)
        layout.addWidget(self.process_button)

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.copy_button = QPushButton('Copiar al portapapeles', self)
        self.copy_button.clicked.connect(self.copy_to_clipboard_result)
        layout.addWidget(self.copy_button)

        self.fancam_label = QLabel('Link de fancams:')
        layout.addWidget(self.fancam_label)
        self.fancam_text = QLineEdit(self)
        layout.addWidget(self.fancam_text)

        self.process2_button = QPushButton('Procesar', self)
        self.process2_button.clicked.connect(self.process2_text)
        layout.addWidget(self.process2_button)

        self.result2_text = QTextEdit(self)
        self.result2_text.setReadOnly(True)
        layout.addWidget(self.result2_text)

      
        self.copy2_button = QPushButton('Copiar al portapapeles', self)
        self.copy2_button.clicked.connect(self.copy_to_clipboard_result2)
        layout.addWidget(self.copy2_button)

        self.setLayout(layout)

    def process_text(self):
        descripcion = self.input_text.text()

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

                self.result_text.setPlainText(descripcion)
            else:
                self.result_text.setPlainText("No se encontró 'EXO Chile' en el texto.")
        else:
            self.result_text.setPlainText("El formato no es correcto.")

    def copy_to_clipboard_result(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.result_text.toPlainText())

    def process2_text(self):
        link = self.fancam_text.text()
        link += "/video/1"
        self.result2_text.setPlainText(link)

    def copy_to_clipboard_result2(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.result2_text.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextProcessor()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextProcessor()
    ex.show()
    sys.exit(app.exec())
