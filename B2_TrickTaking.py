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
pass_R = []

# 空リストに、Tと値が一致したCに対応したRを、[何番目の、何という値か]の形で加えていく
for i in range(N):
    if C[i] == T:
        pass_R.append([i, R[i]])


##### ２．最大値のRを求め、答えを出力する #####

# 基準値を設定する
max_value = 0

# 基準値より大きい場合は更新する
for sublist in pass_R:
    if sublist[1] > max_value:
        max_value = sublist[1]

# Rが最大値になる選手番号を抽出する
for a, b in pass_R:
    if b == max_value:
        print(a+1)
