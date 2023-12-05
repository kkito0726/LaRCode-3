"""
トヨタ自動車プログラミングコンテスト2023#4(AtCoder Beginner Contest 311)
URL: https://atcoder.jp/contests/abc311/tasks/abc311_b
B問題
"""

N, D = map(int, input().split())
S = [input() for _ in range(N)]

days = [0] * D

# 参加可能人数をリストにする
for i in S:
    for j in range(D):
        if i[j] == "o":
            days[j] += 1

aeru = 0
aeru_days = []

# 全員参加可能な日をカウント
for k in days:
    if k == N:
        aeru += 1
        aeru_days.append(aeru)

    else:
        aeru = 0

# 出力
if aeru_days == []:
    print(0)
else:
    print(max(aeru_days))