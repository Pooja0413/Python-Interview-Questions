
# # Question:
# # Write a loop program to print 1 to 5 one by one.

# # for i in range(1, 6):
# #     print(i)




# # Question:
# # Write a loop program to print 5 to 1 one by one.

# # for i in range(5, 0, -1):
# #     print(i)




# # Question:
# # Write a loop program to print sum of 1 to 5.

# # total = 0
# # for i in range(1, 6):
# #     total += i
# # print(total)




# # Question:
# # Write a loop program to print sum of 6 to 1.

# # total = 0
# # for i in range(6, 0, -1):
# #     total += i
# # print(total)




# # Question:
# # Write a loop program to print odd numbers 1 to 9.

# # for i in range(1, 10, 2):
# #     print(i)




# # Question:
# # Write a loop program to print the two-digit odd numbers,
# # below 20.

# # for i in range(11, 20, 2):
# #     print(i)




# # Question:
# # Write a loop program to print the two-digit odd numbers
# # whose sum of digits is 7.

# # for i in range(11, 100, 2):
# #     if (i // 10) + (i % 10) == 7:
# #         print(i)




# # Question:
# # Write a loop program to print the two-digit even numbers
# # whose sum of digits is 6.

# # for i in range(10, 100, 2):
# #     if (i // 10) + (i % 10) == 6:
# #         print(i)




# # Question:
# # Write a loop program to print the sum of two-digit numbers
# # whose one's digit is 5.

# # total = 0
# # for i in range(15, 100, 10):
# #     total += i
# # print(total)



# # Question:
# # Write a loop program to print the sum of two-digit odd
# # numbers whose ten's digit is 7.

# # total = 0
# # for i in range(71, 80, 2):
# #     total += i
# # print(total)



# # Question:
# # Write a program to get a number from user and print
# # the total number of digits in that number.
# #
# # Input : 123456 -> Output : 6
# # Input : 76895439 -> Output : 8
# # Input : 675 -> Output : 3

# # n = int(input("Enter Number: "))
# # count = 0
# # while n > 0:
# #     count += 1
# #     n //= 10
# # print(count)



# # Question:
# # Write a program to get a number from user and print
# # the sum of all digits.
# #
# # Input : 123456 -> Output : 21
# # Input : 76895439 -> Output : 51
# # Input : 675 -> Output : 18

# # n = int(input("Enter Number: "))
# # total = 0
# # while n > 0:
# #     total += n % 10
# #     n //= 10
# # print(total)



# # Python Level 2 | Problem 13
# # Question:
# # Write a program to get a number from user and print
# # the reverse of that number.
# #
# # Input : 123456 -> Output : 654321
# # Input : 76895439 -> Output : 93459867
# # Input : 675 -> Output : 576

# # n = int(input("Enter Number: "))
# # rev = 0
# # while n > 0:
# #     digit = n % 10
# #     rev = rev * 10 + digit
# #     n //= 10
# # print(rev)



# # Question:
# # Write a program to get a number from user and interchange
# # the first and last digits and print the result.
# #
# # Input : 123456 -> Output : 623451
# # Input : 76895439 -> Output : 96895437
# # Input : 675 -> Output : 576

# # n = input("Enter Number: ")
# # result = n[-1] + n[1:-1] + n[0]
# # print(result)



# # Question:
# # Get a number from user and if the first digit is odd,
# # subtract 1 from the first digit and print the result.
# #
# # Input : 123456 -> Output : 023456
# # Input : 96895439 -> Output : 86895439
# # Input : 675 -> Output : 675
# # Input : 575 -> Output : 475

# # n = input("Enter Number: ")
# # first = int(n[0])
# # if first % 2 != 0:
# #     first -= 1
# # result = str(first) + n[1:]
# # print(result)


# # Question:
# # Write a program get number from user print whether that
# # number is prime or not.
# #
# # Input : 31 -> Prime
# # Input : 27 -> Not Prime


# # n = int(input("Enter Number: "))
# # is_prime = True
# # if n < 2:
# #     is_prime = False
# # else:
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if n % i == 0:
# #             is_prime = False
# #             break
# # if is_prime:
# #     print("Prime")
# # else:
# #     print("Not Prime")



# # Question:
# # Write a program to get a number from user, print whether
# # that number is prime, and sum of digits is equal to 14.


# # n = int(input("Enter Number: "))
# # temp = n
# # digit_sum = 0
# # while temp > 0:
# #     digit_sum += temp % 10
# #     temp //= 10
# # is_prime = True
# # if n < 2:
# #     is_prime = False
# # else:
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if n % i == 0:
# #             is_prime = False
# #             break
# # if is_prime and digit_sum == 14:
# #     print("Prime & Sum of Digits is 14")
# # elif not is_prime and digit_sum == 14:
# #     print("Not Prime but Sum of Digits is 14")
# # elif is_prime:
# #     print("Prime but Sum of Digits is not 14")
# # else:
# #     print("Not Prime and Sum of Digits is not 14")



# # Question:
# # Print whether last two digits are prime.
# #
# # Input : 359 -> Prime (59)
# # Input : 3577 -> Not Prime (77)

# # n = int(input("Enter Number: "))
# # last_two = n % 100
# # is_prime = True
# # if last_two < 2:
# #     is_prime = False
# # else:
# #     for i in range(2, int(last_two ** 0.5) + 1):
# #         if last_two % i == 0:
# #             is_prime = False
# #             break
# # if is_prime:
# #     print("Prime")
# # else:
# #     print("Not Prime")



# # Question:
# # Get a 4-digit number and check whether the middle
# # two digits form a prime number.
# #
# # Input : 6359 -> Not Prime (35)
# # Input : 3517 -> Prime (51? as per PDF example)


# # n = input("Enter 4 Digit Number: ")
# # middle = int(n[1:3])
# # is_prime = True
# # if middle < 2:
# #     is_prime = False
# # else:
# #     for i in range(2, int(middle ** 0.5) + 1):
# #         if middle % i == 0:
# #             is_prime = False
# #             break
# # if is_prime:
# #     print("Prime")
# # else:
# #     print("Not Prime")



# # Question:
# # Print total number of single digit prime numbers.
# #
# # Output : 4


# # count = 0
# # for i in range(1, 10):
# #     is_prime = True
# #     if i < 2:
# #         is_prime = False
# #     else:
# #         for j in range(2, i):
# #             if i % j == 0:
# #                 is_prime = False
# #                 break
# #     if is_prime:
# #         count += 1
# # print(count)



# # Question:
# # Print total number of odd digits in a number.
# #
# # Input : 12345678 -> 4
# # Input : 987531 -> 5


# # n = input("Enter Number: ")
# # count = 0
# # for digit in n:
# #     if int(digit) % 2 != 0:
# #         count += 1
# # print(count)



# # Question:
# # Print total number of odd digits in a number.
# #
# # Input : 12345678 -> 3
# # Input : 987531 -> 4

# # n = input("Enter Number: ")
# # count = 0
# # for digit in n:
# #     if int(digit) % 2 != 0:
# #         count += 1
# # print(count)



# # Question:
# # Print total number of single-digit perfect squares.
# #
# # Input : 123456789 -> 3
# # Input : 987531 -> 2


# # n = input("Enter Number: ")
# # count = 0
# # for digit in n:
# #     if int(digit) in [1, 4, 9]:
# #         count += 1
# # print(count)


# # Question:
# # Write a program get number from user print the total
# # number of two-digit perfect square numbers in the number.
# #
# # Input: 163496481 -> Output: 4
# # Input: 364925 -> Output: 4

# n = input("Enter Number: ")
# count = 0
# for i in range(len(n) - 1):
#     num = int(n[i:i+2])
#     root = int(num ** 0.5)
#     if root * root == num:
#         count += 1
# print(count)



# # Question:
# # Write a program get number from user print the total
# # number of single-digit prime numbers in the number.
# #
# # Input: 163496481 -> Output: 1
# # Input: 364925 -> Output: 3


# n = input("Enter Number: ")
# count = 0
# for digit in n:
#     if int(digit) in [2, 3, 5, 7]:
#         count += 1
# print(count)



# # Question:
# # Write a program to print biggest 4-digit number which
# # is divisible by 7 and 9.


# for i in range(9999, 999, -1):
#     if i % 7 == 0 and i % 9 == 0:
#         print(i)
#         break



# # Question:
# # Write a program to print the total count of numbers
# # less than 100000 whose sum of digits is 14.


# count = 0
# for num in range(1, 100000):
#     temp = num
#     digit_sum = 0
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
#     if digit_sum == 14:
#         count += 1
# print(count)



# # Question:
# # Write a program to get two numbers from user and
# # print the LCM of those numbers.


# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# greater = max(a, b)
# while True:
#     if greater % a == 0 and greater % b == 0:
#         print(greater)
#         break
#     greater += 1



# # Question:
# # Write a program to get three numbers from user and
# # print the LCM of those numbers.


# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))
# greater = max(a, b, c)
# while True:
#     if greater % a == 0 and greater % b == 0 and greater % c == 0:
#         print(greater)
#         break
#     greater += 1



# # Question:
# # Write a program to get two numbers from user and
# # print the HCF of those numbers.


# # a = int(input("Enter First Number: "))
# # b = int(input("Enter Second Number: "))
# # hcf = 1
# # for i in range(1, min(a, b) + 1):
# #     if a % i == 0 and b % i == 0:
# #         hcf = i
# # print(hcf)