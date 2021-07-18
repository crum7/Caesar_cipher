before=input("シーザー暗号を入力してください。:")
before_num=len(before)


i=0
after=[]
answer=[]

for i in range(before_num):
    
    after.append(before[i])
    
 
base=input("入力した文字の最初の文字を、どのアルファベットにしますか？:")
base=ord(base)
original=ord(after[0])
result=original-base



for c in after:
    
    a=c.isalnum()
    if a==False:
        print(c,end="")
        answer.append(c)

    else:
    
        i=ord(c)
    
         
        i2=chr(int(i)-result)
        answer.append(i2)

        print(i2,end="")



print("")
