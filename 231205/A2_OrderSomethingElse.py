"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""

N,P,Q = map(int,input().split())
D = list(map(int, input().split()))

price = P
for i in range(len(D)):
    if (D[i]+Q) < price:
        price = (D[i]+Q)

print(price)
