"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""
a,b,c = map(int, input().split())  # 3個の数字の入力を受け取る                     # 出力を確認
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

price = 0
for i in num_list :
    if b <= c + min(num_list):
        price = b
    else :
        price = c + min(num_list)

print(price)



