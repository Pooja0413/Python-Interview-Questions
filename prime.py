# "Prime Numbers
# 1.Given a number N, determine whether it is prime or not.
# 2.Display all prime numbers between 1 and 20.
# 3.Count Prime Numbers Between 1 and N
# 4.Print First N Prime Numbers
# 5.Sum of Prime Numbers up to N
# 6.Find Largest Prime Less Than N
# 7.Find Smallest Prime Greater Than N
# 8.Prime Numbers in a Range ( ex: 10 to 30 ) print prime number
# between 10 to 30.


# 1.Prime or Not

# n = int(input("Enter a number:"))
# if n<=1:
#     print("Not Prime")
# else:
#     for i in range(2,n):
#         if (n%i==0):
#             print("Not prime")
#             break
#     else:
#         print("Prime")

# 2.Prime 2 to 20
# for i in range(2,20):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         print(i)

# 3.Count prime between 1 to N

# N = int(input("Enter a number to count prime:"))
# count = 0
# for i in range(2,N):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         count+=1
# print("Prime count:",count)

# 4.Print first N prime

# N = int(input("Enter a number to print prime:"))
# for i in range(2,N):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         print(i)

# 5.Sum of prime

# N= int (input("Enter a number to print sum of prime:"))
# sum=0
# for i in range(2,N):
#     for j in range(2,i):
#        if (i%j==0):
#            break
#     else:
#         sum+=i        
# print("The sum of prime numbers is",sum)

# 6.Largest prime less than N
# N = int(input("Enter a number to find largest prime :"))
# largest_prime = 0 
# for i in range(2,N):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         largest_prime = i
# print("The largest prime less than",N,"is ",largest_prime)

# 7.Smallest prime greater than N

# N = int(input("Enter a number to find smallest prime: "))
# for i in range(N + 1, N * 2):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         smallest_prime = i
#         break
# print("The smallest prime greater than", N, "is", smallest_prime)

# 8.Prime number between 10 to 30

# for i in range(10, 31):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)