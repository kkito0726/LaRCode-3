'''
AtCoder Beginner Contest 314
URL: https://atcoder.jp/contests/abc314/tasks/abc314_b
B問題
'''

# 入力
N = int(input())

C = []
A = []

for i in range(N):
    C.append(int(input()))
    A.append(list(map(int, input().split())))

X = int(input())

# 出力
C_min = 100
ans = []

for j in range(N):

    # XがA内にある
    if X in A[j]:

        # Cが最小値
        if C[j] < C_min:

            C_min = C[j]

            # 新たな最小値が見つかったらansリストをクリアして追加
            ans = []
            ans.append(j+1)
            
        # Cが最小値と同値
        elif C[j] == C_min:
            ans.append(j+1)

print(len(ans))
print(*ans)



