import sys,os
from PyQt5.Qt import *
from PyQt5.QtGui import (QIcon,QFont)

class QrcodePage(QWidget):

    def __init__(self):
        super().__init__()

        os.getcwd()
        # qr_path_ = os.path.join(os.getcwd(),'qrcode')
        self.qr_path = os.path.join(os.getcwd(),'qrcode.png')

        self.initUI()

    def initUI(self):
        #设置字体
        QPushButton.setFont(self,QFont('宋体',12,60))
        QToolTip.setFont(QFont('仿宋', 10))#提示框字题

        # 设置窗口参数
        self.resize(600,800)
        self.center()
        self.setWindowTitle('请扫描二维码')
        logo = os.path.join('src', 'abs.png')
        self.setWindowIcon(QIcon(logo))

        #背景设置
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(logo)))
        self.setPalette(self.palette)

        #设置label
        self.label1 = QLabel()
        self.label1.setFixedSize(QSize(410,410))
        self.QrImage= QPixmap(self.qr_path)
        self.label1.setPixmap(self.QrImage)

        self._layout_main = QVBoxLayout()
        self._layout_main.addStretch(1)
        self._layout_main.addWidget(self.label1,0,Qt.AlignCenter)
        self._layout_main.addStretch(1)

        self.setLayout(self._layout_main)

    #窗口相对屏幕居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QrcodePage()
    ex.show()
    sys.exit(app.exec_())