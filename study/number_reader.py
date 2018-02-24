#!/usr/bin/env python
# encoding: utf-8

import json
'''
with open('numbers.json') as f:
  numbers = f.readlines()
print numbers
'''

#username = raw_input("What is your name? ")

'''
with open(filename, 'w') as f:
  json.dump(username, f)
  print("We'll remember you when you come back, " + username + "!")
'''

'''如果以前存储了用户名,加载 ;# 否,提示用户输入用户名并存储''' 
"""
def greet_user():
  '''问hou用户并指出其名字'''
filename = 'username.json'
  try:
    with open(filename) as f:
      username = json.load(f) 
  except IOError:
      username = raw_input("What is your name? ")
      with open(filename, 'w') as f:
        json.dump(username, f)
        print("We'll remember you when you come back, " + username + "!")
  else:
      print("Welcome back, " + username + "!")


'''重构greet_user():将其按照功能拆分'''

def storage_user():
  filename = 'username.json'
  username = raw_input("What is your name? ")
  try:
      with open(filename, 'w') as f:
        json.dump(username, f)
  except IOError:
    pass
  else:
    return username


def greet_user():
    username = storage_user()
    if username:
      print("Welcome back, " + username + "!")
    else:
      username = input("What is your name? ") 
      filename = 'username.json'
      with open(filename, 'w') as f:
          json.dump(username, f)
          print("We'll remember you when you come back, " + username + "!")
        
greet_user()
"""



filename = 'numbers.json'

try:
  with open(filename) as f:
    fav_num = raw_input('your favourite number:')
    json.dump(fav_num,f)
    print("your favourite number is:" + favourite_num)
except IOError:
  print(filename + " not exist") 

'''
with open(filename) as f:
  favourite_num = json.load(f)
  print("your favourite number is:" + favourite_num)
  
'''














































