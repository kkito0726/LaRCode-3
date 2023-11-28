'''
AtCoder Beginner Contest 314
URL: https://atcoder.jp/contests/abc314/tasks/abc314_b
B問題
'''
#入力
N = int(input())
C = []
A = []
for i in range(N):
    C.append(int(input()))
    A.append(list(map(int,input().split())))
X = int(input())
#print(N)
#print(C)
#print(A)
#print(X)

#出力1
M = []
victory = []
#X(当たり)があるか見てる
for i in range(N):
    if (X in A[i]) == True:
        M.append(C[i])
#print(M)
#当たった人の中でかけた数が少ない人をvictoryリストに入れてる
if len(M) > 0:
    for n in range(len(M)):
        if M[n] == min(M):
            victory.append(C.index(M[n])+1)
            C[C.index(M[n])] = N
    print(M.count(min(M)))
#リストを文字列にしてます。
    print(' '.join(map(str,victory)) ) 
else :
    M.append(0)
    print(' '.join(map(str,M)) ) 
#print(C)
#リストを文字列にしてます。        

        