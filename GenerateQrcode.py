# -*-coding:utf-8-*-

"""============================================
    Time   : 2021/7/28  10:05 上午
    Author : Xiaoying Bai
    Brief  :
============================================"""
from qiniu import Auth, put_file, CdnManager, BucketManager
import os
import cv2
import qrcode

class Generate_Qrcode():
    def __init__(self, num):
        url_num = ['video_0.mp4', 'video_1.mp4']

        access_key = 'MUICwt2o0zFJrpP7huPW6dXOaK7KJ0HLMgXx34xG'  # 七牛云密钥
        secret_key = 'OSxUQ5PG1JSbN6_Y7Zd2qCNM3WZ9Z17OdCqnrFoo'  # 七牛云密钥

        q = Auth(access_key=access_key, secret_key=secret_key)  # 初始化对接
        bucket_name = 'neural-style-transfer'  # 上传的七牛云空间名称
        self.key = url_num[num]  # 上传后保存的文件名
        key_1 = url_num[1-num]  # 刷新的那个文件名
        self.token = q.upload_token(bucket_name, self.key)  # 生成上传token

        domain_name = 'http://qwjn3oc8w.hb-bkt.clouddn.com/'  # 七牛云空间域名
        self.base_url = domain_name + self.key  # 文件链接
        base_url_1 = domain_name + key_1  # 文件链接

        bucket = BucketManager(q)
        bucket.delete(bucket_name, self.key)  # 删除云上文件

        cdn_manager = CdnManager(q)  # cdn管理
        url_refresh = [base_url_1]  # 需要刷新的文件链接
        stat=cdn_manager.refresh_urls(url_refresh)  # 刷新cdn缓存
        print(type(stat))
        # self.Generateqrcode(imgdir, fps)

    def Generateqrcode(self, imgdir, fps):
        if self.filecheck(imgdir) != 'nofile':
            videodir = './neural_style_transfer.mp4'
            # videodir ='/media/test/8026ac84-a5ee-466b-affa-f8c81a423d9b/zq/style-transfer_v1/neural_style_transfer.mp4'
            self.png2mp4(imgdir, fps, videodir)  # 图片转视频

            put_file(self.token, self.key, videodir)  # 上传文件

            qrcode_path = os.path.join(os.getcwd(), "qrcode.png")

            if os.path.exists("./qrcode.png"):  # 若本地已有二维码图片，则将其删除
                os.remove(qrcode_path)

            img = qrcode.make(self.base_url)  # 生成二维码
            img.save("./qrcode.png")  # 保存二维码图片


            return qrcode_path
        else:
            return False

    def filecheck(self, imgdir):
        filenum = len(os.listdir(imgdir))  # 获得imgdir目录下所有文件的数量
        if filenum == 0:
            # print("there is no file")
            return 'nofile'


    def png2mp4(self, imgdir, fps, videodir):
        all_files = sorted(os.listdir(imgdir))  # 获得imgdir目录下所有图片的名字并排序

        if os.path.exists(videodir):  # 删掉历史文件（否则代码会询问是否覆盖）
            os.remove(videodir)

        img = cv2.imread(os.path.join(imgdir, all_files[2]))  # 读取第3张图片 （保险起见，万一第一张是隐藏文件）
        sp = img.shape  # 获得图片的size [0]:宽，[1]:长，[2]:通道
        # fourcc = cv2.VideoWriter_fourcc(*'avc1')
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        videodir0='123.avi'
        video_writer = cv2.VideoWriter(filename=videodir0, fourcc=fourcc, fps=fps, frameSize=(sp[1], sp[0]))  # 设置生成视频文件名称为vid.mp4；

        for i in all_files:
            if i[-3:] != 'png':  # 如果不是图片，就跳出本轮循环
                continue
            if os.path.exists(os.path.join(imgdir, i)):  # 判断图片是否存在
                img = cv2.imread(os.path.join(imgdir, i))  # 读取图片
                # cv2.waitKey(100)  # 延时保证读取图片成功
                video_writer.write(img)
        
        video_writer.release()
        os.system('ffmpeg -i {0} -vcodec libx264 {1}'.format(videodir0,videodir))

if __name__ == '__main__':

    # path = r'D:\interface\style_transfer_page\video_buffer'
    path ='./'
    num = 0
    # path = r'E:\video_picture\video'
    # path = r'E:\video_picture\video_frame1'
    # path = r'E:\PycharmProjects\style-transfer\style-transfer-main\style_transfer_page\vidoe_buffer'
    # print(img_qrcode(path, 5, num))
    aa = Generate_Qrcode(num)
    print(aa.Generateqrcode(imgdir=path, fps=5))
