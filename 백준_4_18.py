# -*- coding: utf-8 -*-
"""백준 4 18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cR2rx374a7qumOo0w4C9pIDL0JeDHxGZ

https://noanswercode.tistory.com/14

10828번 해설:
코랩에서는 sys.stdin.readline 사용이 불가능하므로 idle에서 풀어야함.

input()으로 할 경우 많이 느려서 돌아가지 않음.

함수 정의해서 그냥 풀면 됨.
"""

# 10828
import sys

def push(X):
  stack.append(X)

def pop():
  try:
     print(stack.pop(-1))
  except:
     print(-1)  

def size():
  print(len(stack))

def empty():
  if len(stack) == 0:
     print(1)
  else:
     print(0)  

def top():
  try:
     print(stack[-1])  
  except:
     print(-1)

stack = []
n = int(sys.stdin.readline())

for i in range(n):
    
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    elif cmd[0] == "top":
        top()

