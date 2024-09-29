import sys
import string
import random
import pyperclip
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QCheckBox, QPushButton, QSpinBox, QTextEdit
)
from PyQt5.QtCore import Qt

# Function to generate password
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_characters = lower + upper + digits + symbols
    if not all_characters:
        return ""
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# PyQt GUI Application
class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Random Password Generator')
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        # Password Length
        length_layout = QHBoxLayout()
        length_label = QLabel('Password Length:')
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 64)
        self.length_spinbox.setValue(10)
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_spinbox)
        
        # Checkbox options
        self.uppercase_checkbox = QCheckBox('Include Uppercase Letters')
        self.numbers_checkbox = QCheckBox('Include Numbers')
        self.symbols_checkbox = QCheckBox('Include Symbols')
        
        # Generate Button
        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)
        
        # Text Edit to display the generated password
        self.password_display = QTextEdit()
        self.password_display.setReadOnly(True)
        
        # Copy Button
        self.copy_button = QPushButton('Copy to Clipboard')
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        
        # Add widgets to layout
        layout.addLayout(length_layout)
        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.numbers_checkbox)
        layout.addWidget(self.symbols_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_display)
        layout.addWidget(self.copy_button)
        
        self.setLayout(layout)
    
    def generate_password(self):
        length = self.length_spinbox.value()
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_numbers = self.numbers_checkbox.isChecked()
        use_symbols = self.symbols_checkbox.isChecked()
        
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        self.password_display.setText(password)
    
    def copy_to_clipboard(self):
        password = self.password_display.toPlainText()
        if password:
            pyperclip.copy(password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
