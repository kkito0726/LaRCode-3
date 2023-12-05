"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""
N = int(input())
nums = list(map(int, input().split()))
nums.sort()

isNo = False
for i in range(N-1):
    if nums[i+1] - nums[i] != 1:
        print(nums[i]+1)
        isNo = True
        break

if not isNo:
    print(nums[-1]+1)