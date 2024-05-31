import requests

# Test with gpt 4 turbo
data = {
  "id": "string",
  "model": "gpt-4-turbo",
  "messages": [
        {"role": "system", "content": "You are an assistant who perfectly describes images."},
        {
            "role": "user",
            "content": [
                {"type" : "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" } }
            ]
        }
  ],
  "temperature": 0.7,
  "top_p": 1,
  "n": 1,
  "max_tokens": 256,
  "user": "string",
  "best_of": 0,
  "top_k": -1,
  "use_beam_search": False,
  "grammar": None
}

response = requests.post('http://localhost:8080/v1/chat/completions', json=data)
print(response.json())  

# test with local multimodal llava model

data = {
  "id": "string",
  "model": "ggml_llava-v1.5-7b",
  "messages": [
        {"role": "system", "content": "You are an assistant who perfectly describes images."},
        {
            "role": "user",
            "content": [
                {"type" : "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" } }
            ]
        }
  ],
  "temperature": 0.7,
  "top_p": 1,
  "n": 1,
  "max_tokens": 256,
  "user": "string",
  "best_of": 0,
  "top_k": -1,
  "use_beam_search": False,
  "grammar": None
}

response = requests.post('http://localhost:8080/v1/chat/completions', json=data)
print(response.json())  

# test with local multimodal llava model with grammer
data = {
  "id": "string",
  "model": "ggml_llava-v1.5-7b",
  "messages": [
        {"role": "user", "content": "My Name is santu and I am 32 years old."},
  ],
  "temperature": 0.7,
  "top_p": 1,
  "n": 1,
  "max_tokens": 256,
  "user": "string",
  "best_of": 0,
  "top_k": -1,
  "use_beam_search": False,
  "grammar": "\nroot ::= Person\nPerson ::= \"{\"   ws   \"\\\"name\\\":\"   ws   string   \",\"   ws   \"\\\"age\\\":\"   ws   number   \"}\"\nstring ::= \"\\\"\"   ([^\"]*)   \"\\\"\"\nws ::= [ \\t]*\nnumber ::= [0-9]+   \".\"?   [0-9]*\n"
}

response = requests.post('http://localhost:8080/v1/chat/completions', json=data)
print(response.json())  