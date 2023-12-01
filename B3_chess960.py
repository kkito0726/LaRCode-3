'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''
S = list(input())
score = 0
#Sの中のRの位置のリスト
R = []
#Sの中のKの位置
K = S.index('K')
for i in range(8):
    #Sの中のRの位置をリストRに入れる
    if S[i] == 'R':
        R.append(i)
    #Bが偶数ならscoreに+1
    if S[i] == 'B' and i % 2 == 0:
        score += 1
#Bが偶奇かどうか、偶2ならscore=2、偶奇ならscore=1、奇2ならscore=0
#リストRの0番目よりもKが大きく、リストRの1番目よりもKが小さいならKは間に挟まれている
if score == 1 and R[0] < K < R[1]:
    print("Yes")
else:
    print("No")