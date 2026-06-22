# Question : Get a number from user and add 2 to that number and print 
# the result.
# Testcase : Input :45 Output 47. 
#  Input:56789 Output:56791

#n = int(input("Enter a number : "))
#op = n + 2
#print("Output : " ,op)

# Question : Get a number from user and subtract 5 to that number and 
# print the result.
# Testcase : Input :45 Output 40. Input: 56789 Output: 56784

#n = int(input("Enter a number : "))
#op = n - 5
#print("Output : " ,op)


# Question : Get a number from user and multiply 3 to that number and 
# print the result.
# Testcase : Input: 45 Output 135. Input: 1200 Output: 3600

#n = int(input("Enter a number : "))
#op = n*3
#print("Output : ",op)

# Question : Get a number from user and divide by the number by 6 and 
# print the quotient.
# Testcase : Input: 45 Output 7. Input: 143 Output: 23

#n = int(input("Enter a number : "))
#op = n%3
#print("Output : ",op)

# Question : Get a number from user and divide by the number by 8 and 
# print the remainder.
# Testcase : Input: 45 Output 5. Input: 143 Output: 7

#n = int(input("Enter a number : "))
#op = n%8
#print("Output : ",op)

# Question : Get a two-digit number from user and print the one’s digit.
# Testcase : Input: 45 Output 5. Input: 56 Output: 6

#n = int(input("Enter a number : "))
#op = n%10
#print("Output : ",op)

# Question : Get a two-digit number from user and print the ten’s digit.
# Testcase : Input: 45 Output 4. Input: 56 Output: 5

#n = int(input("Enter a number : "))
#op = (n//10)% 10
#print("Output : ",op)

# Question : Get a three-digit number from user and print the one’s digit.
# Testcase : Input: 456 Output 6. Input: 569 Output: 9

##n = int(input("Enter a 3 digit number : "))
##op = n%10
##print("Output : ",op)

# Question : Get a three-digit number from user and print the hundred’s 
# digit.
# Testcase : Input: 456 Output 4. Input: 569 Output: 5

##n = int(input("Enter a 3 digit number : "))
##op = int(n/100)
##print("Output : ",op)

# Question : Get a three-digit number from user and print the ten’s digit.
# Testcase : Input: 456 Output 5. Input: 569 Output: 6

##n = int(input("Enter a 3 digit number : "))
##op = int(n/10)%10
##print("Output : ",op)

# Question : Get a two-digit number from user and print sum the digits.
# Testcase : Input: 56 Output 11. Input: 69 Output: 15

##num = int(input("Enter a number: "))
##op = 0
##for i in str(num):
##    op+=int(i)
##print(op)

# Question : Get a three-digit number from user and print sum the digits.
# Testcase : Input: 562 Output 13. Input: 469 Output: 19

##num = int(input("Enter a 3 digit number: "))
##op = 0
##for i in str(num):
##    op+=int(i)    
##print(op)

# Question : Get a two-digit number from user and print the reverse of the 
# number.
# Testcase : Input: 56 Output 65. Input: 59 Output: 95

# num=int(input("Enter a number : "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = (rev*10)+ digit
#     num = num // 10
# print(rev)

# Question : Get a four-digit number from user and only reverse the
# first two digits of the number, then print the number.
# Testcase : Input: 9561 Output 9516. Input: 3859 Output: 3895

# num = int(input("Enter a number: "))
# rev = 0
# for i in str(num):
#     digit = num % 10
#     rev = (rev*10) + digit 
#     num = num // 10
# print(rev)
    
    
# Question : Get a two-digit number from user and make the one’s digit as 
# 0, then print it.
# Testcase : Input: 95 Output 90. Input: 18 Output: 10

# num = int(input("Enter a two digit number: "))
# num = num -(num%10)
# print(num)

# Question : Get a two-digit number from user and make the ten’s digit 1,
# then print it.
# Testcase : Input: 95 Output 15. Input: 82 Output: 12

# n = int(input("Enter a number: "))
# n = (n//10)+(n%10)
# print(n)

# Question : Get a number from user and subtract 5 from that number if 
# the number is odd, then print the result. Do not use “if”. 
# Testcase : Input: 695 Output 690. Input: 182 Output: 182

# n = int(input("Enter a number: "))
# while(n%2!=0):
#     n-=5
# print(n)
    
# Question : Get a number from user and subtract 5 from that number if 
# the number’s ten’s position digit is odd, then print the result. Do not use “if”. 
# Testcase : Input: 685 Output 685. Input: 89172 Output: 89167

# n = int(input("Enter a number: "))
# tenth = (n // 10) % 10
# result = n - 5 * (tenth % 2)
# print(result)

# Get a two digit number from user and subtract 5 from that 
# number if the sum of the digits of the number is odd, then print the result. 
# Do not use “if”.
# Testcase : Input: 95 Output 95. Input: 72 Output: 67


# n = int(input("Enter a number: "))
# dig = (n//10)%10
# op = n-5 *(dig%2)
# print(op)

# Question : Get a two-digit number from user. If the sum of the digits is 10 
# then print “Success”, otherwise print “Failure”.
# Testcase : Input: 56 - Output Failure. Input: 37 - Output: Success.

# n = int(input("Enter a number: "))
# sum = 0
# for i in str(n):
#     sum+=int(i)
# if(sum==10):
#     print("Success")
# else:
#     print("Failure")

# Question : Get a three-digit number from user. If the sum of the digits is 
# 10 then print “Success”, otherwise print “Failure”.
# Testcase : Input: 956 - Output: Failure. Input: 127 - Output: Success.

# n = int(input("Enter a number: "))
# sum = 0
# for i in str(n):
#     sum+=int(i)
# if(sum==10):
#    print("Success")
# else:
#    print("Failure")

# Question : Get a three-digit number from user. If the sum of the one’s 
# digit and hundred’s digit is less than 10, then print “Success”, otherwise print
# “Failure”.
# Testcase : Input: 569 - Output Failure. Input: 316 - Output: Success.

# n= int(input("Enter a number: "))
# sum = 0
# dig = (n//100)+(n%10)
# sum+=dig
# if(sum==10):
#    print("Success")
# else:
#    print("Failure")

# Question : Get a four-digit number from user. If the sum of the ten’s digit 
# and hundred’s digit is greater than 10, then print “Success”, otherwise print
# “Failure”.
# Testcase : Input: 7529 – Output: Failure. Input: 9386 - Output: Success.   
   
# n= int(input("Enter a number: "))
# sum = 0
# dig = (n//100)+(n%10)
# sum+=dig
# if(sum>=10):
#    print("Success")
# else:
#    print("Failure")
   
# Question : Get two 2-digit numbers from user. If the sum of the numbers is 
# less than 100, then print the sum, otherwise print the difference.
# Testcase : Input: 56 78 – Output: 22 Input: 14 65 - Output: 79

# n = int(input("Enter a number: "))
# sum = 0
# for i in str(n):
#     sum+=int(i)
# if (sum<100):
#     print(sum)
# else :
#     print((n//100)-(n%10))
    
# Question : Get two 2-digit numbers from user. Print the sum of digits of 
# the biggest number.
# Testcase : 
# Input: 56 78 – Output: 15
# Input: 14 65 - Output: 11


# n1=int(input("Enter a number1: "))
# n2=int(input("Enter a number2: "))
# sum =0
# if n1>n2:
#     sum+=(n1//100)+(n1%10)   
# else:
#     sum+=(n2//100)+(n2%10)   
# print(sum)
    
# Question : Get two 3-digit numbers from user. Print the difference 
# between the one’s digit and
# hundred’s digit of the number whose ten’s digit is bigger than the other 
# number’s ten’s
# digit
# Testcase : 
# Input: 856 978 – Output: 1
# Input: 128 365 - Output: 2

# n1 = int(input("Enter a number1: "))
# n2 = int(input("Enter a number2: "))

# ten1 = (n1//10)%10
# ten2 = (n2//10)%10

# if(ten1>ten2):
#     print(abs((n1%10)-(n1//100)))
# else:
#     print(abs((n2%10)-(n2//100)))

    
# Question : Get two 3-digit numbers from user. Add the one’s and 
# hundred’s digits of both the numbers. Print the sum of all the digits of the 
# number whose sum of one’s and hundred’s digits is bigger.
# Testcase : 
# Input: 856 978 – Output: 24
# Input: 128 365 - Output: 11

# n1 = int(input("Enter a number1: "))
# n2 = int(input("Enter a number2: "))

# sum1 = (n1//100)+(n1%10)
# sum2 = (n2//100)+(n2%10)
# res = 0
# if sum1>sum2:
#    res = int((n1// 100) + ((n1// 10) % 10) + (n1 % 10))
    
# else:
#     res = int((n2// 100) + ((n2/ 10) % 10) + (n2 % 10))

# print(res)

# Question : Get a three-digit number from user. If the sum of the digits is 
# less than 10, then print the sum, otherwise add the digits of the sum. If the 
# sum of the digits is less than 10, then print the sum, otherwise add the digits 
# of the sum, and print the sum.
# Note: The result should be always single digit only. 
# Testcase :
# Input: 123 – Output: 6
# Input: 149 - Output: 5 (149:1+4+9 = 14: 1+4 = 5)
# Input: 991 - Output: 1 (991: 9+9+1 = 19: 1+9 = 10: 1+0 = 1)

# n = int(input("Enter a number: "))
# sum = int((n// 100) + ((n// 10) % 10) + (n % 10))
# if sum<10:
#     print(sum)
# else:
#     print(int((sum// 100) + ((sum// 10) % 10) + (sum % 10)))
 
# Question : Get a three-digit number from user and print the reverse of the 
# number.
# Testcase : Input: 561 Output 165. Input: 859 Output: 958

# n = int(input("Enter Number: "))
# a = n // 100
# b = (n // 10) % 10
# c = n % 10
# y = c * 100 + b * 10 + a
# print("Result =", y)

# Question : Get a four-digit number from user and only reverse the
# last two digits of the number, then print the number.
# Testcase : Input: 9561 Output 5961. Input: 3859 Output: 8359

# n = int(input("Enter Number: "))
# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
# y = b * 1000 + a * 100 + c * 10 + d
# print("Op =", y)

# Question : Get a three-digit number from user and make the one’s digit 
# as 2, then print it.
# Testcase : Input: 695 Output 692. Input: 182 Output: 182

# x = int(input("Enter Number: "))
# y = (x // 10) * 10 + 2
# print("Op =", y)

# Question : Get a three-digit number from user and make the ten’s digit as 
# 0, then print it.
# Testcase : Input: 695 Output 605. Input: 182 Output: 102

# n = int(input("Enter Number: "))
# hundreds = n // 100
# ones = n % 10
# y = hundreds * 100 + ones
# print("Op =", y)

# Question : Get a three-digit number from user and subtract 5 from that 
# number if one’s digit number and 100’s digit number are same, then print the
# result. Do not use “if”. 
# Testcase : Input: 595 Output 590. Input: 372 Output: 372

# n = int(input("Enter Number: "))
# hundreds = n // 100
# ones = n % 10
# y = n - (hundreds == ones) * 5
# print("Op =", y)

# Question : Get a four-digit number from user and subtract 5 from that 
# number if ten’s digit position and 100’s digit position is same, then print the 
# result. Do not use “if”. 
# Testcase : Input: 7595 Output 7595. Input: 3772 Output: 3767

# n = int(input("Enter Number: "))
# hundreds = (n // 100) % 10
# tens = (n // 10) % 10
# y = n - (hundreds == tens) * 5
# print("Op =", y)

# Question : Get a four-digit number from user. If the sum of the ten’s digit 
# and hundred’s digit is equal to 10, and one of the digits is more than 7 then
# print “Success”, otherwise print “Failure”.
# Testcase : Input: 4649 – Output: Failure. Input: 9286 - Output: Success.

# n = int(input("Enter Number: "))
# hundreds = (n // 100) % 10
# tens = (n // 10) % 10
# if (hundreds + tens == 10) and (hundreds > 7 or tens > 7):
#     print("Success")
# else:
#     print("Failure")