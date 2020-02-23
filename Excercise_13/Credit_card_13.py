L=[]
a=int(input('Please enter your credit card number (16 digits) and then, press ENTER:'))
while a!=0:
    x=a%10
    L.append(x)
    a=a//10
for i in range(0,9):
        temp=L[i]
        L[i]=L[15-i]
        L[15-i]=temp

        sum=0
for i in range(0,16):
   if i%2!=0:
        sum=sum+L[i]
   else:
         if L[i]*2>=10:
                sum=sum+L[i]*2-9
         else:
                sum=sum+L[i]*2
if sum %10==0:
        print('Valid card')
else:
        print('Invalid card')
