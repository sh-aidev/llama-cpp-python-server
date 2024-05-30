
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
