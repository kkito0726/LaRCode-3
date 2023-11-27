'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_b
B問題
'''

N, M = map(int,input().split())

C = list((input().split()))
D = list((input().split()))
P = list(map(int, input().split()))

total = 0

for i in range(N):
    if C[i] in D:
        total += P[D.index(C[i]) + 1]
    else:
        total += P[0]

print(total)
