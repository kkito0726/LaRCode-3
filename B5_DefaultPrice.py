'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/abc308/tasks/abc308_b
B問題
'''
#入力
N,M = map(int, input().split())
eat_color = list(input().split())
dish_color = list(input().split())
price = list(map(int, input().split()))
#出力
pay = 0
for i in range(N):
    if eat_color[i] in dish_color:
        pay += price[dish_color.index(eat_color[i]) + 1]
    else:
        pay += price[0]
print(pay)
    