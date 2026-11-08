# Python set demo
s1 = {1, 2, 3, 3, 4}
print("s1:", s1)

s2 = set()
s2.add(5)
s2.add(6)
print("s2:", s2)

lst = [1, 1, 2, 2, 7]
s3 = set(lst)
print("s3:", s3)

s4 = {x for x in range(10) if x % 2 == 1}
print("s4:", s4)