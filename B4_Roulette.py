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
for i in range(N):
    if X in A_list[i]:
        if C_list[i] < num_buy:
            num_buy = C_list[i]
            B.clear()
            B.append(i+1)
        elif C_list[i] == num_buy:
            B.append(i+1)
print(len(B))
print(*B)