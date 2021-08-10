# -coding: utf-8-
import sys,os

from QrcodePage import QrcodePage
from ModePage import ModePage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from GenerateQrcode import Gnerate_qrcode


class Controller():
    def __init__(self):
        self.qr_num =0
        pass
    def show_ModePage(self):

        self.Page1 = ModePage()
        self.Page1.switch_QrcodePage.connect(self.show_QrcodePage)
        self.Page1.show()

    def show_QrcodePage(self):
        _path = os.getcwd()
        vd_path = os.path.join(_path, 'video_buffer')  # 初始化整个缓冲区
        # self.buffer_video_buffer = os.path.join(self.buffer, "video_buffer")  # 初始化视频帧缓冲区

        # if self.qr_num == 0:
        #     self._Qr = Gnerate_qrcode(0)
        #     self.qr_num += 1
        # else:
        #     self._Qr = Gnerate_qrcode(1)
        #     self.qr_num -= 1
        path=Gnerate_qrcode(vd_path)
        if path == False:
            self.Page3 = MessageBox()
            self.Page3.show_messagebox()
        else:
            self.Page2 = QrcodePage(path)
            self.Page2.show()

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

