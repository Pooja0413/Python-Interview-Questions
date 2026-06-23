# #1. Question : Get a Two-digit number from user and print the digit in “Ones”
# # position
# # Output : 
# # User Enters “78”
# # Answer - 8

# # def main():
# #  x = int(input("Enter Number: "))
# #  y = x%10
# #  print(f"Result = {y}")
# # if __name__ == "__main__":
# #  main()

# #2 Question : Get a Two digit number from user and print the digit in “Tens”
# # position
# # Output : 
# # User Enters “78”
# # Answer - 7

# # def main():
# #  x = int(input("Enter Number: "))
# #  y = x//10
# #  print(f"Result = {y}")
# # if __name__ == "__main__":
# #  main()

# # 3Question :Get a Three digit number from user and print the digit in “Ones”
# # position
# # Output : 
# # User Enters “738”
# # Answer - 8

# # def main():
# #  x = int(input("Enter Number: "))
# #  y = x%10
# #  print(f"Result = {y}")
# # if __name__ == "__main__":
# #  main()
 
# # 4 Get a Three digit number from user and print the digit in “Tens”
# # position
# # Output : 
# # User Enters “738”
# # Answer - 3

# # def main():
# #  x = int(input("Enter Number: "))
# #  y = int((x/10)%10)
# #  print(f"Result = {y}")
# # if __name__ == "__main__":
# #  main()

# #5 Question :Get a Three digit number from user and print the digit in 
# # “Hundreds” position
# # Output : 
# # User Enters “738”
# # Answer - 7

# # def main():
# #  x = int(input("Enter Number: "))
# #  y = x//100
# #  print(f"Result = {y}")
# # if __name__ == "__main__":
# #  main()

# # 6  Question :Get a Two digit number from the user and print the reverse of it.
# # Output : 
# # User Enters “73”
# # Answer - 37

# # def main():
# #  x = int(input("Enter Number: "))
# #  rev = 0
# #  while x > 0:
# #      digit = x % 10
# #      rev = (rev*10)+ digit
# #      x = x // 10
# #  print(f"Result = {rev}")
# # if __name__ == "__main__":
# #  main()




# # Question: Get a Three digit number from the user and
# # print the reverse of it.
# # Example: 738 -> 837


# # def main():
# #     x = int(input("Enter Number: "))
# #     a = x // 100
# #     b = (x // 10) % 10
# #     c = x % 10
# #     y = c * 100 + b * 10 + a
# #     print("Result =", y)
# # if __name__ == "__main__":
# #     main()



# # Question: Get a Four digit number from the user and
# # print the reverse of it.
# # Example: 7384 -> 4837

# def main():
#     x = int(input("Enter Number: "))
#     a = x // 1000
#     b = (x // 100) % 10
#     c = (x // 10) % 10
#     d = x % 10
#     y = d * 1000 + c * 100 + b * 10 + a
#     print("Result =", y)
# if __name__ == "__main__":
#     main()


# #
# # Question: Get a Two digit number from the user and
# # print the sum of all digits.
# # Example: 78 -> 15


# def main():
#     x = int(input("Enter Number: "))
#     y = (x // 10) + (x % 10)
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Get a Three digit number from the user and
# # print the sum of all digits.
# # Example: 738 -> 18
# #

# def main():
#     x = int(input("Enter Number: "))
#     y = (x // 100) + ((x // 10) % 10) + (x % 10)
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Get a Four digit number from the user and
# # print the sum of all digits.
# # Example: 7638 -> 24

# def main():
#     x = int(input("Enter Number: "))
#     y = (x // 1000) + ((x // 100) % 10) + ((x // 10) % 10) + (x % 10)
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Get a number from the user and print the
# # reverse of it.
# # Example: 123456 -> 654321


# def main():
#     x = int(input("Enter Number: "))
#     y = 0
#     while x > 0:
#         digit = x % 10
#         y = y * 10 + digit
#         x = x // 10
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Get a number from the user and print the
# # sum of all digits.
# # Example: 123456 -> 21


# def main():
#     x = int(input("Enter Number: "))
#     y = 0
#     while x > 0:
#         y += x % 10
#         x = x // 10
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print the total number of single digit
# # odd numbers.
# # Answer: 5


# def main():
#     y = 0
#     for i in range(1, 10, 2):
#         y += 1
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print the total number of TWO digit
# # odd numbers.
# # Answer: 45


# def main():
#     y = 0
#     for i in range(11, 100, 2):
#         y += 1
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print the total number of THREE digit
# # odd numbers.
# # Answer: 450

# def main():
#     y = 0
#     for i in range(101, 1000, 2):
#         y += 1
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print the sum of all single digit odd
# # numbers.
# # Answer: 25


# def main():
#     y = 0
#     for i in range(1, 10, 2):
#         y += i
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print the sum of all TWO digit odd
# # numbers.
# # Answer: 2475


# def main():
#     y = 0
#     for i in range(11, 100, 2):
#         y += i
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print the sum of all THREE digit odd
# # numbers.
# # Answer: 247500


# def main():
#     y = 0
#     for i in range(101, 1000, 2):
#         y += i
#     print("Result =", y)
# if __name__ == "__main__":
#     main()



# # Question: Print total number of single digit
# # prime numbers.
# # Answer: 4

# def main():
#     y = 0
#     for i in range(2, 10):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             y += 1
#     print("Result =", y)
# if __name__ == "__main__":
#     main()
    

# Question :Print the number of zeroes you encounter between the numbers 0 
# to 1000

# count = 0
# for i in range(0,1000):
#     count+=str(i).count('0')
# print(count)

# Total number of prime numbers below 1,000,000 have the sum of 
# their digits equal to 14?
# Output : 
# Example: 59. 5 + 9 = 14
# count = 0
# for i in range(2,1000000):
#     for j in range(2, int(i**0.5) + 1):
#         if (i%j==0):
#             break
#     else:
#         digit_sum = sum(int(digit) for digit in str(i))
#         if digit_sum == 14:
#             count += 1
# print(count)

# Question :Print the total number of non-decreasing numbers from 1000 to 
# 9999.Non decreasing numbers have individual digits that do not have a 
# decreasing order from left to right.
# Output : 
# (For e.g.: 1234 is a non-decreasing number 
# where as 2134 is not)
                
# total = 0
# for i in range(1000,10000):
#     n = str(i)
#     if n[0]<=n[1]<=n[2]<=n[3]:
#         total+=1
# print(total)

# Question :Print the total number of all Palindrome numbers less than 
# 100000.
# Output : 
# Example: 101,12321,656,99899,11511
# count = 0
# for i in range(10,100000):
#     if str(i)==str(i)[::-1]:
#         count+=1
# print(count)   

# Question :Get 2 numbers from user and find the LCM of them.
# Output : 
# Example: Input 20,30 Output:60

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# def find_lcm(num1, num2):
#     if num1 == 0 or num2 == 0:
#         return 0
#     greater = max(num1, num2)
#     while True:
#         if greater % num1 == 0 and greater % num2 == 0:
#             return greater
#         greater += 1
# lcm = find_lcm(num1, num2)
# print("The LCM of", num1, "and", num2, "is", lcm)


# # Question :Get a character and print its ASCII Value.

# ch = input("Enter a character: ")
# print(ord(ch))

# Question :Get a number and print its ASCII Value

# num = int(input("Enter a number: "))
# print(ord(str(num)))

# Question :Get a String and print the same.
# string = input("Enter a string: ")
# print(string)

# Question : Get a number as String and print the integer value of the string..
# num_str = input("Enter num as string: ")
# print(int(num_str))

# Question :Get an integer and print it as string
# num = int(input("Enter a number:"))
# s = str(num)
# print(s)
# print(type(s))

# Question :Get an integer and print each digit as character.
# Print one character on one line.

# num = int(input("Enter a number: "))
# for i in str(num):
#     print(i)

# Question :Get a string and find the length of the string
# st = input("Enter a string: ")
# print(len(st)) 

# Question :Get a string and find the length of the string
# Output : 
# E.g.: 1234567 → valid number
# 12abc35 → Not a valid number

# inp = input("Enter a value: ")
# for i in inp:
#     if i not in '0123456789':
#         print("Not a valid number")
#         break
# else:
#     print("Valid number")

# Get a string of numbers up to 50 digits and remove all leading 
# zeros.
# Output : 
# E.g.: 00000012345
# Answer: 12345

