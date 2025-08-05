## RAGFlow-DeepDoc

从 RAGFlow 项目中分离出来的 DeepDoc 文档解析模块，原始项目地址：

- [RAGFlow](https://github.com/infiniflow/ragflow/blob/main/README_zh.md)
- [DeepDoc](https://github.com/infiniflow/ragflow/blob/main/deepdoc/README_zh.md)

### 使用

1. 安装依赖（推荐使用虚拟环境）

```bash
pip install -r requirements.txt
```

2. 下载需要的模型等文件（约400MB）

```bash
python scripts/download.py
```

3. 修改 `demo.py` 中的文件路径，运行测试

```bash
python demo.py
```

### 项目说明

- 代码完全来自 RAGFlow 项目，尽量少地去做修改
- 本项目的目的是为了尽可能简单的使用 “文档解析” 功能，去除了 LLM 多模态理解图像解析文档的部分
