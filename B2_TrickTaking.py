'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''

# 入力
N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))


##### １．条件を満たすRを整理 #####

# C列にTがない場合、C列最初の値をTとする
if not T in C:
    T = C[0]

# 空リストを作る
pass_Rs = []

# 空リストに、Tと値が一致したCに対応するRのみを、[index、Rの値]の形で加えていく
for i in range(N):
    if C[i] == T:
        pass_Rs.append([i, R[i]])


##### ２．最大値のRを求め、答えを出力 #####

# 基準値を設定する
max_value = 0
max_player = 0

# 基準値より大きい場合は更新する
for pass_R in pass_Rs:
    player, value = pass_R
    if value > max_value:
        max_value = value
        max_player = player 

# Rが最大値になる選手番号を抽出する
print(max_player + 1)
