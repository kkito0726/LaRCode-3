'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''
#パターン１

N = 8
komoji = [chr(i) for i in range(ord('a'),ord('h')+1)]

list = []
for i in range(N):
   list.append(input())

for i, s  in enumerate(list):
   if "*" in s:
      x = str(komoji[s.index("*")])
      y = str(N - i)
      print(x+y)