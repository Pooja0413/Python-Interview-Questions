
# # Question:
# # Get a number from user and add 2 to that number and print
# # the result. Write your code inside the function.
# #
# # Input : 45     Output : 47
# # Input : 56789  Output : 56791

# def function(no1):
#     no2 = 0
#     no2 = no1 + 2
#     return no2

# def main():
#     number1 = int(input("Enter a number: "))
#     number2 = function(number1)
#     print(number2)

# if __name__ == "__main__":
#     main()


# #
# # Question:
# # Get a number from user and subtract 5 from that number and
# # print the result. Write your code inside the function.
# #
# # Input : 45     Output : 40
# # Input : 56789  Output : 56784

# def function(no1):
#     no2 = 0
#     no2 = no1 - 5
#     return no2

# def main():
#     number1 = int(input("Enter a number: "))
#     number2 = function(number1)
#     print(number2)

# if __name__ == "__main__":
#     main()



# # Question:
# # Get a number from user and Check whether the sum of digits
# # is 14 and print the result.
# #
# # Input : 59   Output : Sum of Digits is 14
# # Input : 123  Output : Sum of Digits is not 14
# #
# def sum14(no):

#     total = 0

#     while no > 0:
#         total += no % 10
#         no //= 10

#     if total == 14:
#         return 1
#     else:
#         return 0

# def main():
#     number = int(input("Enter a number: "))
#     result = sum14(number)

#     if result == 1:
#         print("Sum of Digits is 14")
#     else:
#         print("Sum of Digits is not 14")

# if __name__ == "__main__":
#     main()



# # Question:
# # Get a number from user and Check Prime or Not and print
# # the result.
# #
# # Input : 61   Output : Number is Prime
# # Input : 1200 Output : Number is not Prime
# #

# def is_prime(number):

#     if number < 2:
#         return False

#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False

#     return True

# def main():

#     number = int(input("Enter a number: "))

#     result = is_prime(number)

#     if result:
#         print("Number is Prime")
#     else:
#         print("Number is not Prime")

# if __name__ == "__main__":
#     main()



# # Question:
# # Get a number from user and count the number of zeros in
# # that number and print.
# #
# # Input : 100      Output : 2
# # Input : 1060030  Output : 4


# def find_number_of_zeros(number):

#     count = 0

#     while number > 0:
#         if number % 10 == 0:
#             count += 1

#         number //= 10

#     return count

# number = int(input("Enter a number: "))

# result = find_number_of_zeros(number)

# print(result)



# # Question:
# # Get a number from user and reverse that number and print.
# #
# # Input : 123    Output : 321
# # Input : 56789  Output : 98765

# def reverse_number(number):

#     reverse = 0

#     while number > 0:
#         digit = number % 10
#         reverse = reverse * 10 + digit
#         number //= 10

#     return reverse

# def main():

#     number = int(input("Enter a number: "))

#     result = reverse_number(number)

#     print(result)

# if __name__ == "__main__":
#     main()



# # Question:
# # Get two numbers from user and compare the numbers.
# # If same print "Same" otherwise print "Not Same".
# #
# # Input : 123,123      Output : Same
# # Input : 56789,12345  Output : Not Same


# def function(no1):

#     no2 = int(input("Enter second number: "))

#     if no1 == no2:
#         return "Same"
#     else:
#         return "Not Same"

# def main():

#     number1 = int(input("Enter first number: "))

#     number2 = function(number1)

#     print(number2)

# if __name__ == "__main__":
#     main()



# # Question:
# # Get a number from user and check whether the digits are
# # in ascending order.
# #
# # Input : 1234  Output : Yes
# # Input : 5687  Output : No


# def check_assending(no):

#     num = str(no)

#     for i in range(len(num) - 1):
#         if num[i] >= num[i + 1]:
#             return "No"

#     return "Yes"

# def main():

#     number1 = int(input("Enter a number: "))

#     result = check_assending(number1)

#     print(result)

# if __name__ == "__main__":
#     main()



# # Question:
# # Get a two-digit number from user and swap the digits.
# #
# # Input : 34  Output : 43
# # Input : 56  Output : 65


# def swapNumbers(no):

#     tens = no // 10
#     ones = no % 10

#     return ones * 10 + tens

# def main():

#     number1 = int(input("Enter a number: "))

#     result = swapNumbers(number1)

#     print(result)

# if __name__ == "__main__":
#     main()



# # Question:
# # Get a number from user, find the number of digits and
# # print the same.
# #
# # Input : 34678     Output : 5
# # Input : 12345678  Output : 8

# def count_Digits(no):
#     count = 0
#     while no > 0:
#         count += 1
#         no //= 10
#     return count

# def main():

#     number1 = int(input("Enter a number: "))

#     result = count_Digits(number1)

#     print(result)

# if __name__ == "__main__":
#     main()