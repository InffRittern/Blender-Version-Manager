import sys

from PyQt5.QtWidgets import QApplication

from main_window import B3dVersionMangerMainWindow


def main():
    QApplication.setApplicationName("Blender Version Manager")
    QApplication.setApplicationVersion('1.0.2')

    app = QApplication(sys.argv)
    window = B3dVersionMangerMainWindow(app)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
