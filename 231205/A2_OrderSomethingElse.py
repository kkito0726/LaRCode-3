"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""
N, P, Q = map(int, input().split())
foods = list(map(int, input().split()))

ans = [P]
for i in range(N):
    ans.append(Q+foods[i])

print(min(ans))