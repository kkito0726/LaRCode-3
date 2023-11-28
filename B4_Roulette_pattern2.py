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
#出力2
victory =[]

#賭けた数を一人ずつXと比べて,はずれの人の賭け数を当たっているヒトの中の最小賭け数（37）よりも大きい数にしてます
for i in range(N):
    if (X in A[i]) == False:
        C[i] = 38
        
#当たっている人の中の最小賭け数の人をvictoryのリストに入れてます
for n in range(N):
    if (X in A[n]) == True and C[n] == min(C) and min(C) < 38:
        victory.append(n+1)
        
#当たった人数をprintしてます
print(len(victory))

#当たった人が0人より多い場合誰が当たったかを表示してます。
if len(victory) > 0:
    print(' '.join(map(str,victory)) )    