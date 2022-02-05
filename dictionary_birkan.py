# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
# using dict()
my_dict = dict({1:'apple', 2:'ball'})
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)])
#george
res = list(mydict.keys()).index("george")
print(res)#0 index

dic_a={}
# Adding the first element
dic_a['A'] = 'Apple'
print (dic_a)
# >>> {'A': 'Apple'}
# Adding the second element
dic_a['B'] = 'Ball'
# print (dic_a)
# >>> {'A': 'Apple', 'B': 'Ball'}


dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
for key, value in dic_a.items():
    print (key, value)
# >>> A Apple
#     B Ball
#     C Cat


dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
list(dic_a.keys())[0]
# >>> 'A'
list(dic_a.keys())[-1]
# >>> 'C'
list(dic_a.values())[0]
# >>> 'Apple'
list(dic_a.values())[-1]
# >>> 'Cat'

a=-1
data = {'george': [16,45] ,'amber': [19,76]}
for i in data.keys():
    a = a + 1
    test = list(data.values())[a][1]  # slow
    print(test)  # slow
# 45
# 76
r = []
for k, v in data.items():
    title_list = v[0]  # value first
    r.append(title_list)



def method3(list,search_age):
    return list.keys()[list.values().index(search_age)]

d={"iki":2,"uc":3,"dort":4,"bes":5 }
#add item
d['bir'] = 1

vals = dict(one=1, two=2)#{'two': 2, 'one': 1}
#get item
print(d['bir'])# None if dont find
print(d.get('iki'))#erorr if dont find
#for
for item in d.items():
    print(item)
# ('iki', 2)
# ('uc', 3)
# ('dort', 4)
# ('bes', 5)
# ('bir', 1)

print(list(sorted(d.keys())))#['bes', 'bir', 'dort', 'iki', 'uc']

#delete
del d["uc"]
print(d)#{'iki': 2, 'dort': 4, 'bes': 5, 'bir': 1}
print(d.pop("bir"))#1
print(d)#{'iki': 2, 'dort': 4, 'bes': 5}
print(d.popitem())#('bes', 5)
print(d)#{'iki': 2, 'dort': 4}
d.clear()
print(d)#{}
datam = {"a":"test","b":"test"}
datam2 = {"a":"test","b":"test","keep":"test"}
for i in datam.keys():
    #print(i)
    del datam2[i]
print(datam2)
#{'keep': 'test'}


# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)# Output: True
print(2 not in squares)# Output: True
print(49 in squares)# Output: False

# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
# 1
# 9
# 25
# 49
# 81

# Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(all(squares))# Output: False
print(any(squares))# Output: True
print(len(squares))# Output: 6
print(sorted(squares))# Output: [0, 1, 3, 5, 7, 9]


dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
dic_b = {'D':'Dog', 'E':'Egg'}
dic_a.update(dic_b)
print(dic_a)
# >>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog', 'E': 'Egg'}

capitals = { "Bratislava": 424207, "Vilnius": 556723, "Lisbon": 564657,
             "Riga": 713016, "Jerusalem": 780200, "Warsaw": 1711324,
             "Budapest": 1729040, "Prague": 1241664, "Helsinki": 596661,
             "Yokyo": 13189000, "Madrid": 3233527 }
capitals = { key:val for key, val in capitals.items() if val < 1000000 }
#{'Bratislava': 424207, 'Vilnius': 556723, 'Jerusalem': 780200, 'Riga': 713016,'Lisbon': 564657, 'Helsinki': 596661}

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary"}
domains2 = { "us": "United States", "no": "Norway" }
domains.update(domains2)
#{'sk': 'Slovakia', 'de': 'Germany', 'no': 'Norway','us': 'United States', 'hu': 'Hungary'}


#setdefault-----------------------------
#print(fruits.setdefault('oranges', 11))
#print(fruits.setdefault('kiwis', 11))
#{'bananas': 0, 'pears': 0, 'oranges': 12, 'apples': 0}
#{'kiwis': 11, 'bananas': 0, 'pears': 8, 'oranges': 12, 'apples': 4}# kivi was not her thats why kiwi add but orange not update


domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway" }
for key in domains:
    print(key)
for val in domains.values():
    print(val)
for k, v in domains.items():
    print(": ".join((k, v)))

dic_a = {'A': 'Apple', 'B': 'Ball'}
dic_b = {'C': 'Cat', 'D': 'Dog'}
dic_merged = {**dic_a, **dic_b}
print (dic_merged)
# >>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway"  }
key = "sk"
if key in domains:
    print("{0} is in the dictionary".format(domains[key]))

#sort
items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }
kitems = list(items.keys())
kitems.sort()

#sort value
items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }
for key, value in sorted(items.items(), key=lambda pair: pair[1]):
    print("{0}: {1}".format(key, value))
print("###############")
for key, value in sorted(items.items(), key=lambda pair: pair[1], reverse=True):
    print("{0}: {1}".format(key, value))




# bags: 1
# cups: 2
# pens: 3
# bottles: 4
# books: 5
# coins: 7
# ###############
# coins: 7
# books: 5
# bottles: 4
# pens: 3
# cups: 2
# bags: 1

