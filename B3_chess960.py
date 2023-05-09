'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''

# 入力
S = list(input())

# ans関数を設定
ans = "No"

# 2つのBのindexが、奇偶異なるものを抽出
for a in range(len(S)):
    for b in range(a+1, len(S)):
        if S[a] == 'B' and S[b] == 'B':
            if a % 2 != b % 2:
                
                # x < z < yの関係を指定
                for x in range(len(S)):
                    for z in range(x+1, len(S)):
                        for y in range(z+1, len(S)):
                        
                            # 2つのRのindexが、奇偶異なるものを抽出
                            if S[x] == 'R' and S[y] == 'R' and S[z] == 'K':
                                if x % 2 != y % 2:
                                    ans = "Yes"

# 出力
print(ans)
