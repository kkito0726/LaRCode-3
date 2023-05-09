'''
AtCoder Beginner Contest 296
https://atcoder.jp/contests/abc296/tasks/abc296_b
B問題
'''

# Sを入力
S = [input() for _ in range(8)]

# アルファベットa~hを並べた「line」変数を設定
line = ["a","b","c","d","e","f","g","h"]

# for文で8*8のマスにおける"*"の有無を探索
for i in range(8):
    for j in range(8):

        # "*"のあるマスのx座標とy座標の値を指定  
        if S[i][j] == "*":
            ans_y = str(8-i)
            ans_x = str(line[j])

# 答えをprint
print(ans_x + ans_y)