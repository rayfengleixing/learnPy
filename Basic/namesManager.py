print("namesManager V8.6")
print("1.append a name:\n2.remove a name:\n3.update a name:\n4.find a name:\n5.quit:")


names = []

while True:

    num = int(input("input your choice:"))

    if num == 0:
        print(names)
    elif num == 1:
        newName = input("please input the name you want to append:")
        names.append(newName)
        print(names)
    elif num == 2:
        delName = input("please input the name you want to remove:")
        if delName in names:
            names.remove(delName)
            print("remove seccess!")
            print(names)
        else:
            print("%s is not in names!"%delName)
    elif num == 3:
        modifyName = input("please input the name you want to modify:")
        if modifyName in names:
            newOne = input("please input the new name you want:")
            names[names.index(modifyName)] = newOne
            print(names)
        else:
            print("the %s is not in names!"%modifyName)
    elif num == 4:
        findName = input("please input the name you want to find:")
        if findName in names:
            print("the name %s is in!"%findName)
        else:
            print("the name is not in!")
    elif num == 5:
        break
    else:
        print("input error,please input a right num!")

    print("")
