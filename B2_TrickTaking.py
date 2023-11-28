'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''
n , t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
#n個の0が入ったリストを作成
result = [0]*n
#指定の色がなかったらプレイヤー1の色を指定
if t not in c:
    t = c[0]
#指定の色ならresultに+1
#指定の色ならresultにカードと同じ数を足す
for i in range(n):
    if c[i] == t:
        result[i] += 1
        result[i] += r[i]
#resultの中で一番大きい値の位置をprint
print(result.index(max(result))+1)