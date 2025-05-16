<div align="center">

# ⚙️ Installation Center

<h3>🔧 VisageX 依赖安装中心 🔧</h3>

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![pip](https://img.shields.io/badge/pip-latest-orange.svg)](https://pip.pypa.io/)
[![Status](https://img.shields.io/badge/Status-Stable-success.svg)](https://github.com)

</div>

---

## 📦 依赖概览

本目录包含 VisageX 系统所需的所有依赖项安装脚本。我们使用清华镜像源来确保稳定快速的下载体验。

### 🔍 核心依赖

| 依赖包 | 版本 | 用途 |
|--------|------|------|
| deepface | 最新版 | 核心人脸识别引擎 |
| Pillow | 最新版 | 图像处理库 |
| tf-keras | 最新版 | 深度学习框架 |

## 🚀 安装方法

### 方法一：普通安装（推荐）

```bash
# 在 installDepends 目录下运行
install.cmd
```

### 方法二：管理员权限安装

```bash
# 在 installDepends 目录下运行
setup.bat
```

## 📋 安装说明

### 🔄 安装参数

所有依赖安装都使用以下参数：

```bash
--no-cache-dir      # 禁用缓存
--force-reinstall   # 强制重新安装
--upgrade           # 更新到最新版本
-i [mirror]         # 使用清华镜像源
```

### 🌐 镜像源

```
https://pypi.tuna.tsinghua.edu.cn/simple
```

## ⚡ 快速安装指南

1. **确保环境就绪**
   ```bash
   python --version  # 确认 Python 版本 >= 3.x
   pip --version     # 确认 pip 已安装
   ```

2. **选择安装方式**
   - 普通用户：运行 `install.cmd`
   - 管理员权限：运行 `setup.bat`

3. **验证安装**
   ```python
   python -c "import deepface; print(deepface.__version__)"
   python -c "from PIL import Image; print(Image.__version__)"
   python -c "import tensorflow as tf; print(tf.__version__)"
   ```

## 🛠️ 故障排除

### 常见问题

<details>
<summary>1. 网络连接问题</summary>

- ✔️ 检查网络连接
- ✔️ 确认防火墙设置
- ✔️ 尝试切换网络
</details>

<details>
<summary>2. 权限问题</summary>

- ✔️ 使用管理员权限运行
- ✔️ 检查用户权限
- ✔️ 确认安装目录权限
</details>

<details>
<summary>3. 依赖冲突</summary>

- ✔️ 检查现有包版本
- ✔️ 清理 pip 缓存
- ✔️ 使用虚拟环境
</details>

## ⚠️ 注意事项

1. **安装前**
   - 确保网络连接稳定
   - 关闭杀毒软件
   - 预留足够磁盘空间

2. **安装中**
   - 请勿中断安装过程
   - 观察错误信息
   - 保持电源连接

3. **安装后**
   - 验证所有依赖
   - 测试基本功能
   - 保存错误日志

## 📊 系统要求

| 项目 | 最低要求 | 推荐配置 |
|------|----------|----------|
| Python | 3.7+ | 3.8+ |
| RAM | 4GB | 8GB+ |
| 存储空间 | 2GB | 5GB+ |
| 网络 | 1Mbps | 10Mbps+ |

## 🔄 更新记录

```
2024.01 - 初始版本
- 添加基础依赖安装脚本
- 配置清华镜像源
- 添加管理员权限支持
```

---

<div align="center">

**Installation Center** - *为 VisageX 提供强大动力*

</div>