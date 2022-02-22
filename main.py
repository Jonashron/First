def first():
    name = "Jonah"
    print(name)
    return 0
def second():
    name = "Jonah"
    age = 14
    print(name, " hi! Your age is ", age)
    return 0
def third():
    name = " Jonah"
    name = name * 5
    print(name)
    return 0
def fourth_5():
    name = input("Insert your name - ")
    age = input("Insert your age - ")
    if int(age) > 10:
        print("Hi,",name,"! Joke > 10")
    else:
        print("Hi,",name,"! Joke <= 10")
    return 0
def sixth():
    name = input("Insert your name - ")
    print(name[-2:0:-1])
    print(name[-3:])
    print(name[:5])
    return 0
def seventh():
    name = input("Insert your name - ")
    print(len(name))
    sum = 0
    prod = 1
    for i in range(0, len(name)):
        sum = sum + int(name[i])
        prod = prod * int(name[i])
    print(sum)
    print(prod)
    return 0
def eightth():
    name = input("Insert your name - ")
    print(name.lower())
    print(name.upper())
    return 0
def ninth():
    ans = input("2+2*2 = ")
    if int(ans) != 6:
        print("wrong")
    else:
        print("right")
    return 0
ninth()