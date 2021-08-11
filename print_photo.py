import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QSizePolicy,QAction
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter
from PyQt5.QtGui import QImage,QIcon,QPixmap,QPainter
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self,parent=None):
    super(MainWindow, self).__init__(parent)

    #设置标题
    self.setWindowTitle('打印图片')

    #创建标签，设置标签的大小规则以及控件的位置居中
    self.imageLabel=QLabel()
    self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
    self.setCentralWidget(self.imageLabel)

    #实例化Qimage类
    self.image = QImage()
    #自定义的多个函数，实现的功能不一
    self.createActions()
    # self.createMenus() #父菜单
    self.createToolBars()

    if self.image.load('./photo_buffer/preview.png'):
      self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
      self.resize(self.image.width(),self.image.height())

  def createActions(self):
    #加载图标，添加快捷方式，添加提示信息，绑定槽函数
    self.PrintAction=QAction(self.tr('打印'),self)
    self.PrintAction.setShortcut('Ctrl+P')
    self.PrintAction.setStatusTip(self.tr('打印'))
    self.PrintAction.triggered.connect(self.slotPrint)
  def createMenus(self):
    #实例化菜单栏，并添加一个父菜单，以及把PrintAction添加到父菜单下
    PrintMenu=self.menuBar().addMenu(self.tr('打印'))
    PrintMenu.addAction(self.PrintAction)

  def createToolBars(self):
    #在工具栏区域内添加控件printACtion
    fileToolBar=self.addToolBar('Print')
    fileToolBar.addAction(self.PrintAction)

  def slotPrint(self):
    #实例化打印图像对象
    printer=QPrinter()
    # #打印窗口弹出
    # printDialog=QPrintDialog(printer,self)
    # if printDialog.exec_():

    painter=QPainter(printer)
    #实例化视图窗口
    rect=painter.viewport()
    #获取图片的尺寸
    size=self.image.size()

    size.scale(rect.size(),Qt.KeepAspectRatio)
    #设置视图窗口的属性
    painter.setViewport(rect.x(),rect.y(),size.width(),size.height())

    #设置窗口的大小为图片的尺寸，并在窗口内绘制图片
    painter.setWindow(0,0,size.width(),size.height())
    painter.drawImage(0,0,self.image)
    painter.end()

if __name__ == '__main__':
  app=QApplication(sys.argv)
  main=MainWindow()
  main.show()
  sys.exit(app.exec_())