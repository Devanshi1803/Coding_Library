
def reverseWord(s):
    le= len(s)
    l1=[]
    for i in range(le):
        l1.append(s[le-i-1])
    return "".join(l1)


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

