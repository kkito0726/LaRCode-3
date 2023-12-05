"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""

N = int(input())
A = list(map(int, input().split()))

A_sort = sorted(list(set(A)))

for i in range(len(A_sort)):
  if not A_sort[i+1] == A_sort[i] + 1:
    print(A_sort[i]+1)
    break
