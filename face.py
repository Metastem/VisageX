import sys 
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
from CommonFunctions import *
from deepface import DeepFace
from FaceDataBaseDialog import *
from FaceFindialog import *
from os  import *
   
#预定义窗口变量   
mainWindow=None

##########################
#功能：显示人脸入库窗口
#输入：
#   无
#输出：
#   无
##########################
def ShowDBaseWindow():
    window = FaceDataBaseDialog(  mainWindow )
    window.grab_set()
    return

##########################
#功能：显示人脸识别窗口
#输入：
#   无
#输出：
#   无
##########################
def ShowRecoganizeWindow():
    window = FaceFindialog(  mainWindow )
    window.grab_set()
    return
# 判断人脸库目录是否存在，不存在则创建
if ( not os.path.exists(FACE_DB)):
   os.makedirs(FACE_DB)

# 设置deepface 预训练库位置环境变量
deepfaceHome=os.getenv('DEEPFACE_HOME')
# 判断DEEPFACE_HOME环境变量是否存在，若不存在则用自己的FACE_MODEL创建DEEPFACE_HOME环境变量
if ( deepfaceHome==None or len(deepfaceHome)<1 ):
    os.environ['DEEPFACE_HOME']= os.path.abspath(FACE_MODELS) 

#创建主窗口
mainWindow = Tk()
mainWindow.title('工商2024-1 傅思奇，李思嘉，刘可欣')
mainWindow.geometry("480x270")
mainWindow.resizable(False,False)
centerWindow(mainWindow,480,270)
#创建人脸入库按钮
buttonFaceDBase = Button(mainWindow,
                          text="人脸入库", 
                          height=2,
                          font=("Microsoft Yahei", 14),
                          highlightbackground="black",
                          highlightcolor="green",
                          highlightthickness=2,
                          justify="center",
                          overrelief="raised",
                          padx=10,
                          pady=5,
                          width=12,
                          foreground='#444',
                          command=ShowDBaseWindow)
# 创建人脸识别按钮
buttonFaceRecoganize = Button(mainWindow, 
                          text="人脸识别", 
                          height=2,
                          font=("Microsoft Yahei", 14),
                          highlightbackground="black",
                          highlightcolor="green",
                          highlightthickness=2,
                          justify="center",
                          overrelief="raised",
                          padx=10,
                          pady=5,
                          width=12,
                          foreground='#444',
                          command=ShowRecoganizeWindow)
buttonFaceDBase.place(x=50,y=90)
buttonFaceRecoganize.place(x=249,y=90)
mainWindow.mainloop()



 


