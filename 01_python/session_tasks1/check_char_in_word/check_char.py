s_str:str="ahmed"
put_input=input("enter the character: ")
for i in range(len(s_str)):
    if(s_str[i]==put_input):
        print("char is found")
        break
else:
    print("char isn't found")