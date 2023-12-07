from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication, QMainWindow
)
import sys

from ui_zeekify import Ui_MainWindow


replacements = {'I am': 'Thy art', 
                     'am I': 'art Thy',
                     'you are': 'thou art',
                     'You are': 'Thou art',
                     'are you': 'art thou',
                     'Are you': 'Art thou',
                     'He is': 'He beith',
                     'he is': 'he beith',
                     'Is he': 'Beith he',
                     'is he': 'beith he',
                     'Perhaps': 'Mayhaps',
                     'perhaps': 'mayhaps',
                     'Maybe': 'Mayhaps',
                     'maybe': 'mayhaps',
                     'well': 'wellith',
                     'Well': 'Wellith',
                     'It is': 'Tis',
                     'it is': 'tis',
                     'You': 'Thou',
                     'you': 'thou',
                     'Your': 'Thou',
                     'your': 'thou',
                     'I': 'Thy',
                     'Me': 'Thy',
                     'me': 'thy',
                     'my': 'thy',
                     'My': 'Thy',
                     }


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.source_text = ""
        self.converted_text = ""

        # Signals and slots

        self.ui.button_Zeekify.clicked.connect(self.zeekify)
        self.ui.button_Copy.clicked.connect(self.copy_to_clipboard)

    def zeekify(self):
        self.update_source_text
        self.converted_text = self.source_text
        
        # Zeekify
        for original, replacement in replacements.items():
            self.replace_expressions(original, replacement)

        self.ui.text_Converted.setText(self.converted_text)
        
    def replace_expressions(self, original, replacement):
        # Find the original expression and replace it with the replacement.
        self.source_text.replace(original, replacement)

    def update_source_text(self):
        self.source_text = self.ui.text_Source.toPlainText()

    def update_converted_text(self):
        self.converted_text = self.ui.text_Converted.toPlainText()

    def copy_to_clipboard(self):
        print("copying to clipboard")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
