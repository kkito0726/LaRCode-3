'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''
#入力
N,T = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(2)]
#出力
#0を作って後々数を比較する際に使います。
t = 0
#色がTでないかを１要素ずつ見てNを入れるために空のリストを作ってます。
n = []
for i in range(N):
#色がTのものの中から大きいものを確認して、tに置換している。
    if C[0][i] == T and C[1][i] >= t:
       t = C[1][i]
#Tでない場合は、nにN(NoのN)を追加します。
    else:
        n += 'N'
for p in range(N):
#Nが４つたまっていたら、すべての色がT出ない場合は、色がプレイヤー1と同じものの中から最大値を探しています。
    if len(n) == N:
        if C[0][p] == C[0][0] and C[1][p] >= t :
            t =C[1][p]
#最大値が分かったので、要素から位置を特定しています。
print(C[1].index(t)+1)

        