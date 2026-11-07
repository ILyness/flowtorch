"""Desktop application entry point."""

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


def main() -> None:
    """Launch the FlowTorch desktop application."""
    app = QApplication.instance() or QApplication([])
    window = QMainWindow()
    window.setWindowTitle("FlowTorch")
    window.setCentralWidget(QLabel("Model design workspace"))
    window.resize(960, 640)
    window.show()
    app.exec()
