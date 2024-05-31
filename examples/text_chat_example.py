import requests

# # Test chat with gpt models
data = {
  "id": "string",
  "model": "gpt-4-turbo",
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
  "grammar": None
}

response = requests.post('http://localhost:8080/v1/chat/completions', json=data)
print(response.json())  

# # Test chat with local mistral models
data = {
  "id": "string",
  "model": "mistral-7b-openorca.Q6_K.gguf",
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
  "grammar": None
}

response = requests.post('http://localhost:8080/v1/chat/completions', json=data)
print(response.json())  

# Test chat with local mistral models with grammer
data = {
  "id": "string",
  "model": "mistral-7b-openorca.Q6_K.gguf",
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


# Grammer_string = "\nroot ::= Person\nPerson ::= \"{\"   ws   \"\\\"name\\\":\"   ws   string   \",\"   ws   \"\\\"age\\\":\"   ws   number   \"}\"\nstring ::= \"\\\"\"   ([^\"]*)   \"\\\"\"\nws ::= [ \\t]*\nnumber ::= [0-9]+   \".\"?   [0-9]*\n"

# grammar_txt = r'''
# root ::= Person
# Person ::= "{"   ws   "\"name\":"   ws   string   ","   ws   "\"age\":"   ws   number   "}"
# string ::= "\""   ([^"]*)   "\""
# ws ::= [ \t]*
# number ::= [0-9]+   "."?   [0-9]*
# '''