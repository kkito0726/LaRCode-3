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
    #値段が記載されているお皿の色の中にi番目に食べたお皿の色が含まれているか確認する。
    if eat_color[i] in dish_color:
        #食べたお皿の色と同じ色がdish_colorのどの位置にあるか特定して値段をpayに加える。
        pay += price[dish_color.index(eat_color[i]) + 1]
    else:
        #食べたお皿の色の値段が決まっていないとき、priceの0番目をpayに加える。
        pay += price[0]
print(pay)
    