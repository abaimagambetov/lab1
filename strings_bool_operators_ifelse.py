# strings
# 1
x = "Hello World"
print(len(x))
# 2
txt = "Hello World"
x = txt[0]
# 3
txt = "Hello World"
x = txt[2:5]
# 4
txt = " Hello World "
x = txt.strip()
# 5
txt = "Hello World"
txt = txt.upper()
# 6
txt = "Hello World"
txt = txt.lower()
# 7
txt = "Hello World"
txt = txt.replace('H', 'J')
# 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# bool
# 1
print(10 > 9)
true
# 2
print(10 == 9)
false
# 3
print(10 < 9)
false
# 4
print(bool("abc"))
true
# 5
print(bool(0))
false


# operators
# 1
print(10 * 5)
# 2
print(10 / 2)
# 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
# 4
if 5 != 10:
    print("5 and 10 is not equal")
# 5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")


# if else
# 1
a = 50
b = 10
if a > b:
    print("Hello World")
# 2
a = 50
b = 10
if a != b:
    print("Hello World")
# 3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
# 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
# 5
if a == b and c == d:
    print("Hello")
# 6
if a == b or c == d:
    print("Hello")
# 7
if 5 > 2:
    print("Five is greater than two!")
# 8
if 5 > 2: print("Five is greater than two!")
# 9
print("Yes") if 5 > 2 else print("No")
