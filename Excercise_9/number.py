a=int(input('Enter a number:'))
a=a*3+1
sum=0
while a!=0:
    sum=sum+a%10
    a=a//10
    print(sum)