"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""

N,P,Q = map(int, input().split())
nedan = list(map(int, input().split()))

# print(N,P,Q)
# print(nedan)

Min = min(nedan)

total = Q
total += Min

if P > total:
    print(total)
else:
    print(P)



