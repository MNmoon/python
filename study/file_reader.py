#!/usr/bin/env python
# encoding: utf-8
'''
print '-----------------With代码块内读取  处理-------------------------------------'
with open("pi_digits.txt") as f:
  contents = f.read()
  print contents.rstrip()

print '------------With代码块内读取信息，with代码块外面处理-------------------------'

with open('pi_digits.txt') as f:
  lines = f.readlines()

for line in lines:
  print line.rstrip()


pi_string = ''

for line in lines:
  pi_string +=line

print pi_string.rstrip()

print len(pi_string)

print '-------------打印前面10位，避免不断的打印导致终端不断的翻滚-----------------'
print pi_string[:10] + '.....'

print '一次性打印所有文件内容'
with open('learning_python.txt') as learn:
  contents = learn.readlines()
  for line in contents:
    print line.rstrip()

print 'With代码块内读取信息，with代码块外面处理'
with open('learning_python.txt') as learn:
  contents = learn.readlines()

for line in contents:
  print line.rstrip()

print '遍历文件对象????'
with open('learning_python.txt') as learn:
  content = learn.readline()
  print content.rstrip()


print 'Replace python to C \n '

with open('learning_python.txt',"rw") as f:
  contents = f.readlines()
  for line in contents:
    if 'Python' in line:
      line = line.replace('Python','C')
      print line

print 'Python2.7貌似不能用with open自动创建一个不存在的文件'
with open('programming.txt','a') as f:
  f.write('I love programming\n')
  f.write('I love programming\n')
  f.write("I also love finding meaning in large datasets.\n")
  f.write("I love creating apps that can run in a browser.\n")

with open('guest.txt','w') as f:
  nam = input('enter your name:')
  f.write(nam)


count = 0
while True:
  with open('guest_book.txt','a') as f:
    name = raw_input('please enter your name:') 
    if not name == 'exit':
        print 'Welcome ' + name
        count += 1 
    else:
      break
    f.write('visit:' + str(count) + '\n')

'''












































