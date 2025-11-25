#과제32
a = {1,2,21,22,20}
b = {11,15,12,24,22}

c = set.union(a,b)
d = set.intersection(a,b)

print(c,d)

#과제33
a = {1,2,21,22,20}
b = {20,15,12,24,22}

c = set.difference(a,b)
d = set.symmetric_difference(a,b)

print(c,d)

#과제34
a = {1,2,21,22,20}
a.update({100})

print(a)

#과제35
a = {100,200,300,400,500}
b = {400,500,600,700,800}

a.intersection_update(b)
print(a)
a.difference_update(b)
print(a)
a.symmetric_difference_update(b)
print(a)

#과제36
a = {100,200,300,400,500}
b = {100,200,300,400,500}

if a.issuperset(b) and a.issubset(b):
    print("동시")
elif a.issuperset(b):
    print("상위")
elif a.issubset(b):
    print("부분")

#과제37
a = {1,2,21,22,20}
a.add(1000)
a.remove(1000)

print(a)

#과제38
multiples = {x for x in range(1,101)if x % 3 == 0 and x % 5 == 0 }
print(multiples)
