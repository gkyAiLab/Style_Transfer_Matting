import sys
import cv2
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QIcon,QFont)
# from style_transfer_page import transformer
from matting import transformer
from matting import utils
import torch
import os

####
from matting import *
from matting.stylematting import * 
from PyQt5.QtCore import QTimer,QEventLoop
from PyQt5 import *
from PIL import Image

# # import onnx
# import torch.onnx 
# import onnxruntime 


class ModePage(QWidget):
    switch_style1 = QtCore.pyqtSignal()  # 跳转信号
    switch_style2 = QtCore.pyqtSignal()  # 跳转信号
    switch_style3 = QtCore.pyqtSignal()  # 跳转信号
    switch_QrcodePage = QtCore.pyqtSignal()#跳转信号

    def __init__(self,parent=None):
        super().__init__(parent)
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.initUI()
        self.slot_init()
        
        self.with_recording = False # 录制的记录信号
        self.recording_index = 0 # 记录录制的视频帧下标
        
        self.model_mat='0'
        self.stat_mat='0'
        self.input=None
        self.route="./matting/transforms/mosaic.pth"

    def initUI(self):
        #设置窗口参数
        self.resize(1200,900)
        self.center()
        self.setWindowTitle('风格迁移')
        logo = os.path.join('src', 'abs.png')
        logo_s1=os.path.join('src', 'city.jpg')
        logo_s2=os.path.join('src', 'qingming.jpg')
        logo_s3=os.path.join('src', 'fuzi.jpg')

        logo_b1=os.path.join('src', 'abs.png')
        logo_b2=os.path.join('src', 'b2.jpg')
        logo_b3=os.path.join('src', 'mosaic.jpg')
        self.setWindowIcon(QIcon(logo))

        self.label_camera = QLabel()  # 定义显示视频的Label
        self.label_camera.setFixedSize(1080, 820)  # 给显示视频的Label设置大小为641x481

        self.label_counter = QLabel()  # 定义显示倒数器的Label
        self.label_counter.setVisible(False)
        self.label_counter.setFixedSize(1080,820)
        self.label_counter.setText("3")
        self.label_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_counter.setStyleSheet("font-size: 102px;")

        self.style_cb = QComboBox() #定义下拉框
        self.style_cb.setFixedSize(250,35)
        self.style_cb.setIconSize(QSize(100,100))
        self.style_cb.addItem(QIcon(logo),'no风格')
        self.style_cb.addItem(QIcon(logo_s1),'风格1')
        self.style_cb.addItem(QIcon(logo_s2),'风格2')
        self.style_cb.addItem(QIcon(logo_s3),'风格3')

        self.background_cb = QComboBox()  # 定义下拉框
        self.background_cb.setVisible(False)
        self.background_cb.setFixedSize(250, 35)
        self.background_cb.setIconSize(QSize(100,100))
        self.background_cb.addItem(QIcon(logo), 'no背景')
        self.background_cb.addItem(QIcon(logo_b1), '背景1')
        self.background_cb.addItem(QIcon(logo_b2), '背景2')
        self.background_cb.addItem(QIcon(logo_b3), '背景3')

        self.btn_cutout = QPushButton('开始')
        self.btn_cutout.setFixedSize(250, 35)

        self.btn_record = QPushButton('开始录制')
        self.btn_record.setFixedSize(250, 35)

        self._layout_1 = QVBoxLayout()  # 布局1
        self._layout_1.addStretch(3)
        self._layout_1.addWidget(self.btn_record)
        self._layout_1.addStretch(2)
        self._layout_1.addWidget(self.btn_cutout)
        self._layout_1.addStretch(1)
        self._layout_1.addWidget(self.background_cb)
        self._layout_1.addStretch(3)

        self._layout_2 = QVBoxLayout() #布局2
        self._layout_2.addStretch(1)
        self._layout_2.addWidget(self.style_cb,0,QtCore.Qt.AlignCenter)
        self._layout_2.addWidget(self.label_camera)
        self._layout_2.addWidget(self.label_counter)
        self._layout_2.addStretch(1)

        self._layout_main = QHBoxLayout()  # 总布局
        self._layout_main.addLayout(self._layout_1)
        self._layout_main.addStretch(1)
        self._layout_main.addLayout(self._layout_2)
        self._layout_main.addStretch(1)

        self.setLayout(self._layout_main)  # 到这步才会显示所有控件

    # 窗口相对屏幕居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 整体初始化
    def slot_init(self):
        self.stat='0'
        # self.path='mosaic.pth'
        self.route="./matting/transforms/mosaic.pth"
        self.style_type=None
        self.transfer_init()
        self.open_camera()
        # self.bgmModel_load()
        BGModel.reload(self)
        matting_model.preload_init(self) 
        self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()
        self.btn_cutout.clicked.connect(self.btn_cutout_clicked)
        self.style_cb.currentIndexChanged.connect(self.switch_style)
        self.background_cb.currentIndexChanged.connect(self.switch_background)

        self.btn_record.clicked.connect(self.btn_record_clicked)

    # 点击开始录制
    def btn_record_clicked(self):
        if int(self.label_counter.text()) == 3:
            self.btn_record.setText('结束录制')
            self.label_camera.setVisible(False)
            self.label_counter.setVisible(True)
            if int(self.time_counter()) == 0:
                self.label_counter.setVisible(False)
                self.label_camera.setVisible(True)
                self.recording_init()
        else:
            self.btn_record.setText('开始录制')
            self.label_counter.setVisible(False)
            self.label_camera.setVisible(True)
            self.recording_end()
            self.label_counter.setText('3')
        if self.recording_index == -1 and self.with_recording == False:
            self.switch_QrcodePage.emit()
        else:
            print('生成二维码失败!')

    def time_counter(self):
        counter_time = int(self.label_counter.text())
        count = 0
        while counter_time >= count:
            count_now = counter_time - count
            self.label_counter.setText(str(count_now))
            QApplication.processEvents()
            time.sleep(1)
            count += 1
        return count_now

    def recording_init(self):
        self.with_recording = True
        self.recording_index = 0
        
        # 重新初始化一次，删除之前保存的视频帧
        file_list = os.listdir(self.buffer_video_buffer)

        for file in file_list:
            frame = os.path.join(self.buffer_video_buffer, file)
            if os.path.exists(frame):
                os.remove(frame)

    def recording_end(self): # 结束录制
        self.with_recording = False
        self.recording_index = -1

    def switch_background(self):
        if self.background_cb.currentText() == '背景1':
            print('background1 clicked')
            self.stat_mat='1'
            self.input='video'
            self.model_mat='1'
            self.style_change=True
            
        elif self.background_cb.currentText() == '背景2':
            print('background2 clicked')
            self.stat_mat='2'
            self.input='img'
            self.model_mat='1'
            self.style_change=True

        elif self.background_cb.currentText() == '背景3':
            print('background3 clicked')
            self.stat_mat='3'
            self.input='style'
            self.model_mat='1'
            self.style_change=True

        elif self.background_cb.currentText() == 'no背景':
            print('nobackground clicked')
            self.stat_mat='0'
            self.model_mat='0'
            self.style_change=True

    def switch_style(self):
        if self.style_cb.currentText() == '风格1':
            print('style1 clicked')
            self.stat='style1'
            # self.path='city.pth'
            self.style_type='1'
            self.route="./matting/transforms/mosaic.pth"
            self.style_change=True

        elif self.style_cb.currentText() == '风格2':
            print('style2 clicked')
            self.stat='style2'
            # self.path='star2.pth'
            self.style_type='2'
            self.route="./matting/transforms/qingming.pth"
            self.style_change=True

        elif self.style_cb.currentText() == '风格3':
            print('style3 clicked')
            self.stat='style3'
            # self.path='fuzi.pth'
            self.style_type='3'
            self.route="./matting/transforms/fuzi.pth"
            self.style_change=True

        elif self.style_cb.currentText() == 'no风格':
            print('no style1 clicked')
            # self.stat_mat='10'
            self.style_type=None
            self.stat='0'
            self.style_change=True

    # 点击抠图按钮
    def btn_cutout_clicked(self):
        print('btn_cutout clicked')
        if self.background_cb.isVisible() == True:
            self.btn_cutout.setText('开始')
            self.background_cb.setVisible(False)
            self.model_mat='0'

            
            self.transfer_init()
        else:
            self.btn_cutout.setText('byebye')
            self.background_cb.setVisible(True)

            self.matting(self.image) #init
            self.init_image=self.image
    
    def mat_style(self,input,style_type):
    
        flag, self.image = self.cap.read()  # 从视频流中读取 
        self.image = matting_model.matting_step(self,self.image,input,style_type)  #matting

        return self.image

    def cam_init(self,image):
        # flag = self.save_image_to_buffer(image)  # save image
        # img = self.read_img_from_buffer()  # load image
        # return img
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    def matting(self,image):
        img=matting_model.matting_step1(self,image,style_type=self.style_type)
        # flag = self.save_image_to_buffer(img)  # save image
        # img = self.read_img_from_buffer()  # load image
        return img
    
    # def matting_choose(self,image,input,style_type,stat):
    #     img=matting_model.matting_step(self,image=image,input=input,style_type=style_type,stat=stat)
        
    #     # norm_img=cv2.normalize(img,None,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_32F)
    #     # print(norm_img)
    #     # norm_img.astype(np.uint8)

    #     # flag = self.save_image_to_buffer(img)  # save image
    #     # img = self.read_img_from_buffer()  # load image
    #     return img

    def transfer_init(self):
        _path = os.getcwd()
        self.buffer = os.path.join(_path, './')  # 初始化整个缓冲区

        self.buffer_video_buffer = os.path.join(self.buffer, "video_buffer")  # 初始化视频帧缓冲区
        if not os.path.exists(self.buffer_video_buffer):
            os.mkdir(self.buffer_video_buffer)

        # self.buffer_video = os.path.join(self.buffer, "vidoe")
        # if not os.path.exists(self.buffer_video):  # 保存最终的录制的视频
        #     os.mkdir(self.buffer_video)
        
        # self.transfer_models_path = os.path.join(self.buffer, 'transforms')

        # self.buffer_image = os.path.join(self.buffer, 'buffer')
        # self.buffer_image = os.path.join(self.buffer_image, 'tmp.png')




    # def preload_init(self):
    #     # define transfer model
    #     device = ("cuda" if torch.cuda.is_available() else "cpu")
    #     self.device = device
    #     # style_transform_path = os.path.join(self.transfer_models_path, self.path)
    #     style_transform_path= self.route
    #     net = transformer.TransformerNetwork()
    #     net.load_state_dict(torch.load(style_transform_path))
    #     net = net.to(device)
    #     self.net = net
    #     self.style_change=False

    def open_camera(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确",buttons=QtWidgets.QMessageBox.Ok)
                print(msg)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
        else:
            self.close_camera()

    def close_camera(self):
        self.timer_camera.stop()  # 关闭定时器
        self.cap.release()  # 释放视频流

    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取
        if(self.model_mat=='0'):
            t=time.time()
            if (self.stat=='style1' or self.stat=='style2' or self.stat=='style3'):
                if(self.style_change):
                    matting_model.preload_init(self) # style reload
                    print("number load style!alllllllllllllllllllllll")
                self.image = self._get_image(self.image)  # 风格迁移转换
            if(self.stat=='0'):
                self.image = self.cam_init(self.image)
            t2=time.time()
            print("stylestylestylestyle",t2-t)
            
        elif(self.model_mat=='1'):
            t=time.time()

            if (self.stat_mat=='1'):
                self.image =self.mat_style(self.input,style_type= self.style_type)
            elif (self.stat_mat=='2'):
                self.image =self.mat_style(self.input,style_type= self.style_type)
            elif (self.stat_mat=='3'):
                self.image =self.mat_style(self.input,style_type= None)
            # elif (self.stat=='style1' or self.stat=='style2' or self.stat=='style3'):
            #     self.image =self.mat_style(input="video",style_type= self.style_type)
            t2=time.time()
            print(t2-t,"##############################")
            

        if self.with_recording:
            self.recording(self.image)

        width, height = self.label_camera.width(), self.label_camera.height()
        show = cv2.resize(self.image, (width, height))  # 把读到的帧的大小重新设置
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式

        self.label_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里显示QImage


    def bgmModel_load(self):
        args = load_args()
        self.bgmModel = BGModel(args.model_checkpoint, args.model_backbone_scale, args.model_refine_mode,
                       args.model_refine_sample_pixels, args.model_refine_threshold)
        self.bgmModel.reload()

    # def transfer_image_style(self, img):
    #     # img = cv2.flip(img, 1)

    #     # Free-up unneeded cuda memory
    #     torch.cuda.empty_cache()
                
    #     # Generate image
    #     content_tensor = utils.itot(img).to(self.device)

    #     # normal
    #     generated_tensor = self.net(content_tensor)
       
    #     generated_image = utils.ttoi(generated_tensor.detach())
    #     return generated_image
        
    #     # # onnx
    #     # t=time.time()
    #     # # onnx_model = onnx.load("./fast_neural_style.onnx")
    #     # # onnx.checker.check_model(onnx_model)

    #     # ort_session = onnxruntime.InferenceSession("fast_neural_style.onnx")
    #     # ortvalue = onnxruntime.OrtValue.ortvalue_from_numpy(content_tensor, 'cuda', 0)
        
    #     # def to_numpy(tensor):
    #     #     return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()
        
    #     # ort_inputs = {ort_session.get_inputs()[0].name: ortvalue}
    #     # ort_outs = ort_session.run(None, ort_inputs)


    #     # # ort_session = onnxruntime.InferenceSession("./fast_neural_style.onnx")

    #     # # ort_inputs = {ort_session.get_inputs()[0].name: self.to_numpy(content_tensor)}
    #     # # ort_outs = ort_session.run(None, ort_inputs)
    #     # generated_tensor = ort_outs[0]
        
    #     # generated_tensor = generated_tensor.squeeze()
    #     # generated_image = generated_tensor.transpose(1, 2, 0)
    #     # t2=time.time()
    #     # print("________",t2-t,onnxruntime.get_device(),"&&&&&&&&&&&&&&&&")
    #     # return generated_image

    # def to_numpy(self,tensor):

    #     return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

    # def save_image_to_buffer(self, image):
    #     cv2.imwrite(self.buffer_image, image)
    
    # def read_img_from_buffer(self):
    #     image = cv2.imread(self.buffer_image)
    #     img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     return img

    def _get_image(self, image):
        img = matting_model.transfer_image_style(self,image)  # tranfer style
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB).clip(0,255)
        norm_img=img.astype(np.uint8)
        return norm_img
        
    def recording(self, image):  # 根据下标保存视频帧
        frame_name = "{:08d}.png".format(self.recording_index)
        frame_name = os.path.join(self.buffer_video_buffer, frame_name)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(frame_name, image)
        self.recording_index += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModePage()
    ex.show()
    sys.exit(app.exec_())