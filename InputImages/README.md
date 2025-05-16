<div align="center">

# 📸 Input Images Gallery

<h3>🌟 默认人脸图片入库目录 🌟</h3>

[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com)
[![Type](https://img.shields.io/badge/Type-Image%20Upload-blue.svg)](https://github.com)
[![Format](https://img.shields.io/badge/Format-JPG%20%7C%20PNG%20%7C%20JPEG-orange.svg)](https://github.com)

</div>

---

## 📂 目录结构

```
InputImages/
├── name/    # 人名目录
│   └── *.jpg       # 人脸图片
```

## 🎯 功能说明

### 图片入库流程
1. **创建人名目录**：为每个人创建独立目录
2. **上传图片**：将人脸图片放入对应目录
3. **自动检测**：系统会自动检测目录中的新图片
4. **人脸入库**：图片会被自动处理并加入人脸库

### 文件命名规则
- 目录名：使用人名拼音（如`Chloe`）
- 图片名：任意名称（如`1.jpg`, `profile.png`）
- 支持格式：`.jpg`, `.png`, `.jpeg`

## 💡 使用建议

1. **图片质量**
   - 使用清晰的正面照片
   - 建议分辨率 ≥ 300x300
   - 光线均匀，无强烈阴影

2. **目录管理**
   - 每人一个独立目录
   - 可存放多张不同角度照片
   - 目录名建议使用英文/拼音

3. **最佳实践**
   - 每人至少3-5张不同照片
   - 包含不同表情（微笑/中性）
   - 不同光照条件下的照片

## ⚙️ 技术规格

| 项目 | 说明 |
|------|------|
| 推荐尺寸 | 300x300 ~ 1000x1000 |
| 文件大小 | < 2MB/张 |
| 色彩模式 | RGB |
| 文件格式 | JPG/PNG/JPEG |
| 命名规范 | 英文/数字/下划线 |

## ⚠️ 注意事项

- 仅包含人脸图片
- 避免团体照片
- 不要修改系统生成的目录
- 首次使用请创建目录结构

## 🛠️ 维护命令

```bash
# 查看目录大小
du -sh InputImages/

# 清理无效图片
find InputImages/ -type f ! -name "*.jpg" ! -name "*.png" ! -name "*.jpeg" -delete
```

---

<div align="center">

**InputImages Gallery** - *人脸识别的起点*

[⬆️ 返回上级](../README.md)

</div>