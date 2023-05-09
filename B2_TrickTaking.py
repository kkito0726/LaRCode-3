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
    C[0] = T

# 空リストを作る
pass_Rs = []

# 空リストに、Tと値が一致したCに対応するRのみを、[index、Rの値]の形で加えていく
for i in range(N):
    if C[i] == T:
        pass_Rs.append([i, R[i]])


##### ２．最大値のRを求め、答えを出力 #####

# 基準値を設定する
max_value = 0

# player, value関数を用意する
player = 0
value = 0

# 基準値より大きい場合は更新する
for pass_R in pass_Rs:
    pass_R = player, value
    if value > max_value:
        max_value = value

# Rが最大値になる選手番号を抽出する
if value == max_value:
    print(player)
