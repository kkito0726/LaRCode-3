"""
トヨタ自動車プログラミングコンテスト2023#4(AtCoder Beginner Contest 311)
URL: https://atcoder.jp/contests/abc311/tasks/abc311_b
B問題
"""
N, D = map(int, input().split())
str_list = [input() for _ in range(N)]
day_1 = list(range(1, D+1))
for i in range(N):
    for j in range(D):
        if str_list[i][j] == 'x':
            if j+1 in day_1:
                day_1.remove(j+1)
count = 1
scedule = []
ans = []
for i in range(len(day_1)-1):
    if day_1[i+1] == day_1[i]+1:
        scedule.append(day_1[i])
        count += 1
    elif not day_1[i+1] == day_1[i]+1:
        ans.append(count)
        count = 1
ans.append(count)
if len(day_1) == 0:
    print(0)
else:
    print(max(ans))