before=input("Enter the sentence you want to make into a Caesar cipher:")
before_num=len(before)


i=0
after=[]
answer=[]

for i in range(before_num):
    
    after.append(before[i])
    
 
base=input("How many letters do you want to shift?:")

for c in after:
    


    
    
    i=ord(c)
    
         
    i2=chr(int(i)+int(base))
    answer.append(i2)

    print(i2,end="")



print("")
