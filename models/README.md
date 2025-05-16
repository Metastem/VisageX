<div align="center">

# 🤖 DeepFace 模型仓库

<h3>⚡ 预训练权重文件存储中心 ⚡</h3>

[![DeepFace](https://img.shields.io/badge/DeepFace-0.0.79-blue.svg)](https://github.com/serengil/deepface)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Weights](https://img.shields.io/badge/Weights-Pretrained-orange.svg)](https://github.com/serengil/deepface/releases)

</div>

---

## 📂 目录结构

```
models/
└── .deepface/
    └── weights/          # 权重文件目录
        ├── *.h5          # Keras模型权重
        ├── *.onnx        # ONNX模型文件
        └── *.caffemodel  # Caffe模型文件
```

## 🔗 完整模型下载列表

### 人脸识别模型

| 模型名称 | 文件 | 下载链接 |
|---------|------|---------|
| ArcFace | `arcface_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/arcface_weights.h5) |
| Facenet | `facenet_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/facenet_weights.h5) |
| Facenet512 | `facenet512_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/facenet512_weights.h5) |
| VGG-Face | `vgg_face_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/vgg_face_weights.h5) |
| DeepID | `deepid_keras_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/deepid_keras_weights.h5) |
| OpenFace | `openface_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/openface_weights.h5) |
| GhostFaceNet | `ghostfacenet_v1.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/ghostfacenet_v1.h5) |
| SFace | `face_recognition_sface_2021dec.onnx` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/face_recognition_sface_2021dec.onnx) |

### 人脸检测模型

| 模型名称 | 文件 | 下载链接 |
|---------|------|---------|
| RetinaFace | `retinaface.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/retinaface.h5) |
| CenterFace | `centerface.onnx` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/centerface.onnx) |
| SSD | `res10_300x300_ssd_iter_140000.caffemodel` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/res10_300x300_ssd_iter_140000.caffemodel) |

### 属性分析模型

| 模型名称 | 文件 | 下载链接 |
|---------|------|---------|
| Age Prediction | `age_model_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/age_model_weights.h5) |
| Gender Prediction | `gender_model_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/gender_model_weights.h5) |
| Emotion Detection | `facial_expression_model_weights.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/facial_expression_model_weights.h5) |
| Race Prediction | `race_model_single_batch.h5` | [下载](https://github.com/serengil/deepface/releases/download/v1.0/race_model_single_batch.h5) |

## 💾 下载说明

1. **自动下载**：DeepFace会在首次使用时自动下载所需模型
2. **手动下载**：
   - 点击上方链接下载对应文件
   - 将文件保存到 `models/.deepface/weights/` 目录
   - 保持原始文件名不变

## ⚠️ 注意事项

- 确保下载完整的模型文件（无.part临时文件）
- 部分大文件下载可能需要较长时间
- 建议使用稳定的网络连接
- 总大小约 1.5GB（所有模型）

## 🛠️ 验证安装

```python
from deepface import DeepFace

# 检查基础模型
DeepFace.build_model("Facenet")
print("模型加载成功！")

# 检查检测模型
DeepFace.build_model("RetinaFace")
print("检测模型加载成功！")
```

---

<div align="center">

[⬆️ 返回顶部](#deepface-模型仓库) | 
[🌐 访问DeepFace官网](https://github.com/serengil/deepface)

</div>
