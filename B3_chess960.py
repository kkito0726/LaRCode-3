'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''
#入力
S = input()
#出力
t = 0
n = []
j = []
for i in range(8):
    if S[i] == 'R':
        n += [i+1]
    if S[i] == 'K':
        j += [i+1]
    if S[i] == 'B':
        t += i+1
if t%2 == 1 and n[0] <= j[0] and n[1]>= j[0]:
    print('Yes')
else:
    print('No')
    
    