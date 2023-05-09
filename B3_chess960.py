'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''

# 入力
S = list(input())


# 条件1のクリアをみるflag1と、条件2のクリアをみるfrag2を設定
flag1 = False
flag2 = False


# 空リストを作成
B_index = []

# そのリストにBのindexのみ追加
for i in range(len(S)):
    if S[i] == 'B':
        B_index.append(i+1)

# Bのindexの奇偶が異なる場合、flag1をTrueに変更
for _ in B_index:
    if B_index[0] % 2 != B_index[1] % 2:
        flag1 = True
                

# 空リストを作成
K_index = []
R_index = []

# そのリストにKとRのindexのみそれぞれ追加
for i in range(len(S)):
    if S[i] == "K":
        K_index.append(i+1)
    
    if S[i] == "R":
        R_index.append(i+1)

# KがRの間にある場合、flag2をTrueに変更
for _ in K_index:
    if R_index[0]  < K_index[0] and K_index[0] < R_index[1]:
        flag2 = True

# 出力
if flag1 and flag2:
    print("Yes")

else:
    print("No")