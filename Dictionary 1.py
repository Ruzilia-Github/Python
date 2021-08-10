dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
result.update(dict1)
for i in dict2:
    result[i] = result.get(i, 0) + dict2[i]



"""
4
Birkan Pen 2
Birkan Pen 2
Ruzilia Book 7
Birkan Book 1
"""

n = int(input())
dic = {}
for i in range(n):
    a, b, c = input().split()
    c = str(c)
    dic.setdefault(a, []).append({b: c})

for i in dic:
    print(i, "EQUAL:", dic[i])
    for x in dic[i]:
        quantity = int(list(x.values())[0])
        item = list(x.keys())[0]
        print(x.get(item))
        print(dic.get(i))


        # dic.get(b).update(a)
        # print("adet", a)
        # print("urun", b)
        # print("kac adet", x.get(b))

    # name=list(dic.keys())[list(dic.values()).index(dic[i])]

#
#     print(f'{dic[i]}:')
print(dic)
# print(dic["Birkan"])
for key in dic.values():
    # print("keys:",key)
    for x in key:
        val = x.values()
        key = x.keys()

        # if key ==x.keys():
        #     print("ok",key,":",x)
        # else:
        #     print("noo",key, ":", x)
        # print(x)
    # print((i.update(i)))

# for i in range(num):
#     a, *b = tuple(input().split())
#     b = tuple(b)
#     dct[b] = a
