import sys,os
from PyQt5 import QtGui
from PyQt5.Qt import *
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QIcon,QFont, QImage)
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtPrintSupport import QPrinter

class PhotoPage(QWidget):

    def __init__(self,path):
        super().__init__()

        os.getcwd()  
        photo_path_ = os.path.join(os.getcwd(),'photo_buffer')
        self.photo_path = os.path.join(photo_path_,'preview.png')

        self.ph_qr_path = path

        self.photo = QImage()
        self.photo.load(self.photo_path)

        self.initUI()

    def initUI(self):
        #设置字体
        QPushButton.setFont(self,QFont('宋体',12,60))
        QToolTip.setFont(QFont('仿宋', 10))#提示框字题

        # 设置窗口参数
        self.resize(1000,500)
        self.center()
        self.setWindowTitle('请扫描二维码')
        logo = os.path.join('src', 'abs.png')
        self.setWindowIcon(QIcon(logo))

        #背景设置
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(logo)))
        self.setPalette(self.palette)

        self.btn_print = QPushButton('Print!')
        self.btn_print.setFixedSize(QSize(250,35))
        self.btn_print.clicked.connect(self.btn_print_clicked)

        #设置label
        self.label1 = QLabel()
        self.label1.setFixedSize(QSize(640,360))
        self.QrImage= QPixmap(self.photo_path)
        self.label1.setPixmap(self.QrImage)

        self.label2 = QLabel()
        self.label2.setFixedSize(QSize(450,450))
        self.QrImage= QPixmap(self.ph_qr_path)
        self.label2.setPixmap(self.QrImage)

        self._layout_main = QHBoxLayout()
        self._layout_main.addWidget(self.label1,0,Qt.AlignCenter)
        self._layout_main.addStretch(1)
        self._layout_main.addWidget(self.label2,0,Qt.AlignCenter)

        self._layout_=QVBoxLayout()
        self._layout_.addLayout(self._layout_main)
        self._layout_.addStretch(1)
        self._layout_.addWidget(self.btn_print,0,Qt.AlignCenter)

        self.setLayout(self._layout_)

    #窗口相对屏幕居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def btn_print_clicked(self):
        printer = QPrinter()
        painter= QtGui.QPainter(printer)
        #实例化视图窗口
        rect=painter.viewport()
        #获取图片的尺寸
        size=self.photo.size()

        size.scale(rect.size(),Qt.KeepAspectRatio)
        #设置视图窗口的属性
        painter.setViewport(rect.x(),rect.y(),size.width(),size.height())

        #设置窗口的大小为图片的尺寸，并在窗口内绘制图片
        painter.setWindow(0,0,size.width(),size.height())
        painter.drawImage(0,0,self.photo)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhotoPage()
    ex.show()
    sys.exit(app.exec_())