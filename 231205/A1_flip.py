"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: https://atcoder.jp/contests/abc289/tasks/abc289_a
"""
s = input()  # sはstr型


S = ""
for i in s :
    if i == "0" :
        S += "1"
    elif i == "1" :
        S += "0"
print(S)
