'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''
N, T = map(int, input().split())
C, R = [list(map(int, input().split())) for i in range(2)]

list=[]

if T in C:
    for i,s in enumerate(C):
        if s == T:
            list.append(R[i])
        else:
            list.append(0)
else:
    color = C[0] 
    for i,s in enumerate(C):
        if s == color:
            list.append(R[i])
        else:
            list.append(0)

print(list.index(max(list))+1)


