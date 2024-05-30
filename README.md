<div align="center">

# **LLaMA CPP Python Server with FastAPI**

[![python](https://img.shields.io/badge/-Python_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![fastapi](https://img.shields.io/badge/-FastAPI_%7C_0.68.1-278c5d?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![uvicorn](https://img.shields.io/badge/-Uvicorn_%7C_0.15.0-8c9146?logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)
[![cpp](https://img.shields.io/badge/-C%2B%2B_-00599c?logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
![license](https://img.shields.io/badge/License-MIT-green?logo=mit&logoColor=white)

This repository contains the source code for the LLaMA CPP Python Server with FastAPI. The server is a REST API that allows users to interact with the LLaMA C++ library using Python. The server is built using FastAPI, a modern web framework for building APIs with Python. The server uses Uvicorn as the ASGI server to run the FastAPI application. The server provides endpoints for interacting with the LLaMA C++ library, including loading models, making predictions also provides endpoints for embeddings and health checks.

</div>

## 📌 Feature
- [x] **FastAPI** endpoint gguf models
- [x] **FastAPI** endpoint for embeddings
- [x] **FastAPI** endpoint for health checks
- [x] accept dynamic grammar data in fastapi request

## 📁  Project Structure
The directory structure of new project looks like this:

```bash
├── LICENSE
├── README.md
├── __main__.py
├── configs
│   └── config.toml
├── docker
│   └── Dockerfile.dev
├── examples
│   └── test.py
├── requirements.txt
└── src
    ├── __init__.py
    ├── app.py
    ├── core
    │   ├── __init__.py
    │   ├── llm_core.py
    │   └── llm_embed.py
    ├── server
    │   ├── __init__.py
    │   └── server.py
    └── utils
        ├── __init__.py
        ├── configs.py
        ├── logger.py
        ├── models.py
        ├── openai_protocol.py
        └── s3.py
```

## 🚀 Getting Started
### Step 1: Clone the repository
```bash
git clone https://github.com/sh-aidev/llama-cpp-python-server.git

cd llama-cpp-python-server
```

### Step 2: Install the dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the server
```bash
python3 __main__.py
```

### Step 4: Run the server using Docker
```bash
# Build the Docker image
docker build -t llama-cpp-python-server:latest -f docker/Dockerfile.dev .

# Run the Docker container
docker run -p 8080:8080 --rm llama-cpp-python-server:latest
```

### Step 5: Test the server

You can test the server by sending a POST request to the `/predict` endpoint with a JSON payload containing the input data. Here is an example using the `requests` library in Python else, you can test using fastapi docs.

Go to `http://<host>:<port>/docs` to test the server using FastAPI docs.


## 📜  References

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [C++](https://isocpp.org/)
- [LLaMACpp](https://github.com/ggerganov/llama.cpp.git)
- [OpenOrcha-Mistral](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca)
