# -*-  codeing = utf-8 -*-
# @Time : 2021/7/22 9:38
# @Author : Fancyicookie
# @File : GenerateQrcode.py
# @Software : PyCharm

import os
from qiniu import Auth, put_file, BucketManager, CdnManager
import qrcode
import cv2
import time
import shutil

# 云空间名称
bucket_name = 'uhd-transfer'
# 域名
domain_name = 'http://qwjpz2njs.hb-bkt.clouddn.com/'
# 需要填写你的 Access Key 和 Secret Key, 构建鉴权对象
access_key = 'QwI8i5Geoh0BJWqVUywIogNOAxjoIxkuNeh3MKoi'
secret_key = 'v_Ii9ifhrpmEdY-s79uTh-6gG2w9ovpcVM__kP2p'
# 指定上传空间，获取鉴权
q = Auth(access_key, secret_key)

video_path = os.path.join(os.getcwd(), 'video')
video_path_ori=os.path.join(os.getcwd(), 'video_ori')
if not os.path.exists(video_path_ori):
    os.makedirs(video_path_ori)


def init_upurl(fname):
    # 如果上传的视频已存在，则删除之前的上传的视频 并刷新
    # 删除
    bucket = BucketManager(q)
    bucket.delete(bucket_name, fname)
    # 刷新
    base_url = domain_name + fname
    print("baseurl:{}".format(base_url))
    cdn_manager = CdnManager(q)
    # 需要刷新的文件链接
    urls = [
        base_url
    ]
    # 刷新链接
    refresh_url_result = cdn_manager.refresh_urls(urls)
    print(refresh_url_result)

def frame2video(fps, path, fname):
    '''
    视频帧 转成 视频
    :param fps: 视频帧率
    :param path: 视频帧（图片）保存路径
    :param fname: 视频名，生成在当前路径的xx-video文件夹中
    :return: filename: 视频的完整地址 + 视频名
    '''

    # 视频编码格式设定
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # 先取第一张图片判断size
    listdir = os.listdir(path)
    file_path = os.path.join(path, listdir[0])
    img = cv2.imread(filename=file_path)
    x, y = img.shape[0:2]
    framesize = (y, x)
    print(framesize)

    
    # 将视频路径与视频名字合在一起
    filename = os.path.join(video_path_ori, fname)
    # 转换成视频
    video_writer = cv2.VideoWriter(filename=filename, fourcc=fourcc, fps=fps, frameSize=framesize)  # 图片实际尺寸，不然生成的视频会打不开

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        img = cv2.imread(filename=file_path)
        # cv2.waitKey(100)
        video_writer.write(img)
    video_writer.release()

    return filename

def video_encoder(video_path_name, video_out_name):
    '''
    视频 转码 （也许视频可以不转码）
    :param video_path_name: 视频原地址
    :param video_out_name: 转码后的视频名字
    :return: 转码后的视频地址 + 视频名
    '''
    # 获取到当前文件的目录，并检查是否有video文件夹，如果不存在则自动新建文件
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    # 转码后视频地址 + 名字
    video_outpath = os.path.join(video_path, video_out_name)
    # print(video_outpath)

    # 如果视频在本地已存在，则删除视频
    if os.path.exists(video_outpath):
        os.remove(video_outpath)

    # 将video的编码格式转为h264，否则有些编码谷歌浏览器等无法播放，例如mpeg4
    os.system('ffmpeg -i {0} -vcodec libx264 {1}'.format(video_path_name, video_outpath))

    return video_outpath

def upload(video_path_name, fname):
    """
    上传视频，视频的本地地址，所以就是上面函数给的视频帧生成的视频地址; 以及上传到云空间的视频名字
    """
    # 生成上传 Token，可以指定过期时间等, 默认是3600秒
    token = q.upload_token(bucket_name)
    # 上传，fname为视频名称
    put_file(token, fname, video_path_name, version='v2')

def save_qrcode(qrcode_name, fname):
    '''
    将 下载播放的链接 生成二维码图片
    :param qrcode_name: 生成的二维码命名
    :param fname: 视频名称
    :return:
    '''
    base_url = domain_name + fname
    print(base_url)
    # 生成二维码
    qrcode_img = qrcode.make(base_url)

    # 保存二维码的文件路径
    qrcode_path = os.path.join(os.getcwd(), 'qrcode')
     # 如果该二维码路径已经存在本地，则删除本地的二维码图片
    if os.path.exists(qrcode_path):
        shutil.rmtree(qrcode_path)
        # os.remove(qrcode_path)

    if not os.path.exists(qrcode_path):
        os.makedirs(qrcode_path)
    # 二维码保存在本地的完整路径
    save_qrcode_path = os.path.join(qrcode_path, qrcode_name)
    # # 如果该二维码路径已经存在本地，则删除本地的二维码图片
    # if os.path.exists(qrcode_path):
    #     os.remove(qrcode_path)
    # 重新保存二维码保存，可以在save_qrcode_path看到二维码图片
    qrcode_img.save(save_qrcode_path)

    return save_qrcode_path

def Gnerate_video_qrcode(path):
    '''
    生成 二维码
    :param path: 视频帧保存的地址
    key: 视频名
    :return: 二维码的本地路径
    '''
    #delete video_file_name???
    if os.path.exists(video_path):
        shutil.rmtree(video_path)
    
    if filecheck(path) != 'nofile':
        # 视频文件名
        fname = 'video.mp4'

        # 视频帧转成本地视频，video_path_name为视频路径+视频名
        video_path_name = frame2video(12, path, fname)

        # 本地视频转码
        a = int(time.time())
        c = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(a))
        print(c)
        video_out_name = 'video' + str(c) + '.mp4'
        video_path0 = video_encoder(video_path_name, video_out_name)

        # 上传视频
        upload(video_path0, video_out_name)

        # 生成二维码图片名称
        # qrcode_name = 'qrcode_out.png'
        qrcode_name='qrcode' + str(c) + '.png'
        save_qrcode_video = save_qrcode(qrcode_name, video_out_name)
        print(save_qrcode_video)
        # save_qrcode = []
        # save_qrcode = save_qrcode.append(save_qrcode_path)

        return save_qrcode_video
    else:
        return False

def Gnerate_picture_qrcode(path):

    if filecheck(path) != 'nofile':
    # 照片文件名
        fname = 'photocut.png'
        picture_path = os.path.join(path, fname)

        a = int(time.time())
        c = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(a))
        # 上传图片
        picture_out_name = 'picture' + str(c) + '.png'
        upload(picture_path, picture_out_name)

        
        qrcode_name='qrcode' + str(c) + '.png'
        save_qrcode_picture = save_qrcode(qrcode_name, picture_out_name)
        print(save_qrcode_picture)
    else:
        return False
    return save_qrcode_picture


def filecheck(path):
    filenum = len(os.listdir(path))  # 获得path目录下所有文件的数量
    if filenum == 0:
        # print("there is no file")
        return 'nofile'

if __name__ == '__main__':
    # path = r'E:\video_picture\video'
    # video_path1 = r'E:\video_picture\video_frame'
    picture_path = r'E:\video_picture\picture'
    # path = r'E:\PycharmProjects\style-transfer\style-transfer-main\style_transfer_page\vidoe_buffer'
    # Gnerate_video_qrcode(video_path1)
    Gnerate_picture_qrcode(picture_path)




