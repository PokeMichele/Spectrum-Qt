import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0 ,0 , 800, 600)
        self.setWindowTitle("Spectrum-Qt")
        self.setWindowIcon(QIcon("icon.png"))

        # Create the first entry field
        self.entry_path = QLineEdit()
        self.entry_path.setPlaceholderText("File Path (Without File Extension)")

        # Create the second entry field
        self.entry_mode = QLineEdit()
        self.entry_mode.setPlaceholderText("Mode ('single' or 'dual' - Default: dual)")

        # Create the terminal
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)

        # Create the Button
        btn_run_script = QPushButton("Run")
        btn_run_script.clicked.connect(self.run_script)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.entry_path)
        layout.addWidget(self.entry_mode)
        layout.addWidget(self.terminal)
        layout.addWidget(btn_run_script)

        # Create the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

    def run_script(self):
        path = self.entry_path.text()
        mode = self.entry_mode.text()
        if mode.lower() == "single":
            mode = "single"
        elif mode.lower() == "dual":
            mode = "dual"
        else:
            mode = "dual"
        process = subprocess.Popen(["./create.sh", path, mode, "full", path+"_spectrum.mp4"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.terminal.append(f"stdout: {stdout.decode()}")
        self.terminal.append(f"stderr: {stderr.decode()}")

        # Delete the Video file created w/o Audio
        if os.path.exists(path + "_spec.mp4"):
            os.remove(path + "_spec.mp4")
        else:
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

