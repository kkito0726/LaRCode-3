"""
トヨタ自動車プログラミングコンテスト2023#4(AtCoder Beginner Contest 311)
URL: https://atcoder.jp/contests/abc311/tasks/abc311_b
B問題
"""
#入力
N,D = map(int, input().split())
S = [input() for _ in range(N)]
#出力
import copy
#みんな休みがあるときのかぶりを出力します。
yasumi =[[] for _ in range(N)]
#一人ずつ休みの数を見て、個別のリストに休みの日を列挙してます。
for i in range(N):
    for n in range(D):
        if S[i][n] == 'o':
            yasumi[i].append(n)
match = copy.copy(yasumi[0])
for i in range(N):
    for n in yasumi[0]:
        if not n in yasumi[i] and n in match:
            match.remove(n) 
m =[]
ans =[]
ans.append(0)
for i in range(len(match)-1):
    if match[i+1]-match[i] == 1:
        m.append(i)
        ans.append(len(m))
    else :
        ans.append(len(m))
        m.clear()
if len(match) == 0:
    print(0)
else :
    print(max(ans)+1)

            


   
            
            
    
 

    
