#program to check if a number is prime or not 

num  = int(input("Enter the number"))
#if x > 1:
#   for i in range(2, int(x/2)):  
#       if x%i == 0:
#           print("not a prime number")
#       else:
#            print("its a prime number")
#else: 
#        print("not a prime number")

if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break       
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
