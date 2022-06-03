def string_cast(string):
    k={"count1":0, "count2":0}
    
    for char in string:
        if char.isupper():
            k["count1"]+= 1
        elif char.islower():
            k["count2"]+= 1
        else:
            pass

    print("Original string:", string)

    print("The number of uppercase Character is:", k["count1"])

    print("The number of lowercase Characteris:", k["count2"])

string_cast('The Sun Rises In THe East')
