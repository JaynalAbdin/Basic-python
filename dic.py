# def myFunc(e):
#     return e[m]

dic = {'a':1,'b':4,'c':1,'g':1,'m':2, 't':1, 'd':5}

items = list(dic.items())
n = len(items)

for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1]<items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]



for key, value in items:
    print(key,value)

# m = list(dic.values())
# m.sort(reverse=True)
# print(m)
# # print(m)
# # srt = {i: dic[i] for i in m}
# # print(srt)
# dic2 = dict(sorted(dic.items(), key=lambda keyItems: keyItems[1], reverse=True))
# print(dic2)
