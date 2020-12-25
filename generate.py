#!/usr/bin/python3

import re
import json
import base64

if __name__ == "__main__":
  f_index = open("./index.html", "r")
  f_content = open("./content.json", "r")
  f_output = open("./docs/index.html", "w")
  
  j_content = json.load(f_content)

  def replacer(match):
    if match[1] == "content":
      return j_content[match[2]]
    elif match[1] == "text": 
      f = open("./assets/" + match[2], "r")
      return f.read()
    elif match[1] == "base64": 
      f = open("./assets/" + match[2], "rb")
      return base64.b64encode(f.read()).decode("utf-8")
    else: raise Exception("Command not recognized: " + match[1])

  for line_in in f_index:
    line_out = re.sub("{{(.*?):(.*?)}}", replacer, line_in)
    f_output.write(line_out)
