"""
freee プログラミングコンテスト2023（AtCoder Beginner Contest 310）
URL: https://atcoder.jp/contests/abc310/tasks/abc310_a
A問題
"""
#入力
N,price,price2 = map(int,input().split())
tuika = list(map(int,input().split()))

#出力
total = 0
if min(tuika)+price2 <price:
    total += min(tuika)+price2
else :
    total+=price
print(total)
