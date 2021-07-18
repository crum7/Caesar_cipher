before=input("シーザー暗号にしたい文を入力してください。:")
before_num=len(before)


i=0
after=[]
answer=[]

for i in range(before_num):
    
    after.append(before[i])
    
 
base=input("いくつ文字をずらしますか？:")

for c in after:
    


    
    
    i=ord(c)
    
         
    i2=chr(int(i)+int(base))
    answer.append(i2)

    print(i2,end="")



print("")
