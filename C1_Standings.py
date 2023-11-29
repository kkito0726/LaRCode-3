'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_c
C問題
'''
from decimal import Decimal
#入力
N = int(input())
front_back = [list(map(int, input().split())) for _ in range(N)]
#出力
success_rate = []
for i in range(N):
    success_rate.append([Decimal(front_back[i][0])/Decimal((front_back[i][0]+front_back[i][1])), N-i, i+1])
success_sort = sorted(success_rate, reverse=True)
num_asc = []
for j in range(N):
    num_asc.append(success_sort[j][2])
print(*num_asc)