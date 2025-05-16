<div align="center">

<a id="readme-top"></a>

# 🎭 VisageX

<h3>🌟 简易的智能人脸识别系统 🌟</h3>

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![DeepFace](https://img.shields.io/badge/DeepFace-Latest-green.svg)](https://github.com/serengil/deepface)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com)

[📚 文档](#使用说明) •
[🚀 快速开始](#安装说明) •
[🛠️ 功能](#功能特点) •
[📞 支持](#技术支持)

![Face Recognition](https://img.shields.io/badge/🔍-Face%20Recognition-brightgreen)

</div>

---

## 🌟 项目简介

VisageX是一款强大而优雅的人脸识别系统，采用最先进的深度学习技术，为用户提供高精度的人脸检测和识别服务。通过直观的图形界面，让复杂的人脸识别技术变得简单易用。

## ✨ 功能特点

### 🔍 多算法支持
<details>
<summary>点击展开支持的检测算法</summary>

| 算法 | 特点 | 适用场景 |
|------|------|----------|
| MTCNN | 高精度 | 通用场景 |
| RetinaFace | 快速准确 | 实时检测 |
| OpenCV | 轻量级 | 简单场景 |
| SSD | 高性能 | 大规模处理 |
| DLIB | 稳定可靠 | 精确检测 |
| MediaPipe | 实时性强 | 视频流处理 |
| YOLOv8 | 最新技术 | 复杂场景 |
| CenterFace | 平衡型 | 移动端 |

</details>

### 🧠 识别模型库
<details>
<summary>点击展开支持的识别模型</summary>

| 模型 | 精度 | 特点 |
|------|------|------|
| SFace | ⭐⭐⭐⭐⭐ | 最新技术 |
| Facenet | ⭐⭐⭐⭐ | 经典可靠 |
| ArcFace | ⭐⭐⭐⭐⭐ | 高精度 |
| VGG-Face | ⭐⭐⭐ | 稳定 |
| Facenet512 | ⭐⭐⭐⭐ | 高维特征 |
| OpenFace | ⭐⭐⭐ | 开源友好 |
| DeepFace | ⭐⭐⭐⭐ | 深度学习 |
| DeepID | ⭐⭐⭐ | 经典架构 |
| Dlib | ⭐⭐⭐ | 传统稳定 |
| GhostFaceNet | ⭐⭐⭐⭐⭐ | 轻量高效 |

</details>

### 💫 核心优势

- 🖥️ **直观界面**
  - 简洁现代的GUI设计
  - 实时可视化反馈
  - 操作流程优化
  - 人性化交互体验

- 🚀 **高性能**
  - 快速响应
  - 并行处理
  - 内存优化
  - 高效算法

- 🛡️ **可靠性**
  - 稳定运行
  - 错误处理
  - 异常恢复
  - 数据备份

## 🔧 系统要求

### 基础环境
```python
Python 3.x
```

### 📦 依赖库
```bash
deepface     # 核心识别框架
tkinter      # GUI界面
PIL          # 图像处理
numpy        # 数值计算
opencv-python # 计算机视觉
```

## 📁 目录结构

```
VisageX/
├── 📜 CommonFunctions.py    # 通用函数库
├── 🎯 face.py              # 主程序
├── 📝 FaceDataBaseDialog.py # 人脸录入对话框
├── 🔍 FaceFindialog.py     # 人脸查找对话框
├── 📊 faceDB/              # 人脸数据库目录
├── 📸 InputImages/         # 输入图像目录
├── 🧠 models/              # 模型文件目录
└── ⚙️ installDepends/      # 依赖安装脚本
```

## 🚀 安装说明

1️⃣ **克隆项目**
```bash
git clone https://github.com/yourusername/VisageX.git
```

2️⃣ **安装依赖**
```bash
cd installDepends
./install.cmd    # Windows
```

## 📖 使用说明

### 1️⃣ 启动程序
```bash
python face.py
```

### 2️⃣ 人脸录入
<details>
<summary>展开详细步骤</summary>

1. 点击 "人脸录入" 按钮
2. 选择需要录入的图像文件
3. 选择人脸检测算法
4. 系统自动检测人脸并显示
5. 输入姓名后点击 "入库" 保存

> 💡 提示：建议使用清晰的正面照片，光线充足

</details>

### 3️⃣ 人脸识别
<details>
<summary>展开详细步骤</summary>

1. 点击 "人脸识别" 按钮
2. 选择需要识别的图像文件
3. 选择人脸检测算法和匹配模型
4. 系统自动进行人脸匹配
5. 查看识别结果和相似度

> 💡 提示：首次使用会自动下载模型文件

</details>

## ⚠️ 注意事项

- 📸 使用清晰的单人正面照
- 🔍 推荐使用MTCNN检测算法
- 📄 支持jpg和jpeg格式
- ⚙️ 首次使用需下载模型

## 👥 开发团队

<div align="center">

### 🌟 奇源空间团队

| 成员 | 职责 |
|------|------|
| rufatkiu | 核心开发 |
| 天将官星 | 算法优化 |

</div>

## 🆘 技术支持

<details>
<summary>常见问题解决方案</summary>

### 1. 安装问题
- ✓ 检查Python版本
- ✓ 确认依赖完整性
- ✓ 查看安装日志

### 2. 运行问题
- ✓ 验证图像格式
- ✓ 确认模型下载
- ✓ 检查内存占用

### 3. 识别问题
- ✓ 确保光线充足
- ✓ 使用正面照片
- ✓ 调整算法参数

</details>

## 📄 许可证

<div align="center">

本项目仅供学习和研究使用。

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com)
[![Built with 🦾](https://img.shields.io/badge/Built%20with-🦾-blue.svg)](https://github.com)

</div>

---

<div align="center">

**VisageX** - 让人脸识别变得简单而强大

[🔝 返回顶部](#readme-top)

</div>
