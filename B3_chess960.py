'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''
#入力
S = input()
#出力
#Bに関する判定の際に、和から偶奇を判断するため0を作ってます。
t = 0
#RとKの位置をリストとして保管するために空のリストを作成しました。
n = []
j = []
#文字列を1要素ずつ見ていき、R,K,Bがきたら配列をリストに記憶/0に足しています。
for i in range(8):
    if S[i] == 'R':
        n += [i+1]
    if S[i] == 'K':
        j += [i+1]
    if S[i] == 'B':
        t += i+1
#偶奇ならその和は2で割れないandKの位置をRの位置と比較してYesかNoを判断しています。
if t%2 == 1 and n[0] <= j[0] and n[1]>= j[0]:
    print('Yes')
else:
    print('No')
    
    