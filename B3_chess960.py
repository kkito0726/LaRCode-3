'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''

S = input()
isB = False
isK = False

# B, K, Rが何文字めかをリストに格納
B_idx, K_idx, R_idx = [], [], []
for i in range(len(S)):
  if S[i] == "B":
    B_idx.append(i+1)
    
  if S[i] == "K":
    K_idx.append(i+1)
    
  if S[i] == "R":
    R_idx.append(i+1)

# 1つ目の条件を確認
if (B_idx[0] + B_idx[1]) % 2 == 1:
  isB = True

# 2つ目の条件を確認  
if R_idx[0] < K_idx[0] and K_idx[0] < R_idx[1]:
  isK = True

# 両方TrueならYesを出力
if isB and isK:
  print("Yes")
else:
  print("No")