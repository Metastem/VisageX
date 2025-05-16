##FaceDataBaseDialog.py 

#######################################################################
#文件：FaceDataBaseDialog.py 
#作者: 工商2024-1 傅思奇，李思嘉，刘可欣
#功能：识别输入图像中的人脸，将识别出的人脸剪裁后放库
########################################################################

from tkinter import *
from tkinter import filedialog,messagebox,font 
from PIL import Image, ImageTk
from CommonFunctions import *
from deepface import DeepFace
import os
import csv
# 人脸识别对话框类
class FaceDataBaseDialog(Toplevel):
   # 预定义窗口大小变量
   __windowWdith=960
   __windowHeight=540
   def __init__(self, parent):
      super().__init__(parent)
      self.title(AUTHOR)
      self.__windowWdith=int(self.winfo_screenwidth()*0.75)
      self.__windowHeight=int(self.winfo_screenheight()*0.75)
      centerWindow(self,self.__windowWdith,self.__windowHeight)
      filePathCaptionLabel =Label(self, text="图像文件路径",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      filePathCaptionLabel.place(x=20,y=20)
      self.resizable(False,False)
      
      self.filePathLabel  =Label(self, text="",font=("Microsoft Yahei", 12),borderwidth=1,border=1,relief='sunken',width=50 )
      self.filePathLabel .place(x=140,y=20,height=40)
     
      self.buttonFileDialog =Button(self, 
                                    text="选择图像", 
                                    command=self.chooseImage,
                                    font=("Microsoft Yahei", 12),
                                    width=7 , compound="c",padx=0,pady=0)
      self.buttonFileDialog.place(x=10+ (self.filePathLabel.winfo_reqwidth() +140),y=20)

      self.nameCaptionLabel=Label(self, text="姓名",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.nameCaptionLabel.place( x=10+ (self.filePathLabel.winfo_reqwidth() +140+self.buttonFileDialog.winfo_reqwidth()+10),y=20)
      self.nameText = Text(self,font=("Microsoft Yahei", 12),height=1,width=10,state='disabled')
      self.nameText.bind('<Key>', self.onNameTextInput)
      self.nameText.place(   x=10+ (self.filePathLabel.winfo_reqwidth() +140+self.buttonFileDialog.winfo_reqwidth()+10+self.nameCaptionLabel.winfo_reqwidth()+10),y=20)

      self.buttonSaveFace =Button(self, 
                                    text="入库", 
                                    command=self.saveFace,
                                    font=("Microsoft Yahei", 12),
                                    width=7 , compound="c",padx=0,pady=0,state='disabled')
      self.buttonSaveFace.place(  x=10+ (self.filePathLabel.winfo_reqwidth() +140+self.buttonFileDialog.winfo_reqwidth()+10+self.nameCaptionLabel.winfo_reqwidth()+10)
                                +self.nameText.winfo_reqwidth()
                                ,y=20)
      self.update()

      y=10 + self.filePathLabel.winfo_y()+self.filePathLabel.winfo_height()
      self.faceAlgorimCaptionLabel=Label(self, text="面部识别算法",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.faceAlgorimCaptionLabel.place( x=20,y=y)
      self.update()

      # 人脸识别算法Radio控件的存储变量
      self.faceAlgorim = StringVar()
      algoArray = ['mtcnn','retinaface','opencv' , 'ssd', 'dlib'
                   , 'mediapipe', 'yolov8', 'centerface' ,'skip'
                   ]
      self.faceAlgorim.set('mtcnn')
      #预定义Radio控件数组
      self.algoRadios = [None]*len(algoArray) 
      fontMeasure =  font.Font(family="Microsoft Yahei" , size = 12)
       
      for index, algo in enumerate(algoArray):
        #计算Radio里文字像素宽度
         radioPixelWidth =   fontMeasure.measure(algo,displayof=self) 
         radioPixelWidth+=30
         radioCtrl= Radiobutton(self, text=algo, variable=self.faceAlgorim, value=algo,  
                  font=("Microsoft Yahei", 12)   ,padx=0, pady=0,relief='flat' ) 
         self.algoRadios[index]=radioCtrl
         
         # 计算每个Radio控件的摆放位置
         if (index>0):
             x= self.algoRadios[index-1].winfo_width()+5 +self.algoRadios[index-1].winfo_x()
         else:
             x= self.faceAlgorimCaptionLabel.winfo_x()+self.faceAlgorimCaptionLabel.winfo_width()+20
             radioCtrl.select()
         self.algoRadios   [index] .place( x=x,y=y,width=radioPixelWidth)
         self.update()

      self.orgCaptionLabel=Label(self, text="输入图像",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.orgCaptionLabel.place(x = (self.__windowWdith/2 -   self.orgCaptionLabel.winfo_width()  )/2
                                 ,y=15+self.faceAlgorimCaptionLabel.winfo_y()+ self.faceAlgorimCaptionLabel.winfo_height() )
      
      self.detectedCaptionLabel=Label(self, text="面部识别图像",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.detectedCaptionLabel.place(x =  self.__windowWdith/2 +   (self.__windowWdith/2 - self.faceAlgorimCaptionLabel.winfo_width()  )/2
                                 ,y=15+self.faceAlgorimCaptionLabel.winfo_y()+ self.faceAlgorimCaptionLabel.winfo_height() )

      self.update()
     
      self.orgImageCanvas = Canvas(self ,border=0,
                               borderwidth=0,
                               highlightthickness=0,
                               insertborderwidth=0 ,
                               background="#000000"
                               )
      self.orgImageCanvas.place(
          x=0,
          y=5+self.orgCaptionLabel.winfo_y()+ self.orgCaptionLabel.winfo_reqheight(),
          width=self.__windowWdith/2 -2 ,
          height=self.__windowHeight-(5+self.orgCaptionLabel.winfo_y()+  self.orgCaptionLabel.winfo_reqheight()) )
      self.detectedImageCanvas = Canvas(self, borderwidth=0,
                               highlightthickness=0,
                               insertborderwidth=0 ,
                               background="#000000")
      self.detectedImageCanvas .place(
          x=self.__windowWdith/2 +1,
          y=5+self.orgCaptionLabel.winfo_y()+ self.orgCaptionLabel.winfo_reqheight(),
          width=self.__windowWdith/2 -2 ,
          height=self.__windowHeight-(5+self.orgCaptionLabel.winfo_y()+  self.orgCaptionLabel.winfo_reqheight()) )      
      self.update()
   '''
      END of __init__
   '''

   #当选择输入图像后，处理图像的过程
   def chooseImage(self):
       file_path = filedialog.askopenfilename(defaultextension=".jpg",initialdir=".\\InputImages",parent=self,filetypes=[( "jpg", ".jpg"),( "jpeg", ".jpeg"),  ('All Files', '*')])
       if file_path==None:
          return 
       self.filePathLabel.config(  text=file_path)
       #用黑色填充输入图像画布
       self.orgImageCanvas.create_rectangle(0,0,self.orgImageCanvas.winfo_width(),self.orgImageCanvas.winfo_height(),fill='#000000' )
       #显示输入的图像 
       self.imageInformation= loadAndShowImage(file_path,self.orgImageCanvas )
       #用黑色填充输出图像画布
       self.detectedImageCanvas.create_rectangle(0,0,self.detectedImageCanvas.winfo_width(),self.detectedImageCanvas.winfo_height(),fill='#000000' )
       #计算输入图像MD5
       self.fileMd5Text=getFileMD5(file_path)
       #识别结果存放文件，用csv格式存放
       faceRecordCSV = FACE_DB+self.fileMd5Text+".csv"
       #识别出的面部小图
       faceRecordPng = FACE_DB+self.fileMd5Text+".png"
       #先禁止保存按钮和姓名输入按钮
       self.buttonSaveFace.config(state='disabled')
       self.nameText.config(state='disabled')
       #将姓名删去
       self.nameText.delete('0.0','end')
       if (os.path.exists(faceRecordCSV) & os.path.exists(faceRecordPng) ):
            #此图像已经识别并入库过，给出提示并给出识别结果
            messagebox.showwarning('提示','图像已经入库,请选择其它人脸图像',parent=self)
            self.loadFaceRecord(faceRecordCSV,faceRecordPng)
       else:
           #执行面部检测
           y=self.detectedImageCanvas.winfo_height()//2 ; 
           x=self.detectedImageCanvas.winfo_width()//2 ; 
           str="正在识别，请稍候"
           self.detectedImageCanvas.create_text(x, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='center')
           self.update()
           self.faceDetect(file_path)    
   '''
      END Of chooseImage
   '''         

   #人脸入库
   def saveFace(self):
       nameTxt = self.nameText.get('0.0','end')[:-1]
       # 判断是否输入姓名，否则要求输入姓名
       if ( len(nameTxt) <1):
           self.nameText.focus()
           return 
       faceRecordCSV = FACE_DB+self.fileMd5Text+".csv"
       faceRecordPng = FACE_DB+self.fileMd5Text+".png"
       header=['facial_area_x',
               'facial_area_y',
               'facial_area_w',
               'facial_area_h',
               'facial_area_left_eye_x',
               'facial_area_left_eye_y',
               'facial_area_right_eye_x',
               'facial_area_right_eye_y',
               'name']
       data=[{'facial_area_x':self.facial_area_x,
             'facial_area_y':self.facial_area_y,
             'facial_area_w':self.facial_area_w,
             'facial_area_h':self.facial_area_h,
             'facial_area_left_eye_x':self.facial_area_left_eye_x,
             'facial_area_left_eye_y':self.facial_area_left_eye_y,
             'facial_area_right_eye_x':self.facial_area_right_eye_x,
             'facial_area_right_eye_y':self.facial_area_right_eye_y,
             'name':nameTxt}]
       #保存脸部检测结果
       with open(faceRecordCSV, 'w', encoding='utf-8-sig', newline='') as f:
           writer = csv.DictWriter(f, header)
           writer.writeheader()
           writer.writerows(data)
       #保存脸部小图
       imageCropped =self.imageInformation.imgOrg.crop((self.facial_area_x, self.facial_area_y, self.facial_area_x + self.facial_area_w, self.facial_area_y+self.facial_area_h))
       imageCropped.save(faceRecordPng,'PNG')
       #有新图像入库，先删除所有.pkl文件，否则脸部比对出错
       files = os.listdir(FACE_DB)
       for file in files:
           if os.path.isfile(file) and file.endswith(".pkl"):
               os.remove(file)
       messagebox.showinfo('提示','入库成功',parent=self)
   '''
   END Of saveFace
   '''    
##########################
#功能：调入上次识别结果并显示
#输入：
#   faceRecordCSV：识别结果csv文件路径
#   faceRecordPng：识别结果的脸部小图
#输出：
#   无
##########################
   def loadFaceRecord(self,faceRecordCSV,faceRecordPng):
       with open(faceRecordCSV, newline='',  encoding='utf-8-sig') as csvfile:
              reader = csv.DictReader(csvfile)
              for row in reader:
                    self.facial_area_x=int(row['facial_area_x'])
                    self.facial_area_y=int(row['facial_area_y'])
                    self.facial_area_w=int(row['facial_area_w'])
                    self.facial_area_h=int(row['facial_area_h'])
                    self.facial_area_left_eye_x= int(row['facial_area_left_eye_x'])
                    self.facial_area_left_eye_y=int(row['facial_area_left_eye_y'])
                    self.facial_area_right_eye_x=int(row['facial_area_right_eye_x'])
                    self.facial_area_right_eye_y=int(row['facial_area_right_eye_y'])
                    self.name=row['name']
                    break
        
       self.nameText.delete(1.0, END)
       self.nameText.insert(END, self.name)
       imgOffsetX = int( (self.detectedImageCanvas.winfo_width()-self.imageInformation.scaledWidth)/2 )  
       imgOffsetY =int( (self.detectedImageCanvas.winfo_height()-self.imageInformation.scaledHeight)/2 )  
       x = int(self.facial_area_x* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
       y = int(self.facial_area_y*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
       w = int(self.facial_area_w* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
       h = int(self.facial_area_h* self.imageInformation.scaledHeight/self.imageInformation.orgHeight)
 
       #显示输入图像
       self.detectedImageCanvas.create_image( imgOffsetX, imgOffsetY , anchor=NW, image=self.imageInformation.image)
       #在输入图像上绘制识别出的脸部框
       self.detectedImageCanvas.create_rectangle(x,y,x+w,y+h, width=1, outline='white')

       #绘制左眼位置
       x = int(self.facial_area_left_eye_x* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
       y = int(self.facial_area_left_eye_y*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
       self.detectedImageCanvas.create_oval(x-3,y-3,x+3,y+3, width=1, outline='white')
       #绘制右眼位置
       x = int(self.facial_area_right_eye_x* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
       y = int(self.facial_area_right_eye_y*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
       self.detectedImageCanvas.create_oval(x-3,y-3,x+3,y+3, width=1, outline='white')

   '''
   END Of loadFaceRecord
   '''    

##########################
#功能：人脸检测，将识别结果放入内存变量
#输入：
#   file_path：待检测图像路径
#输出：
#   无
##########################
   def faceDetect(self,file_path):
          try:
              algo=self. faceAlgorim.get()
              result =DeepFace.extract_faces(img_path = file_path,detector_backend=algo)
          except Exception as err:
            #输入图像不能检测出人脸
            w=self.detectedImageCanvas.winfo_width() ; 
            h=self.detectedImageCanvas.winfo_height() ; 
            self.detectedImageCanvas.create_rectangle(0,0,w,h,fill='#000000') 
            messagebox.showwarning('提示','请选择一张单人正面照',parent=self)
            return 
              
          detectCnt=len(result)
          #输入图像人脸不能多于一个
          if (detectCnt!=1):
              w=self.detectedImageCanvas.winfo_width() ; 
              h=self.detectedImageCanvas.winfo_height() ; 
              self.detectedImageCanvas.create_rectangle(0,0,w,h,fill='#000000') 
              messagebox.showerror('提示','请选择一张单人正面照',parent=self)
              return 
          #result[0].face
          self.facial_area_x= result[0]['facial_area']['x']
          self.facial_area_y=result[0]['facial_area']['y']
          self.facial_area_w=result[0]['facial_area']['w']
          self.facial_area_h=result[0]['facial_area']['h']
          if (result[0]['facial_area']['left_eye']!=None):
             self.facial_area_left_eye_x= result[0]['facial_area']['left_eye'][0]
             self.facial_area_left_eye_y=result[0]['facial_area']['left_eye'][1]
          else:   
             self.facial_area_left_eye_x= -1
             self.facial_area_left_eye_y=-1
          if (result[0]['facial_area']['right_eye']!=None):
             self.facial_area_right_eye_x=result[0]['facial_area']['right_eye'][0]
             self.facial_area_right_eye_y=result[0]['facial_area']['right_eye'][1]
          else:
             self.facial_area_right_eye_x=-1
             self.facial_area_right_eye_y=-1
          imgOffsetX = int( (self.detectedImageCanvas.winfo_width()-self.imageInformation.scaledWidth)/2 )  
          imgOffsetY =int( (self.detectedImageCanvas.winfo_height()-self.imageInformation.scaledHeight)/2 )  
          x = int(self.facial_area_x* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
          y = int(self.facial_area_y*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
          x+=imgOffsetX
          y+=imgOffsetY
          w = int(self.facial_area_w* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
          h = int(self.facial_area_h* self.imageInformation.scaledHeight/self.imageInformation.orgHeight)
          
          #显示输入图像
          self.detectedImageCanvas.create_image( imgOffsetX, imgOffsetY , anchor=NW, image=self.imageInformation.image)
          #绘制脸部识别框
          self.detectedImageCanvas.create_rectangle(x,y,x+w,y+h, width=1, outline='white')

          #绘制左眼
          if (self.facial_area_left_eye_x>-1 and self.facial_area_left_eye_y>-1):
             x = int(self.facial_area_left_eye_x* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
             y = int(self.facial_area_left_eye_y*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
             x+=imgOffsetX
             y+=imgOffsetY
             self.detectedImageCanvas.create_oval(x-3,y-3,x+3,y+3, width=1, outline='white')
          #绘制右眼
          if (self.facial_area_right_eye_x>-1 and self.facial_area_right_eye_y>-1):
            x = int(self.facial_area_right_eye_x* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
            y = int(self.facial_area_right_eye_y*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
            x+=imgOffsetX
            y+=imgOffsetY
            
          self.detectedImageCanvas.create_oval(x-3,y-3,x+3,y+3, width=1, outline='white')
          messagebox.showerror('提示','请输入姓名',parent=self)
          self.nameText .config(state='normal')
   '''
   END Of faceDetect
   '''

   def onNameTextInput(self,event):
       self.buttonSaveFace.config(state='normal')
   
"""
   END    FaceDataBaseDialog 
 """
      
