# 项目运行

项目所在虚拟环境：dbgpt

1. 首先进行环境配置（复制模板文件）

```
.env
```

2. 运行LLM服务

```
python llmserver.py
```

3. 运行GRADIO（会调用LLM服务）

```
python webserver.py 
```