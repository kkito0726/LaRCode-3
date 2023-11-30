'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_b
B問題
'''
N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
list = []
ans = 0
for i in range(N):
    if C[i] in D:
        list.append(D.index(C[i])+1)
    elif C[i] not in D:
            list.append(0)
    ans += P[list[i]]
print(ans)