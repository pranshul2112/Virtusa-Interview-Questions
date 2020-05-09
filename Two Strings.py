
import sys

def twoStrings(s1, s2):
    flag = 0

    for i in s1:
        if i in s2:
            flag = 1
            break
    
    if flag == 0:
        print("NO")

    else:
        print("YES")

q = int(input())

for q_itr in range(q):
        s1 = input()

        s2 = input()

        twoStrings(s1, s2)

