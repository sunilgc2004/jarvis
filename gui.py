from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class JarvisGUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TECH VENTURE JARVIS")
        self.setGeometry(100, 100, 1200, 700)

        self.setStyleSheet("background-color: black;")

        label = QLabel(self)
        label.setGeometry(0, 0, 1200, 700)

        movie = QMovie("assets/jarvis.gif")
        label.setMovie(movie)

        movie.start()

        text = QLabel("TECH VENTURE AI ASSISTANT", self)

        text.setStyleSheet("""
            color: cyan;
            font-size: 30px;
            font-weight: bold;
        """)

        text.move(350, 20)

app = QApplication(sys.argv)

window = JarvisGUI()

window.show()

sys.exit(app.exec_())