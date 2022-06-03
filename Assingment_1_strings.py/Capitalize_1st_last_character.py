def Capitalize_1st_last_letters(string):
    string = result = string.title( )
    result = " "
    for word in string.split( ):
        result += word [:-1] + word[-1].upper( ) + " "
    return result [:-1]

print(Capitalize_1st_last_letters("we are going to play football"))        
        