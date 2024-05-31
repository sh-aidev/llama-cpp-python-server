import requests

# # Test embedding with gpt models
data = {
    "id": "string",
    "model": "text-embedding-ada-002",
    "text": "My Name is santu and I am 32 years old."
}

response = requests.post('http://localhost:8080/v1/embeddings', json=data)
print(response.json())

# Test embedding with local BAAI/bge-large-en
data = {
    "id": "string",
    "model": "BAAI/bge-large-en",
    "text": "My Name is santu and I am 32 years old."
}

response = requests.post('http://localhost:8080/v1/embeddings', json=data)
print(response.json())