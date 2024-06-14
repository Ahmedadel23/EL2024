x=[1,4,6,7,4]
counter=0
put_input=input("enter your input= ")
for i in range (len(x)):
    if(int(x[i])==int(put_input)):
        counter+=1
        
print("number counter = " + str(counter))
