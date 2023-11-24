'''
AtCoder Beginner Contest 314
URL: https://atcoder.jp/contests/abc314/tasks/abc314_b
B問題
'''
#入力
N = int(input())
C_list = []
A_list = []
for i in range(N):
    C_list.append(int(input()))
    A_list.append(list(map(int,input().split())))
X = int(input())

#出力
num_buy = 37
B = []
#N人分の賭け数を調べていく
for i in range(N):
    #i番目の人がXにかけていた時に以下の処理を実行
    if X in A_list[i]:
        #最大37点賭けられる中で点数が少ない人が現れたらnum_buyを更新し、以前のBをリセットし、i+1番目の人をBに加える。
        if C_list[i] < num_buy:
            num_buy = C_list[i]
            B.clear()
            B.append(i+1)
        #最小点数と同じ購入数であればi+1番目の人をBに加える。
        elif C_list[i] == num_buy:
            B.append(i+1)
print(len(B))
print(*B)