'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''
#入力
S = [input() for _ in range(8)]
#出力
#位置を示すアルファベットと数字をリストにしました
H = ['a','b','c','d','e','f','g','h']
J = ['8','7','6','5','4','3','2','1']
#１行ずつ(iで)1要素(nで)ずつ調べてます
for i in range(8):
    for n in range(8):
        if S[i][n] == '*':
            print(H[n]+J[i])

            

