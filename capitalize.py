txt = "hello, and welcome to my world!";
x = txt.capitalize()
print(x)

txt2 = "Hello, And Welcome to my World!"
y = txt2.casefold()
print(y)

fruit = "Banana"
b = fruit.center(50)
print(b)

favoriteFruits = "I love apple, apple is my favorite fruit."
apleCount = favoriteFruits.count("apple")
print(apleCount)

# endswith specific position

endw = "Hello, welcome to my world"
rslt = endw.endswith("my world", 5,31)
print(rslt)