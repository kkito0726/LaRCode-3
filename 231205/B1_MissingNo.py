"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    if 0 < i and A[i] - A[i-1] == 2:
        ans += (A[i]-1)
print(ans)