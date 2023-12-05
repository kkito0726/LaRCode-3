"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: https://atcoder.jp/contests/abc289/tasks/abc289_a
"""
s = input()

ans = ""
for letter in s:
    if letter == "0":
        ans += "1"
    else:
        ans += "0"
print(ans)