'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''

str = input()
#条件1: Bの偶奇判定
b_check = []
for i in range(len(str)):
    if str[i] == 'B':
        if i % 2 == 0:
            b_check.append(2)
        else:
            b_check.append(1)
    else:
        b_check.append(0)
b_sum = sum(b_check)#Bの偶奇が異なれば3, 同じなら2か4
#条件2: Kの位置判定
horizon = [1, 2, 3, 4, 5, 6, 7, 8]
x_str = []
RK_judge = []
for i in range(len(str)):
    if str[i] == 'R':
        x_str.append([horizon[i], str[i]])
    elif str[i] == 'K':
        x_str.append([horizon[i], str[i]])
#条件1と条件2を満たす場合のみ「Yes」を出力
if b_sum == 3:
    if x_str[1][1] == 'K':
        print('Yes')
    else:
        print('No')
else:
    print('No')