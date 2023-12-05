"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""
N = int(input())
succession = list(map(int, input().split()))
sort_suc = sorted(succession)
list_1 = list(range(sort_suc[0], sort_suc[0]+N+1))
ans = []
for i in range(N):
    if not sort_suc[i] == list_1[i]:
        ans.append(list_1[i])
print(ans[0])