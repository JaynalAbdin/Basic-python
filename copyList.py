print("Copying list items")

lst1 = ['a', 'b', 'c']
lst2 = [1,2,3]
for x in lst2:
    lst1.append(x)
print(lst1)

# type2
print("Using Operator")
list1 = ["Jaynal", "Love", "Cricket"]
list2 = ["Abdin", "Love", "Football"]
list3 = list1+list2
print(list3)

print("Using extend")

lst1.extend(list2)
print(lst1)