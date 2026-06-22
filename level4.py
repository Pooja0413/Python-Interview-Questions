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
    

# # Question: Print the total number of TWO digit
# # prime numbers.


# count = 0
# for i in range(10, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         count += 1
# print("Problem 21 Answer =", count)



# # Question: Print the total number of THREE digit
# # prime numbers.


# count = 0
# for i in range(100, 1000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         count += 1
# print("Problem 22 Answer =", count)



# # Question: Print the sum of single digit
# # prime numbers.


# sum = 0
# for i in range(2, 10):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         sum += i
# print("Problem 23 Answer =", sum)



# # Question: Print the sum of all TWO digit
# # prime numbers.


# sum = 0
# for i in range(10, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         sum += i
# print("Problem 24 Answer =", sum)



# # Question: Print the sum of all THREE digit
# # prime numbers.


# sum = 0
# for i in range(100, 1000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         sum += i
# print("Problem 25 Answer =", sum)



# # Question: Print the smallest Three digit
# # prime number.


# for i in range(100, 1000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print("Problem 26 Answer =", i)
#         break



# # Question: Print the largest Three digit
# # prime number.


# for i in range(999, 99, -1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print("Problem 27 Answer =", i)
#         break



# # Question: Print the smallest Four digit
# # prime number.


# for i in range(1000, 10000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print("Problem 28 Answer =", i)
#         break



# # Question: Print the largest Four digit
# # prime number.


# for i in range(9999, 999, -1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print("Problem 29 Answer =", i)
#         break



# # Question: Print the largest Eight digit
# # prime number.


# for i in range(99999999, 9999999, -1):
#     flag = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         print("Problem 30 Answer =", i)
#         break