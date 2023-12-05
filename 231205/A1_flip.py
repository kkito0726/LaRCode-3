"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: https://atcoder.jp/contests/abc289/tasks/abc289_a
"""

s = input()

ans = []

for i in range(len(s)):
    if s[i] == "0":
        ans.append("1")

    elif s[i] == "1":
        ans.append("0")

ans = "".join(ans)
print(ans)


##### 失敗 #####
# s = int(input())

# l = [int(x) for x in list(str(s))]
# ans = []


# for i in l:
#     if l[i] == 0:
#         ans.append(0)

#     else:
#         ans.append(1)
  
# ans_a = [str(a) for a in ans]
# ans_a = "".join(ans_a)
# print(ans_a)

