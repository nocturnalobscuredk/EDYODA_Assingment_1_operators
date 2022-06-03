import re

str1 = "welcome@@2ToPython**^"
str2 = "Welcome to python world" 

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:][a-zA-n]')

if(regex.search(str1) == None):
    print("The string is accepted")
else:
    print("The string is not accepted")

     