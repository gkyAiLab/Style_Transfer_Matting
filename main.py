# -coding: utf-8-
import sys,os

from QrcodePage import QrcodePage
from ModePage import ModePage
from PhotoPage import PhotoPage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from GenerateQrcode import Gnerate_video_qrcode
from GenerateQrcode import Gnerate_picture_qrcode


class Controller():
    def __init__(self):
        pass
    def show_ModePage(self):

        self.Page1 = ModePage()
        self.Page1.switch_QrcodePage.connect(self.show_QrcodePage)
        self.Page1.switch_PhotoPage.connect(self.show_PhotoPage)
        self.Page1.show()

    def show_QrcodePage(self):
        _path = os.getcwd()
        vd_path = os.path.join(_path, 'video_buffer')  # 初始化整个缓冲区
        path=Gnerate_video_qrcode(vd_path)
        if path == False:
            self.Page3 = MessageBox()
            self.Page3.show_messagebox()
        else:
            self.Page2 = QrcodePage(path)
            self.Page2.show()

    def show_PhotoPage(self):
        _path = os.getcwd()
        ph_path = os.path.join(_path, 'photo_buffer')  # 初始化整个缓冲区
        path = Gnerate_picture_qrcode(ph_path)
        if path == False:
            self.Page3 = MessageBox()
            self.Page3.show_messagebox()
        else:
            self.Page4 = PhotoPage(path)
            self.Page4.show()

class MessageBox(QtWidgets.QMessageBox):
    def __init__(self): QtWidgets.QMessageBox.__init__(self)
    def show_messagebox(self):
        QtWidgets.QMessageBox.warning(self, "警告", "二维码生成失败", QtWidgets.QMessageBox.Cancel)

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_ModePage()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

