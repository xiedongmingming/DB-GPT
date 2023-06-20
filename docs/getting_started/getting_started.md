# Quickstart Guide

This tutorial gives you a quick walkthrough about use DB-GPT with you environment and data.

## Installation

To get started, install DB-GPT with the following steps.

### 1. Hardware Requirements 
As our project has the ability to achieve ChatGPT performance of over 85%, there are certain hardware requirements. However, overall, the project can be deployed and used on consumer-grade graphics cards. The specific hardware requirements for deployment are as follows:

| GPU  | VRAM Size | Performance                                 |
| --------- | --------- | ------------------------------------------- |
| RTX 4090  | 24 GB     | Smooth conversation inference        |
| RTX 3090  | 24 GB     | Smooth conversation inference, better than V100 |
| V100      | 16 GB     | Conversation inference possible, noticeable stutter |

### 2. Install

This project relies on a local MySQL database service, which you need to install locally. We recommend using Docker for installation.

```bash
$ docker run --name=mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=aa12345678 -dit mysql:latest
```
We use [Chroma embedding database](https://github.com/chroma-core/chroma) as the default for our vector database, so there is no need for special installation. If you choose to connect to other databases, you can follow our tutorial for installation and configuration. 
For the entire installation process of DB-GPT, we use the miniconda3 virtual environment. Create a virtual environment and install the Python dependencies.

```
python>=3.10
conda create -n dbgpt_env python=3.10
conda activate dbgpt_env
pip install -r requirements.txt
```

Once the environment is installed, we have to create a new folder "models" in the DB-GPT project, and then we can put all the models downloaded from huggingface in this directory

```
git clone https://huggingface.co/Tribbiani/vicuna-13b 
git clone https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
git clone https://huggingface.co/GanymedeNil/text2vec-large-chinese
```

The model files are large and will take a long time to download. During the download, let's configure the .env file, which needs to be copied and created from the .env.template

```
cp .env.template .env
```

You can configure basic parameters in the .env file, for example setting LLM_MODEL to the model to be used

### 3. Run
You can refer to this document to obtain the Vicuna weights: [Vicuna](https://github.com/lm-sys/FastChat/blob/main/README.md#model-weights) .

If you have difficulty with this step, you can also directly use the model from [this link](https://huggingface.co/Tribbiani/vicuna-7b) as a replacement.

1. Run server
```bash
$ python pilot/server/llmserver.py
```

Starting `llmserver.py` with the following command will result in a relatively stable Python service with multiple processes.
```bash
$ gunicorn llmserver:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 &
```

Run gradio webui

```bash
$ python pilot/server/webserver.py
```

Notice:  the webserver need to connect llmserver,  so you need change the .env file. change the MODEL_SERVER = "http://127.0.0.1:8000" to your address.  It's very important.