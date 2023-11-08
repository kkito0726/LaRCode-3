'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''
#入力
N,T = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(2)]
#出力
t = 0
n = []
for i in range(N):
    if C[0][i] == T and C[1][i] >= t:
       t = C[1][i]
    else:
        n += 'N'
for p in range(N):
    if len(n) == N:
        if C[0][p] == C[0][0] and C[1][p] >= t :
            t =C[1][p]
print(C[1].index(t)+1)

        