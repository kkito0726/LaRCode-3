"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: https://atcoder.jp/contests/abc289/tasks/abc289_a
"""
s = input()  # sはstr型

T = ""
for i in s:
    if i == "0":
        T += "1"
    elif i == "1":
        T += "0"
print(T)
