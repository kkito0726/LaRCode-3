'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''
num_list = [input() for _ in range(8)]

first = ["a","b","c","d","e","f","g","h"]
second = ["8","7","6","5","4","3","2","1"]

for i in range(8) :
    for n in range(8) :
        if num_list[i][n] == "*" :
            print(first[n]+second[i])