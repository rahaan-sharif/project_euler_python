length=4000000

sum=0
i=[1, 2]
sum+=i[1]
while i[1]<length:
    j=i[0]
    k=i[1]
    i[1]=j+k
    i[0]=k
    print(i[1])
    if i[1]%2==0:
        sum+=i[1]
print("output: ", sum)
