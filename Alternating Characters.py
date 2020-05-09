
def alter(s):
    n = len(s)

    if n < 2:
        return s

    j = 0
    for i in range(n):
        if s[j] != s[i]:
            j += 1
            s[j] = s[i]

    j += 1
    return n - j


t = int(input())
for t_tr in range(t):
    s = input()
    s = list(s.rstrip())
    print(alter(s))
