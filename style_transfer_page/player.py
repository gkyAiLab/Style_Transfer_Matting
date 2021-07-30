import cv2
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtGui
from player_UI import Ui_QtWidgetsApplication_hello_worldClass
from PyQt5.QtCore import QTimer
import os
import torch
import transformer
import utils

class player(QMainWindow):
    def __init__(self, cam = True):
        super(player,self).__init__()
        self.ui = Ui_QtWidgetsApplication_hello_worldClass()
        self.ui.setupUi(self)

        # Open a cam
        if cam == True:
            self.cap = cv2.VideoCapture(0)

        # Setup a QTimer
        self.cam_timer = QTimer()
        self.cam_timer.start(24)   # 24 ms
        self.cam_timer.timeout.connect(self.show_cam)  # connect show_camera

        # buffer space
        _path = os.getcwd()
        self.buffer_path = os.path.join(_path, 'buffer')
        self.buffer_image = os.path.join(self.buffer_path, 'tmp.png')

        # transfer model 
        # Device
        device = ("cuda" if torch.cuda.is_available() else "cpu")
        self.device = device

        # Load Transformer Network
        print("Loading Transformer Network")
        net = transformer.TransformerNetwork()
        style_transform_path = 'transforms/mosaic.pth'
        net.load_state_dict(torch.load(style_transform_path))
        net = net.to(device)
        self.net = net
        print("Done Loading Transformer Network")

    def read_img_from_buffer(self):
        image = cv2.imread(self.buffer_image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return img
    
    def numpy_image_to_QPixmap(self, img):
        # transfer numpy array to QImage
        width, height = self.ui.label.width(), self.ui.label.height()
        img = cv2.resize(img, (width, height))
        Qt_img = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * img.shape[2],
                                 QtGui.QImage.Format_RGB888)
        Qt_img = QtGui.QPixmap.fromImage(Qt_img)
        return Qt_img

    def save_image_to_buffer(self, image):
        cv2.imwrite(self.buffer_image, image)

    
    def read_image_from_cap(self):
        flag, img = self.cap.read()
        return img
    
    def transfer_image_style(self, img):
        # Free-up unneeded cuda memory
        torch.cuda.empty_cache()
                
        # Generate image
        content_tensor = utils.itot(img).to(self.device)
        generated_tensor = self.net(content_tensor)
        generated_image = utils.ttoi(generated_tensor.detach())
        return generated_image

    def show_cam(self):
        img = self.read_image_from_cap()

        real_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        real_img_Pixmap = self.numpy_image_to_QPixmap(real_img)

        img = self.transfer_image_style(img)  # transfer image style
        
        flag = self.save_image_to_buffer(img)  # save image
        img = self.read_img_from_buffer()  # load image
        
        Qt_img = self.numpy_image_to_QPixmap(img)  # numpy image to QPixmap image

        self.ui.label.setPixmap(real_img_Pixmap)
        self.ui.label_2.setPixmap(Qt_img)   # show image in label

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cam_player = player()
    cam_player.show()
    sys.exit(app.exec_())