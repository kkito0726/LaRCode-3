'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_c
C問題
'''
from decimal import Decimal
#入力
N = int(input())
A_B = [list(map(int,input().split())) for _ in range(N)]
#出力
#確率用のリストrate
rate =[]
ans =[]
#すべての確率を出している
for i in range(N):
    rate.append(Decimal(A_B[i][0])/Decimal((A_B[i][0])+(A_B[i][1])))
for i in range(N):
    ans.append(rate.index(max(rate))+1)
    rate[rate.index(max(rate))] = 0
print(*ans)