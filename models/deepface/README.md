<div align="center">

# ⚙️ DeepFace 配置中心

<h3>🛠️ 模型和配置文件存储位置 🛠️</h3>

[![DeepFace](https://img.shields.io/badge/DeepFace-0.0.79-blue.svg)](https://github.com/serengil/deepface)
[![Config](https://img.shields.io/badge/Config-DeepFace-yellow.svg)](https://github.com/serengil/deepface)

</div>

---

## 📂 目录结构

```
.deepface/
└── weights/      # 权重文件目录
```

## 🔧 功能说明

1. **权重存储**：存放所有预训练模型权重
2. **配置管理**：存储DeepFace运行时的配置文件
3. **缓存控制**：管理模型缓存和版本信息

## ⚠️ 注意事项

1. 此目录由DeepFace自动管理
2. 不要手动修改目录结构
3. 删除此目录会强制重新下载所有模型
4. 建议定期备份重要权重文件

## 🔄 维护命令

```bash
# 清除所有缓存
rm -rf .deepface/

# 仅清除权重
rm -rf .deepface/weights/
```

---

<div align="center">

[⬆️ 返回上级](../README.md)

</div>