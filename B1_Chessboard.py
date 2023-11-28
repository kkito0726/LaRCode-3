'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''
S = [list(input()) for _ in range(8)]
Si = [8, 7, 6, 5, 4, 3, 2, 1]
Sj = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(8):
    if '*' in S[i]:
        print(Sj[S[i].index('*')] + str(Si[i]))