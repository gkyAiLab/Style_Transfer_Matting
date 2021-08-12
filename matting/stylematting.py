"""
Videoconferencing plugin demo for Linux.
v4l2loopback-utils needs to be installed, and a virtual webcam needs to be running at `--camera-device` (default: /dev/video1).
A target image and background should be supplied (default: demo_image.png and demo_video.mp4)


Once launched, the script is in background collection mode. Exit the frame and click to collect a background frame.
Upon returning, cycle through different target backgrounds by clicking.
Press Q any time to exit.

Example:
python demo_webcam.py --model-checkpoint "PATH_TO_CHECKPOINT" --resolution 1280 720 --hide-fps
python demo_webcam.py --model-checkpoint "./torchscript_resnet50_fp32.pth"  --resolution 1280 720 --hide-fps --source_device_id 1
# """
import sys
sys.path.append('./matting')

import argparse
import os
import shutil
import time
from dataclasses import dataclass
from threading import Thread, Lock

import cv2
import numpy as np
# import pyfakewebcam  # pip install pyfakewebcam
import torch
from PIL import Image
from torch import nn
from torch.jit import ScriptModule
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import Compose, ToTensor, Resize
from torchvision.transforms.functional import to_pil_image
# from tqdm import tqdm
import utils
import transformer
# import video


STYLE_TRANSFORM_PATH = "./matting/transforms/mosaic.pth"


# --------------- App setup ---------------
app = {
    "mode": "background",
    "bgr": None,
    "bgr_blur": None,
    "compose_mode": "plain",
    "effect_mode": False,
    "target_background_frame": 0
}



class VideoDataset(Dataset):
    def __init__(self, path: str, transforms: any = None ,style_type: any = None,new_self:any = None):
        self.style_type=style_type
        self.new_self=new_self
        # self.recording_index=0
        # self.cap = cv2.VideoCapture(path)
        # if(self.style_type):
        #     new_style_path=self.create_video() #return addr update addr
        #     path=new_style_path
        
        self.cap = cv2.VideoCapture(path)
        self.transforms = transforms
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)

    def create_video(self):
        #fugai create
        device = ("cuda" if torch.cuda.is_available() else "cpu")
        self.device = device
        ret, img = self.cap.read()
    
        while ret:
            print(ret)
            img = utils.itot(img).to(self.device)
            img = self.new_self.net(img)
            img = utils.ttoi(img.detach())
            img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB).clip(0,255)
            img=img.astype(np.uint8)
            frame_name=self.recording(img)
            ret, img = self.cap.read()
        # return frame_name

        return './matting/demo_video.mp4'

    def recording(self, image):  # 根据下标保存视频帧
        _path = os.getcwd()
        self.buf = os.path.join(_path, 'tmp')
        frame_name = "{:08d}.png".format(self.recording_index)
        frame_name = os.path.join(self.buf, frame_name)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if not os.path.exists(self.buf):
            os.makedirs(self.buf)
        cv2.imwrite(frame_name, image)
        print("write!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",frame_name)
        self.recording_index += 1
        return frame_name

    def __len__(self):
        return self.frame_count

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return [self[i] for i in range(*idx.indices(len(self)))]

        if self.cap.get(cv2.CAP_PROP_POS_FRAMES) != idx:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, img1 = self.cap.read()
        if not ret:
            raise IndexError(f'Idx: {idx} out of length: {len(self)}')


        img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        if self.transforms:
            img = self.transforms(img)

        #12345 video bg style change 
        if(self.style_type ):

            # Generate image
            self.device = ("cuda" if torch.cuda.is_available() else "cpu")
            ret, img1 = self.cap.read()
            img1 = utils.itot(img1).to(self.device)
            img = self.new_self.net(img1)
            t=time.time()
            img = utils.ttoi(img.detach())
            t2=time.time()
            print("****************",t2-t)

        return img

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cap.release()


@dataclass
class BGModel:
    model_checkpoint: str
    backbone_scale: float
    refine_mode: str
    refine_sample_pixels: int
    refine_threshold: float

    def model(self):
        return self.model

    def reload(self):
        args = load_args()
        self.model = torch.jit.load(args.model_checkpoint)
        self.model.backbone_scale = args.model_backbone_scale
        self.model.refine_mode = args.model_refine_mode
        self.model.refine_sample_pixels = args.model_refine_sample_pixels
        self.model.model_refine_threshold = args.model_refine_threshold
        # self.model = torch.jit.load(self.model_checkpoint)
        # self.model.backbone_scale = self.backbone_scale
        # self.model.refine_mode = self.refine_mode
        # self.model.refine_sample_pixels = self.refine_sample_pixels
        # self.model.model_refine_threshold = self.refine_threshold
        self.model.cuda().eval()
        

# ----------- Helper Functions -------------

def cv2_frame_to_cuda(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return ToTensor()(Image.fromarray(frame)).unsqueeze_(0).cuda()


class matting_model:
    def preload_init(self):
        # Free-up unneeded cuda memory
        torch.cuda.empty_cache()
        # define transfer model
        device = ("cuda" if torch.cuda.is_available() else "cpu")
        self.device = device
        # style_transform_path = os.path.join(self.transfer_models_path, self.path)
        style_transform_path= self.route
        net = transformer.TransformerNetwork()
        net.load_state_dict(torch.load(style_transform_path))#load style net 
        net = net.to(device)
        self.net = net
        self.style_change=False
    
    def transfer_image_style(self, img):
        # torch.cuda.empty_cache()

        # Generate image
        device = ("cuda" if torch.cuda.is_available() else "cpu")
        self.device = device
        content_tensor = utils.itot(img).to(self.device)

        # normal
        generated_tensor = self.net(content_tensor)

        generated_image = utils.ttoi(generated_tensor.detach())

        return generated_image


    def style_bgr(self,image):
        #change app["bgr_blur"] to style net based on image 
        device = ("cuda" if torch.cuda.is_available() else "cpu")
        # Load Transformer Network
        # print("Loading Transformer Network")
        # net = transformer.TransformerNetwork()
        # STYLE_TRANSFORM_PATH=stat
        # net.load_state_dict(torch.load(STYLE_TRANSFORM_PATH))
        # net = net.to(device)
        net=self.net
        # Get webcam input
        bgr_frame = image
        # app["bgr"] = cv2_frame_to_cuda(bgr_frame)
    # Main loop
        with torch.no_grad():
                # torch.cuda.empty_cache()
                content_tensor = utils.itot(bgr_frame).to(device)
                generated_tensor = net(content_tensor)
                generated_image = utils.ttoi(generated_tensor.detach())
                generated_image=generated_image.clip(0,255).astype(np.uint8)
                app["bgr_blur"] = cv2_frame_to_cuda(generated_image)

                return cv2_frame_to_cuda(generated_image)


    def matting_step1(self,image,style_type):
        app["bgr"] = cv2_frame_to_cuda(image)
        matting_model.style_bgr(self,image)
        args = load_args()
        self.preloaded_image = cv2_frame_to_cuda(cv2.imread(args.target_image))
        self.tb_video = VideoDataset(args.target_video, transforms=ToTensor(),style_type=style_type,new_self=self)#init
        return image

    def matting_step(self,image,input,style_type=None):
            print("many matting model")

            src = cv2_frame_to_cuda(image)
            # app["bgr"] = cv2_frame_to_cuda(frame)
            # grab_bgr(frame)
            
            args = load_args()
            # bgmModel = BGModel(args.model_checkpoint, args.model_backbone_scale, args.model_refine_mode,
            #                args.model_refine_sample_pixels, args.model_refine_threshold)
            # bgmModel.reload()
            # bgmModel=self.model()
            bgmModel=BGModel.model(self)
            pha, fgr = bgmModel(src, app["bgr"])[:2]

            if(input=="img"):
                if(style_type==None):
                    tgt_bgr = nn.functional.interpolate(self.preloaded_image, (fgr.shape[2:]))
                else:
                   
                    if(self.style_change):
                        matting_model.preload_init(self) # style reload
                        matting_model.style_bgr(self,cv2.imread(args.target_image))
                        print("number load style!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    preloaded_image=app["bgr_blur"]

                    # preloaded_image = matting_model.transfer_image_style(self,cv2.imread(args.target_image))  # 风格迁移转换
                    # preloaded_image=cv2.cvtColor(preloaded_image, cv2.COLOR_BGR2RGB).clip(0,255).astype(np.uint8) 
                    # preloaded_image=ToTensor()(preloaded_image).unsqueeze_(0).cuda()              
                    tgt_bgr = nn.functional.interpolate(preloaded_image, (fgr.shape[2:]))


            if(input=="video"):
                if(style_type==None):
                    if(self.style_change):                       
                        self.tb_video = VideoDataset(args.target_video, transforms=ToTensor())#init
                        self.style_change=False
                        
                    vidframe = self.tb_video[app["target_background_frame"]].unsqueeze_(0).cuda()
                    tgt_bgr = nn.functional.interpolate(vidframe, (fgr.shape[2:]))

                    app["target_background_frame"] += 1
                    if app["target_background_frame"] >= self.tb_video.__len__():
                        app["target_background_frame"] = 0
                else:

                    if(self.style_change):

                        matting_model.preload_init(self) # style reload
                        self.tb_video = VideoDataset(args.target_video, transforms=ToTensor(),style_type=style_type,new_self=self)
                        print("number load style!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

                    vidframe = self.tb_video[app["target_background_frame"]]
                    vidframe=vidframe.clip(0,255).astype(np.uint8)
                    vidframe = cv2_frame_to_cuda(vidframe)
                    tgt_bgr = nn.functional.interpolate(vidframe, (fgr.shape[2:]))

                    # t=time.time()
                    # vidframe = self.tb_video[app["target_background_frame"]].cuda()
                    # # tgt_bgr=cv2.cvtColor(vidframe, cv2.COLOR_BGR2RGB).clip(0,255).astype(np.uint8)
                    # # vidframe = cv2_frame_to_cuda(vidframe)
                    
                    # tgt_bgr = nn.functional.interpolate(vidframe, (fgr.shape[2:]))
                    # t2=time.time()
                    # print("%%%%%%%%%",t2-t)
                    

                    app["target_background_frame"] += 1
                    if app["target_background_frame"] >= self.tb_video.__len__():
                        app["target_background_frame"] = 0


            if(input=="style"):
                if(self.style_change):
                        matting_model.preload_init(self) # style reload
                        matting_model.style_bgr(self,self.init_image)
                        print("number load style!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

                tgt_bgr=app["bgr_blur"]
            
            if(input==None):
                tgt_bgr=image

            res = pha * fgr + (1 - pha) * tgt_bgr
            res = res.mul(255).byte().cpu().permute(0, 2, 3, 1).numpy()[0]
            # res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)
            return res

    
def load_args():
    parser = argparse.ArgumentParser(description='Virtual webcam demo')

    parser.add_argument('--model-backbone-scale', type=float, default=0.25)
    parser.add_argument('--model-checkpoint', type=str, default="./matting/torchscript_resnet50_fp32.pth")
    parser.add_argument('--model-checkpoint-dir', type=str, required=False)

    parser.add_argument('--model-refine-mode', type=str, default='sampling',
                        choices=['full', 'sampling', 'thresholding'])
    parser.add_argument('--model-refine-sample-pixels', type=int, default=80_000)
    parser.add_argument('--model-refine-threshold', type=float, default=0.7)

    parser.add_argument('--hide-fps', action='store_true')
    parser.add_argument('--resolution', type=int, nargs=2, metavar=('width', 'height'), default=(1280, 720))
    parser.add_argument('--target-video', type=str, default='./matting/demo_video.mp4')
    parser.add_argument('--target-image', type=str, default='./matting/demo_image.jpg')
    parser.add_argument('--camera-device', type=str, default='/dev/video0')
    parser.add_argument('--source_device_id', type=int, default=1)
    return parser.parse_args()


