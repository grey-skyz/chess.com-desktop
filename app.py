import sys
import time
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from pypresence import Presence

class ChessApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess.com")
        self.setGeometry(100, 100, 1200, 800)

        self.discord_client_id = "1314686685648523336"
        self.rpc = Presence(self.discord_client_id)
        self.rpc.connect()
        self.update_discord_presence()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.chess.com"))
        layout.addWidget(self.browser)

    def update_discord_presence(self):
        self.rpc.update(
            state="Playing Chess.com",
            start=time.time(),
        )

    def closeEvent(self, event):
        self.rpc.close()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessApp()
    window.show()
    sys.exit(app.exec())
