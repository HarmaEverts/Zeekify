from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication, QMainWindow
)
import sys

from ui_zeekify import Ui_MainWindow
from nltk.corpus import wordnet as wn


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
        self.ui.text_Source.textChanged.connect(self.update_source_text)

    def zeekify(self):
        self.update_source_text
        self.converted_text = self.source_text
        
        # Zeekify
        for original, replacement in replacements.items():
            self.converted_text = self.replace_expressions(original, replacement)

        self.replace_verbs()

        self.ui.text_Converted.setText(self.converted_text)
        
    def replace_expressions(self, original, replacement):
        # Find the original expression and replace it with the replacement.
        result = self.converted_text.replace(original, replacement)
        return result

    def replace_verbs(self):
        # Add each word in the converted_text to a list.
        words = self.converted_text.split()
        for w in words:
            tmp = wn.synsets(w)[0].pos()
            if tmp == 'v':
                if tmp[-1] == 'e':
                    tmp[-1] = 'ith'
                else:
                    tmp = tmp + 'ith'
        self.converted_text = " ".join(words)

    def update_source_text(self):
        self.source_text = self.ui.text_Source.toPlainText()

    def update_converted_text(self):
        self.converted_text = self.ui.text_Converted.toPlainText()

    def copy_to_clipboard(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.converted_text, mode=cb.Clipboard)
        # Text is now already in the clipboard, no need for further actions.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
