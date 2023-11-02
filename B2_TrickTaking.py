'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''
N, T = map(int, input().split())#Nはプレイヤー数, Tは色の数
C = list(map(int, input().split()))#Cは色
R = list(map(int, input().split()))#Rは値

count = []
if T in C:
    for i in range(N):#Tと同じ色のプレイヤーの場合
        if C[i] == T:
            count.append([R[i], i+1])#[値の大きさ, プレイヤーO]
        else:#Tと違う色のプレイヤーの場合
            pass
    tornament = sorted(count, reverse=True)
    print(tornament[0][1])
else:
    for i in range(N):
        if C[i] == C[0]:#プレイヤー1と同じ色のプレイヤーの場合
            count.append([R[i], i+1])
        else:#プレイヤー1と違う色のプレイヤーの場合
            pass
    tornament = sorted(count, reverse=True)
    print(tornament[0][1])