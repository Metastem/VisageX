#common py 
#######################################################################
#文件：common py 
#作者: 工商2024-1 傅思奇，李思嘉，刘可欣
#功能：人脸识别基础函数和公共变量定义模块
########################################################################

import sys 
from tkinter import *
from PIL import Image, ImageTk
from typing import NoReturn
import collections;
import hashlib
# 全局变量
AUTHOR="人工智能应用大作业-人脸识别 作者:工商2024-1 李睿佳"

FACE_DB="faceDB/" # 人脸库存放位置
FACE_MODELS="models/" #模型库存放位置
##########################
#功能：将窗口放置在屏幕正中
#输入：
#   window：待放置的窗口
#   width：窗口宽度，单位屏幕像素
#   height：窗口高度，单位屏幕像素
#输出：
#   无
##########################
# 先获取屏幕大小，再根据窗口大小计算中间位置
def centerWindow(window, width, height)-> NoReturn:
    #获取屏幕尺寸
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()

    #计算窗口居中显示的参数
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    #设置窗口居中显示
    window.geometry(size)
    '''
    END Of centerWindow
    '''
##########################
#功能：从硬盘中加载图像文件，保持高宽比缩放图像，将缩放后的图像显示在画布控件中
#输入：
#   imgPath：图像文件路径
#   canvas：  画布控件
#输出：
#   原始图像大小
#   缩放后图像大小
##########################
def loadAndShowImage(imgPath,canvas) :
    # 打开图像
    image = Image.open(imgPath)
    orgWidth=image.width 
    orgHeight= image.height
    
    # 获取画布的大小
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # 判断图像的宽高比例
    image_ratio = image.width / image.height
    canvas_ratio = canvas_width / canvas_height

    # 缩放图像以保持比例
    if image_ratio > canvas_ratio:
    # 图像宽高比例大于画布宽高比例，调整宽度为画布宽度
        scaled_width = canvas_width
        scaled_height = int(canvas_width / image_ratio)
    else:
    # 图像宽高比例小于画布宽高比例，调整高度为画布高度
        scaled_height = canvas_height
        scaled_width = int(canvas_height * image_ratio)
    # 先拷贝原图像
    imgOrg= image.copy()
    # 调整图像大小
     
    resampled=image.resize(size=(scaled_width, scaled_height),resample=Image.Resampling.BICUBIC);

    # 将图像转换为Tkinter可用的格式
    photo = ImageTk.PhotoImage(resampled)
   
    canvas.create_image(  (canvas_width - scaled_width)//2 , (canvas_height - scaled_height)//2 , anchor=NW, image= photo)
    
    ReturnValue = collections.namedtuple ('ImageInfomation', ['image','imgOrg','orgWidth', 'orgHeight','scaledWidth', 'scaledHeight'])
    # Image: 要显示的Python格式的图像 
    # Imgorg: 原始的jpg格式图像 
    # orgWidth：原始图像宽度 
    # orgHeight：原始图像高度 
    # scaledWidth：缩放过后图像的宽度 
    # scaledHeight: 缩放过后图像的高度
    ret= ReturnValue(image=photo,imgOrg=imgOrg, orgWidth=orgWidth ,orgHeight= orgHeight,scaledWidth=scaled_width, scaledHeight=scaled_height)
    
    return ret ; 
    '''
    END Of loadAndShowImage
    '''

##########################
#功能：从硬盘中加载图像文件，从源图像中剪切指定范围的图像,保持高宽比缩放图像，生成缩放后的图像
#输入：
#   imgPath：图像文件路径
#   srcX:剪裁区域的X坐标
#   srcY:剪裁区域的Y坐标
#   srcWidth:剪裁区域宽度
#   srcHeight:剪裁区域高度
#   destWidth：生成的图像宽度 
#   destHeight:生成的图像高度 
#输出：
#   缩放后图像
##########################    
def cropAndthumbnailImage(imgPath,srcX,srcY,srcWidth,srcHeight, destWidth,destHeight):
    image = Image.open(imgPath)
     
    
   

    # 判断图像的宽高比例
    image_ratio = srcWidth / srcHeight
    canvas_ratio = destWidth / destHeight

    # 缩放图像以保持比例
    if image_ratio > canvas_ratio:
    # 图像宽高比例大于画布宽高比例，调整宽度为画布宽度
        scaled_width = destWidth
        scaled_height = int(destWidth / image_ratio)
    else:
    # 图像宽高比例小于画布宽高比例，调整高度为画布高度
        scaled_height = destHeight
        scaled_width = int(destHeight * image_ratio)
    cropedImg = image.crop((srcX,srcY,srcX+srcWidth,srcY+srcHeight))    
    resampled=cropedImg.resize(size=(scaled_width, scaled_height),resample=Image.Resampling.BICUBIC);
    return resampled


##########################
#功能：读取文件内容，返回文件MD5码
#输入：
#   filePath：文件路径
#输出：
#   文件 Md5
##########################
#用途：判断文件的唯一性
def getFileMD5(filePath):
    md5 = hashlib.md5()
    #以二进制只读方式打开文件
    with open(filePath, 'rb') as file:
        while (True):
            # 每次读取4096个字节到content变量中
            content= file.read(4096)
            if (content==None):
                break
            if (len(content)<1):
                break
            md5.update(content)
    md5Text=md5.hexdigest()
    return md5Text
    '''
    END Of getFileMD5
    '''
            