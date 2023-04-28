'''
東京海上日動プログラミングコンテスト2023（AtCoder Beginner Contest 299）
https://atcoder.jp/contests/abc299/tasks/abc299_b
B問題
'''

N, T = map(int, input().split())
colors = list(map(int, input().split()))
points = list(map(int, input().split()))

# 色がTであるカードが出なかった場合プレーヤー1の色をTとする
if not T in colors:
  T = colors[0]

# 出したカードの色がTであるプレーヤーを抽出
matched_player_ids = []
for i in range(len(colors)):
  if T == colors[i]:
    matched_player_ids.append(i)

# ポイントの最大値のプレイヤーを探索
max_point, max_id = 0, 0
for id in matched_player_ids:
  if points[id] > max_point:
    max_point = points[id]
    max_id = id
    
print(max_id+1)