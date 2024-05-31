
# with open("grammer.gbnf", "r") as file:
#     grammar_txt = file.read()

# response = client.chat.completions.create(
#   model="llava-hf/bakLlava-v1-hf",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "How many people live in Berlin?"},
#       ],
#     }
#   ],
#   max_tokens=300,
#   grammar = grammar_txt
# )

# for chunk in response:
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content, end="")

# from srca
# import json
# grammar_txt = r'''
# root ::= Person
# Person ::= "{"   ws   "\"name\":"   ws   string   ","   ws   "\"age\":"   ws   number   "}"
# string ::= "\""   ([^"]*)   "\""
# ws ::= [ \t]*
# number ::= [0-9]+   "."?   [0-9]*
# '''
# print(grammar_txt)
# x = json.dumps(grammar_txt)

# print(x)
# y = '\nroot ::= Person\nPerson ::= "{"   ws   "\\"name\\":"   ws   string   ","   ws   "\\"age\\":"   ws   number   "}"\nstring ::= "\\""   ([^"]*)   "\\""\nws ::= [ \\t]*\nnumber ::= [0-9]+   "."?   [0-9]*\n'

# # z = y.decode("utf-8")

# print(str.encode(y))

# x = {
#   "messages": [
#     {
#       "additionalProp1": "string",
#       "additionalProp2": "string",
#       "additionalProp3": "string"
#     }
#   ],
#   "temperature": 0.7,
#   "top_p": 1,
#   "n": 1,
#   "max_tokens": 0,
#   "user": "string",
#   "best_of": 0,
#   "top_k": -1,
#   "use_beam_search": False,
#   "grammar": '\nroot ::= Person\nPerson ::= "{"   ws   "\\"name\\":"   ws   string   ","   ws   "\\"age\\":"   ws   number   "}"\nstring ::= "\\""   ([^"]*)   "\\""\nws ::= [ \\t]*\nnumber ::= [0-9]+   "."?   [0-9]*\n'
# }

# y = x["grammar"].encode()
# z = y.decode("utf-8")
# print(z)
# import json
# print(json.dumps(x))


# x = r"\nroot ::= Person\nPerson ::= \"{\"   ws   \"\\\"name\\\":\"   ws   string   \",\"   ws   \"\\\"age\\\":\"   ws   number   \"}\"\nstring ::= \"\\\"\"   ([^\"]*)   \"\\\"\"\nws ::= [ \\t]*\nnumber ::= [0-9]+   \".\"?   [0-9]*\n"

# print(str.encode(x).decode('unicode_escape'))

import time
import uuid
from typing import Any, Dict, List, Literal, Optional, Union, Annotated
from fastapi import File

from pydantic import BaseModel, Field

def random_uuid() -> str:
    return str(uuid.uuid4().hex)

class ChatCompletionRequest(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{random_uuid()}")
    model: str = "gpt-3.5-turbo"
    messages: List[Dict[str,Any]]
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    max_tokens: Optional[int] = 256
    user: Optional[str] = None
    best_of: Optional[int] = None
    top_k: Optional[int] = -1
    use_beam_search: Optional[bool] = False
    grammar: Optional[str] = None

data = ChatCompletionRequest(**{
  "id": "string",
  "model": "gpt-3.5-turbo",
  "messages": [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What'\''s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
          }
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
})
print(data)