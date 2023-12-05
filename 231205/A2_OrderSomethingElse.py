"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
if (Q + min(D)) < P:
    print(Q + min(D))
else:
    print(P)