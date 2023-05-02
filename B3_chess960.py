'''
AtCoder Beginner Contest 297
https://atcoder.jp/contests/abc297/tasks/abc297_b
B問題
'''

str_list = list(input())  # n個の文字列がリストに格納される
#print(str_list)

list1 = []
list2 = []


for i,s in enumerate(str_list):
    if s == "B":
        list1.append(i+1)
    if s == "R":
        list2.append(i+1)
    if s == "K":
        int_K = i+1

if (list1[0] + list1[1])%2 != 0 and list2[0]< int_K and int_K < list2[1]:
    print("Yes")
else:
    print("No")




