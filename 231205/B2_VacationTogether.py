"""
トヨタ自動車プログラミングコンテスト2023#4(AtCoder Beginner Contest 311)
URL: https://atcoder.jp/contests/abc311/tasks/abc311_b
B問題
"""
N, D = map(int, input().split())
days = [input() for _ in range(N)]

# 日程ごとに空いている人数を計算
nums = [0 for _ in range(D)]
for day in days:
    for d in range(D):
        if day[d] == "o":
            nums[d] += 1

# 連続して全員が参加できる日数を計算
ans = 0
result = []
for num in nums:
    if num == N:
        ans += 1
        result.append(ans)
    else:
        ans = 0

# リストが空でなければ最大値を出力
if result:
    print(max(result))
else:
    print(0)