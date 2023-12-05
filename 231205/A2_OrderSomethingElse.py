"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""
N, teika, waribiki = map(int, input().split())
price = list(map(int, input().split()))

pay = []
for i in range(N):
    if waribiki + price[i] < teika:
        pay.append(waribiki + price[i])
    else:
        pay.append(teika)
print(min(pay))