<div align="center">

# 🏋️ DeepFace 权重文件

<h3>⚖️ 预训练模型存储位置 ⚖️</h3>

[![DeepFace](https://img.shields.io/badge/DeepFace-0.0.79-blue.svg)](https://github.com/serengil/deepface)
[![Weights](https://img.shields.io/badge/Weights-Pretrained-orange.svg)](https://github.com/serengil/deepface/releases)

</div>

---

## 📂 目录说明

此目录包含DeepFace使用的所有预训练权重文件：

```
weights/
├── *.h5        # Keras模型权重
├── *.onnx      # ONNX模型文件
└── *.caffemodel # Caffe模型文件
```

## 🔍 文件用途

- **.h5文件**：Keras格式的模型权重
- **.onnx文件**：ONNX格式的模型
- **.caffemodel**：Caffe格式的模型

## ⚠️ 注意事项

1. 不要手动修改文件名
2. 不要删除任何权重文件
3. 保持目录结构完整
4. 首次使用时DeepFace会自动下载缺失文件

## 🔄 更新方式

```bash
# 删除所有权重文件强制重新下载
rm -rf .deepface/weights/*
```

---

<div align="center">

[⬆️ 返回上级](../README.md)

</div>