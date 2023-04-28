'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''

board = [input() for i in range(8)]

column = ["a", "b", "c", "d", "e", "f", "g", "h"]
row = [str(i) for i in reversed(range(1, 9))]

# *のときの名前をansに入れる
ans = 0
for i in range(8):
  for j in range(8):
    if board[i][j] == "*":
      ans = column[j]+ row[i]
      
print(ans)