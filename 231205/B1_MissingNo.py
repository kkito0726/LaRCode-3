"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""
n = int(input())  # nはint型
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

num_list.sort()
for i in range(n) :
    if num_list[i+1] - num_list[i] != 1 :
        print(num_list[i]+1)
        break
