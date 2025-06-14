import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        try:
            key = int(self.ui.txt_key.toPlainText())  # Sửa .text() thành .toPlainText()
        except ValueError:
            QMessageBox.critical(self, "Error", "Key must be a number")
            return
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": key
        }
        print(f"Sending payload: {payload}")  # Debug
        try:
            response = requests.post(url, json=payload)
            print(f"Response статус: {response.status_code}, Content: {response.text}")  # Debug
            if response.status_code == 200:
                data = response.json()
                if "encrypted_message" in data:
                    self.ui.txt_cipher_text.setText(data["encrypted_message"])
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Encrypted Successfully")
                    msg.exec_()
                else:
                    print("Error: 'encrypted_message' not found in response")
            else:
                print(f"Error: API returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            
    def call_api_decrypt(self):
        try:
            key = int(self.ui.txt_key.toPlainText())  # Sửa .text() thành .toPlainText()
        except ValueError:
            QMessageBox.critical(self, "Error", "Key must be a number")
            return
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": key
        }
        print(f"Sending payload: {payload}")  # Debug
        try:
            response = requests.post(url, json=payload)
            print(f"Response статус: {response.status_code}, Content: {response.text}")  # Debug
            if response.status_code == 200:
                data = response.json()
                if "decrypted_message" in data:
                    self.ui.txt_plain_text.setText(data["decrypted_message"])
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decrypted Successfully")
                    msg.exec_()
                else:
                    print("Error: 'decrypted_message' not found in response")
            else:
                print(f"Error: API returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())