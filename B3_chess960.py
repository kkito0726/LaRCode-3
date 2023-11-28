'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''
S = list(input())
score = 0
R = []
K = S.index('K')
for i in range(8):
    if S[i] == 'R':
        R.append(i)
    if S[i] == 'B' and i % 2 == 0:
        score += 1
if score == 1 and R[0] < K < R[1]:
    print("Yes")
else:
    print("No")