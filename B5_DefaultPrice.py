'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_b
B問題
'''
#入力
N,M = map(int,input().split())
C = (input().split())
D = (input().split()) 
P = list(map(int,input().split()))
#出力
#お会計用の０を作りました
total = 0
#Cの配列とDの配列を一つずつ比べてます。
for i in range(M):
    for n in range(N):
        if C[n] == D[i]:
            total += P[i+1]
#Dの中にCに含まれている要素が存在しないか見て、P[0]を足してます。
for i in range(N):
    if (C[i] in D) == False:
        total += P[0]
#お会計に移らせていただきます
print(total)
        