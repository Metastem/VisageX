#FaceFindialog.py

#######################################################################
#文件：FaceFindialog.py 
#作者: 奇源空间
#功能：将输入图像中的人脸与人脸库中的人脸进行比较，显示匹配的人脸
########################################################################


from tkinter import *
from tkinter import filedialog,messagebox,font 
from PIL import Image, ImageTk
from CommonFunctions import *
from deepface import DeepFace
import os
import csv

#人脸识别对话框类
class FaceFindialog(Toplevel):
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

      
      self.filePathLabel  =Label(self, text="",font=("Microsoft Yahei", 12),borderwidth=1,border=1,relief='sunken',width=50 )
      self.filePathLabel .place(x=140,y=20,height=40)
     
      self.buttonFileDialog =Button(self, 
                                    text="选择图像", 
                                    command=self.chooseImage,
                                    font=("Microsoft Yahei", 12),
                                    width=7 , compound="c",padx=0,pady=0)
      self.buttonFileDialog.place(x=10+ (self.filePathLabel.winfo_reqwidth() +140),y=20)
      self.update()

      fontMeasure =  font.Font(family="Microsoft Yahei" , size = 12) 
      
      
      y=10 + self.filePathLabel.winfo_y()+self.filePathLabel.winfo_height()
      self.faceAlgorimCaptionLabel=Label(self, text="面部识别算法",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.faceAlgorimCaptionLabel.place( x=20,y=y)
      self.update()

      self.faceAlgorim = StringVar()
      algoArray = ['mtcnn','retinaface','opencv' , 'ssd', 'dlib', 'mediapipe', 'yolov8', 'centerface' ,'skip']
      self.faceAlgorim.set('mtcnn')

      self.algoRadios = [None]*len(algoArray)

      
      
       
      for index, algo in enumerate(algoArray):
         radioPixelWidth =   fontMeasure.measure(algo,displayof=self) 
         radioPixelWidth+=30
         radioCtrl= Radiobutton(self, text=algo, variable=self.faceAlgorim, value=algo,  
                  font=("Microsoft Yahei", 12)   ,padx=0, pady=0,relief='flat' ) 
         self.algoRadios[index]=radioCtrl
         
         if (index>0):
             x= self.algoRadios[index-1].winfo_width()+5 +self.algoRadios[index-1].winfo_x()
         else:
             x= self.faceAlgorimCaptionLabel.winfo_x()+self.faceAlgorimCaptionLabel.winfo_width()+20
             radioCtrl.select()
         self.algoRadios   [index] .place( x=x,y=y,width=radioPixelWidth)
         self.update()
#####
      y=10 + self.faceAlgorimCaptionLabel.winfo_y()+self.faceAlgorimCaptionLabel.winfo_height()
      self.faceModelCaptionLabel=Label(self, text="面部匹配模型",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.faceModelCaptionLabel.place( x=20,y=y)
      self.update()

      self.faceModel = StringVar()
      modelArray=['SFace' , 'Facenet' , 'ArcFace','VGG-Face', 'Facenet512','OpenFace', 'DeepFace', 'DeepID', 'Dlib',  'GhostFaceNet']
      self.faceModel.set('SFace')

      self.faceModelRadios = [None]*len(modelArray)

      
       
      for index, model in enumerate(modelArray):
         radioCtrl= Radiobutton(self, text=model, variable=self.faceModel, value=model,  
                  font=("Microsoft Yahei", 12)   ,padx=0, pady=0,relief='flat',width=len(model) ) 
         self.faceModelRadios[index]=radioCtrl
         
         if (index>0):
             x= self.faceModelRadios[index-1].winfo_width()+5 +self.faceModelRadios[index-1].winfo_x()
         else:
             x= self.faceModelCaptionLabel.winfo_x()+self.faceModelCaptionLabel.winfo_width()+20
             radioCtrl.select()
         self.faceModelRadios   [index] .place( x=x,y=y )
         self.update()
      
      

      
#####



      self.update()
      self.orgCaptionLabel=Label(self, text="输入图像",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.orgCaptionLabel.place(x = (self.__windowWdith/2 -   self.orgCaptionLabel.winfo_reqwidth()  )/2
                                 ,y=15+self.faceModelCaptionLabel.winfo_y()+ self.faceModelCaptionLabel.winfo_height() )
      
      self.detectedCaptionLabel=Label(self, text="识别结果",font=("Microsoft Yahei", 12),borderwidth=1,border=1)
      self.detectedCaptionLabel.place(x =  self.__windowWdith/2 +   (self.__windowWdith/2 - self.orgCaptionLabel.winfo_reqwidth()  )/2
                                 ,y=15+self.faceModelCaptionLabel.winfo_y()+ self.faceModelCaptionLabel.winfo_height() )

      self.update()
       
      self.detectedCanvas = Canvas(self ,
                               width=self.__windowWdith/2 -2,
                               height=self.__windowHeight-(5+self.orgCaptionLabel.winfo_y()+  self.orgCaptionLabel.winfo_height()) ,
                               border=0,
                               borderwidth=0,
                               highlightthickness=0,
                               insertborderwidth=0 ,
                               background='#000000'
                               )
       
      self.detectedCanvas.place(
              x=self.__windowWdith/2 +1,
              y=5+self.orgCaptionLabel.winfo_y()+ self.orgCaptionLabel.winfo_height(),
       
              bordermode='ignore',
              )
      
      self.orgCanvas = Canvas(self  ,
                               width=self.__windowWdith/2 -2 ,
                               height=self.__windowHeight-(5+self.orgCaptionLabel.winfo_y()+  self.orgCaptionLabel.winfo_height()) ,
                               border=0,
                               borderwidth=0,
                               highlightthickness=0,
                               insertborderwidth=0 ,
                               background='#000000'
                               )
      
      self.orgCanvas.place(
               x=0,
               y=5+self.orgCaptionLabel.winfo_y()+ self.orgCaptionLabel.winfo_height(),
              
              bordermode='ignore',
              )  
      self.update()
   '''
      END of __init__
   '''

#选择图像后的处理过程
   def chooseImage(self):
       file_path = filedialog.askopenfilename(defaultextension=".jpg",initialdir=".\\InputImages",parent=self,filetypes=[
          ( "jpg", ".jpg"), 
          ( "jpeg", ".jpeg"), 
          ('All Files', '*')])
       if file_path==None:
          return 
       self.orgCanvas.create_rectangle(0,0,self.orgCanvas.winfo_width(),self.orgCanvas.winfo_height(),fill='#000000' )
       self.detectedCanvas.create_rectangle(0,0,self.detectedCanvas.winfo_width(),self.detectedCanvas.winfo_height(),fill='#000000' )
       self.filePathLabel.config(  text=file_path)
       self.imageInformation= loadAndShowImage(imgPath=file_path,canvas=self.orgCanvas)

       y=self.detectedCanvas.winfo_height()//2 ; 
       x=self.detectedCanvas.winfo_width()//2 ; 
       str="正在识别，请稍候"
       self.detectedCanvas.create_text(x, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='center')
       self.update()

       
       try:
         result=DeepFace.find(file_path, 
                     FACE_DB, 
                     model_name =self.faceModel.get()  , 
                     distance_metric = 'cosine', #余弦距离 计算相似度 相似度=（1-余弦距离）* 100%
                     enforce_detection = True, 
                     detector_backend = self.faceAlgorim.get() , 
                     align = True, 
                     silent=False)
       except Exception as err:
            self.detectedCanvas.create_rectangle(0,0,self.detectedCanvas.winfo_width(),self.detectedCanvas.winfo_height(),fill='#000000')
            messagebox.showwarning('提示','没有匹配到人脸',parent=self)
            return 

       if (len(result)<1  or result[0].empty):
          messagebox.showwarning('提示','没有匹配到人脸',parent=self)
          self.detectedCanvas.create_rectangle(0,0,self.detectedCanvas.winfo_width(),self.detectedCanvas.winfo_height(),fill='#000000')
          return

       self.detectedCanvas.create_rectangle(0,0,self.detectedCanvas.winfo_width() ,self.detectedCanvas.winfo_height(),fill='#000000')
       #查找余弦距离最小的结果（即最相似结果）
       minDistance=1E10
       minIdx=-1
       for index in range(len(result)):
          if ( minDistance>result[index].distance[0] ):
              minDistance=result[index].distance[0] 
              minIdx=index
      
       dstImagePath= result[minIdx]['identity'][0] ##: Identity label of the detected individual.
       csvPath = dstImagePath.replace('.png', ".csv")
       name = ''

       #从人脸库中取出匹配到的姓名
       with open(csvPath, newline='',  encoding='utf-8-sig') as csvfile:
              reader = csv.DictReader(csvfile)
              for row in reader:
                    name=row['name']
                    break


       

      ## result[minIdx]['threshold'] # threshold to determine a pair whether same person or different persons 
      ## result[minIdx]['distance']  # Similarity score between the faces based on the   specified model and distance metric

       w = (self.detectedCanvas.winfo_width() -50)//2  ## 距离左边20PX，距离右边20PX，两小图间隔10PX
       h=  (self.detectedCanvas.winfo_height() -50) //2 ## 距离顶边20PX，距离底边20PX，两小图与文字间隔10PX
      
       #显示输入图像中的人脸小图
       srcCroped= cropAndthumbnailImage(
           self.filePathLabel.cget("text") ,
           result[minIdx]['source_x'][0],
           result[minIdx]['source_y'][0],
           result[minIdx]['source_w'][0],
           result[minIdx]['source_h'][0], # Bounding box coordinates of the  detected face in the source image.
           w,
           h
           )
       
        
       self.srcCroped=ImageTk.PhotoImage(srcCroped)

       self.detectedCanvas.create_image(  20, 20 , anchor=NW, image= self.srcCroped)
       
       #显示人脸库中的人脸小图
       dstCroped= cropAndthumbnailImage(
           dstImagePath,
           result[minIdx]['target_x'][0],
           result[minIdx]['target_y'][0],
           result[minIdx]['target_w'][0],
           result[minIdx]['target_h'][0], # Bounding box coordinates of the target face in the database. 
           w,
           h
           )

       self.dstCroped=ImageTk.PhotoImage(dstCroped)
       self.detectedCanvas.create_image(  20+w+10, 20 , anchor=NW, image=self.dstCroped)  

       y= h+20+10+15; 
       str="输入人脸"
       self.detectedCanvas.create_text(20+w/2, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='center')

       y= h+20+10+15; 
       str="库中人脸"
       self.detectedCanvas.create_text(20+10+w+w/2, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='center')


       y= h+20+10+45; 
       str="匹配人脸数：%d" % len(result)
       self.detectedCanvas.create_text(20, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='nw')
       y+=30
       str="姓名：%s" % name
       self.detectedCanvas.create_text(20, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='nw')
       y+=30
       str="相似置信度：%.2f%%" % ((1-result[minIdx]['distance'][0])*100)
       self.detectedCanvas.create_text(20, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='nw')

##       str="距离：%.4f" % result[minIdx]['distance'][0]
##       self.detectedCanvas.create_text(20, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='nw')
##       y+=30
##       str="门限：%.4f" % result[minIdx]['threshold'][0]
##       self.detectedCanvas.create_text(20, y, text=str,fill='#eeeeee',font=('STHeiti',16),anchor='nw')

       imgOffsetX = int( (self.orgCanvas.winfo_width()-self.imageInformation.scaledWidth)/2 )  
       imgOffsetY =int( (self.orgCanvas.winfo_height()-self.imageInformation.scaledHeight)/2 )  
       x = int(result[minIdx]['source_x'][0]* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
       x+= imgOffsetX
       y = int(result[minIdx]['source_y'][0]*self.imageInformation.scaledHeight/ self.imageInformation.orgHeight) 
       y+=imgOffsetY
       w = int(result[minIdx]['source_w'][0]* self.imageInformation.scaledWidth/self.imageInformation.orgWidth)
       h = int(result[minIdx]['source_h']* self.imageInformation.scaledHeight/self.imageInformation.orgHeight)
       self.orgCanvas .create_rectangle(x,y,x+w,y+h, width=1, outline='white')

          
          
          
   '''
      END Of chooseImage
   '''         
