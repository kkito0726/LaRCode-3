"""
ゲームフリーク Programming Contest 2023（AtCoder Beginner Contest 317）
URL: https://atcoder.jp/contests/abc317/tasks/abc317_b
B問題
"""
n = int(input())  # nはint型
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

new_list = sorted(num_list)

for i in range(n) :
    if new_list[i+1] - new_list[i] != 1:
         print(new_list[i]+1)
         break