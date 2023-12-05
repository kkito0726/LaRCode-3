"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""
#入力
N = int(input())
A = list(map(int, input().split()))

#出力
ans = sorted(A)
ans2=[]
for i in range(ans[0],ans[-1]+1):
    ans2.append(i)
for i in ans2:
    if i not in ans:
        print(i)


#SUM = 

#for i in A:
#   SUM -= i