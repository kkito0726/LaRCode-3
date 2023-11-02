'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''
str_list = [input() for _ in range(8)]

for i in range(len(str_list)):
    for j in range(len(str_list[i])):
        num2alpha = lambda c: chr(65+j)
        if str_list[i][j] == '*':
            print((num2alpha(j).lower()), end="")
            print(8-i)
        else:
            pass