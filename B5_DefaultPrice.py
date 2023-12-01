'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_b
B問題
'''
N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
result = []
ans = 0
for i in range(N):
    if C[i] in D:
        result.append(D.index(C[i])+1)
    elif C[i] not in D:
            result.append(0)
    ans += P[result[i]]
print(ans)