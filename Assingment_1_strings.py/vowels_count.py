string = input("Enter string:")
Vowels = 0
for i in string:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
     Vowels+= 1
if Vowels==0:
    print('No Vowels found')
else:
    print("Total number of Vowels are:"+str(Vowels))        

