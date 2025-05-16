# VisageX 人脸识别系统

VisageX是一个功能强大的人脸识别系统，基于Python开发，集成了多种先进的人脸检测和识别算法。该系统提供了直观的图形用户界面，支持人脸录入和识别功能。

## 功能特点

- **多算法支持**：集成多种人脸检测算法
  - MTCNN
  - RetinaFace
  - OpenCV
  - SSD
  - DLIB
  - MediaPipe
  - YOLOv8
  - CenterFace

- **多种人脸识别模型**：
  - SFace
  - Facenet
  - ArcFace
  - VGG-Face
  - Facenet512
  - OpenFace
  - DeepFace
  - DeepID
  - Dlib
  - GhostFaceNet

- **人性化界面**：
  - 简洁的图形用户界面
  - 实时人脸检测显示
  - 直观的识别结果展示
  - 支持图像预览

- **核心功能**：
  - 人脸录入：支持单人照片录入，自动检测人脸区域
  - 人脸识别：可与数据库中已存储的人脸进行匹配
  - 相似度计算：使用余弦距离计算人脸相似度
  - 结果可视化：同时显示原图和识别结果

## 系统要求

- Python 3.x
- 依赖库：
  - deepface
  - tkinter
  - PIL (Pillow)
  - numpy
  - opencv-python

## 目录结构

```
VisageX/
├── CommonFunctions.py    # 通用函数库
├── face.py              # 主程序
├── FaceDataBaseDialog.py # 人脸录入对话框
├── FaceFindialog.py     # 人脸查找对话框
├── faceDB/              # 人脸数据库目录
├── InputImages/         # 输入图像目录
├── models/              # 模型文件目录
└── installDepends/      # 依赖安装脚本
```

## 安装说明

1. 克隆或下载本项目到本地
2. 运行安装脚本安装依赖：
   ```bash
   cd installDepends
   ./install.cmd    # Windows
   ```

## 使用说明

1. **启动程序**
   ```bash
   python face.py
   ```

2. **人脸录入**
   - 点击"人脸录入"按钮
   - 选择需要录入的图像文件
   - 选择人脸检测算法
   - 系统会自动检测人脸并显示
   - 输入姓名后点击"入库"保存

3. **人脸识别**
   - 点击"人脸识别"按钮
   - 选择需要识别的图像文件
   - 选择人脸检测算法和匹配模型
   - 系统会自动进行人脸匹配并显示结果
   - 结果包含相似度和匹配的人员信息

## 注意事项

- 录入照片时请使用清晰的单人正面照
- 建议使用MTCNN作为默认的人脸检测算法
- 图像文件支持jpg和jpeg格式
- 首次使用某个识别模型时会自动下载相应的模型文件

## 技术支持

如遇到问题，请检查：
1. 是否正确安装了所有依赖
2. 图像格式是否支持
3. 是否使用了单人正面照片
4. 模型文件是否下载完整

## 许可证

本项目仅供学习和研究使用。
