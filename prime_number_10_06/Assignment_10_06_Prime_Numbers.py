number = int(input("Please enter your number: "))
prime = []
for num in range(2,number+1):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        prime.append(num)
print(prime)

