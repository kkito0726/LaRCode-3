"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: https://atcoder.jp/contests/abc289/tasks/abc289_a
"""
S = input()
ans = ""
for i in S:
    if i == "0":
        ans += "1"
    else:
        ans += "0"
print(ans)