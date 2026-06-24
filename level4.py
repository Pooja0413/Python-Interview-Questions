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

# num = input("Enter a number: ")
# result = num.lstrip('0')
# if result == "":
#     result = "0"

# print("Answer:", result)

# Question :Get a number up to 50 digits and reverse it.
# Output : 
# E.g.: 12345678912345
# Answer: 54321987654321

# Question :set a number up to 50 digits and reverse it.
# Output : 
# E.g.: 12345678912345
# Answer: 54321987654321
# num = input("Enter Number: ")
# print("Result =", num[::-1])

# Question : Get a number string up to 50 digits and convert it to integer array.
# num = input("Enter Number: ")
# arr = [int(i) for i in num]
# print("Result =", arr)

# # Question :Add two integer arrays of up to 50 digits and store the result in a 
# 51 digits array
# a = list(map(int, input("Enter First Array: ").split()))
# b = list(map(int, input("Enter Second Array: ").split()))

# Question :Adjust the carry in an integer array. (i.e. convert the 2 digit number
# into single digit and add the carry to the next number)
# Output : 
# E.g.: Array - 6 12 3 15 7
# Answer: 7 2 4 5 7
# result = []
# for i in range(len(a)):
#     result.append(a[i] + b[i])

# print("Result =", result)

# Question :Write a function to convert an integer array to a character array 
# and print it.
# Output : 
# Array – 1 4 5 8 7 6 3
# Answer: 1458763
# arr = list(map(int, input("Enter Array: ").split()))

# for i in range(len(arr) - 1):
#     arr[i + 1] += arr[i] // 10
#     arr[i] %= 10

# print("Result =", arr)

# Question :Get two numbers of up to 50 digits and perform addition and
# print the result.
# arr = list(map(int, input("Enter Array: ").split()))

# result = ""
# for i in arr:
#     result += str(i)

# print("Result =", result)

# Question :Get a string and a character from the user and find all the 
# positions where the character present and print it.
# Output : 
# E.g.: string : hellohellohello
# character : h
# Answer : 1, 6, 11
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))

# print("Result =", num1 + num2)

# Question :Get a main string and sub string. Check the sub string in main 
# string an print the position.
# Output : 
# E.g.: string : hellosurabee
# substring : sura
# Answer : 6
# s = input("Enter String: ")
# ch = input("Enter Character: ")

# for i in range(len(s)):
#     if s[i] == ch:
#         print(i + 1, end=" ")

# print()


# s = input("Enter Main String: ")
# sub = input("Enter Sub String: ")
# print("Result =", s.find(sub) + 1)

# Question :Get a string using gets function and count all the words in it.
# Output : 
# E.g.: string : Welcome to HCL Tech
# Answer : 4
# s = input("Enter String: ")
# words = s.split()
# print("Result =", len(words))

# Question :Write a program to multiply up to two 50 digit numbers.
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# print("Result =", num1 * num2)




# Question :Create a linked list using a class-based structure to store student 
# information. The structure should include the student's ID, Maths mark, and 
# Science mark. Implement a program that continuously accepts user inputs 
# for these values. When the user inputs an ID of -1, the input mode should 
# exit, and the program should display all the entries.
# class Node:
#     def __init__(self, sid, maths, science):
#         self.sid = sid
#         self.maths = maths
#         self.science = science
#         self.next = None


# head = None
# tail = None

# while True:

#     sid = int(input("Enter ID (-1 to stop): "))

#     if sid == -1:
#         break

#     maths = int(input("Enter Maths Mark: "))
#     science = int(input("Enter Science Mark: "))

#     newnode = Node(sid, maths, science)

#     if head is None:
#         head = tail = newnode
#     else:
#         tail.next = newnode
#         tail = newnode

# temp = head

# while temp:
#     print(temp.sid, temp.maths, temp.science)
#     temp = temp.next

# # =========================
# # Linked List Insert After ID
# # =========================
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)

# target = int(input("Enter Target ID: "))
# newdata = int(input("Enter New Value: "))

# temp = head

# while temp:
#     if temp.data == target:
#         newnode = Node(newdata)
#         newnode.next = temp.next
#         temp.next = newnode
#         break

#     temp = temp.next

# temp = head
# while temp:
#     print(temp.data, end=" ")
#     temp = temp.next

# print()

# Question :Create a sample link list with about 5 entries using the class. 
# Insert a new entry before or after a given id.
# Menu Items
# 1. Insert Entry
# 2. Display List
# 3. Exit

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

delete_id = int(input("Enter Value To Delete: "))

if head.data == delete_id:
    head = head.next
else:
    temp = head

    while temp.next:
        if temp.next.data == delete_id:
            temp.next = temp.next.next
            break

        temp = temp.next

temp = head
while temp:
    print(temp.data)
    temp = temp.next

# =========================
# Doubly Linked List
# =========================
# class DNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# head = DNode(10)
# second = DNode(20)
# third = DNode(30)

# head.next = second
# second.prev = head

# second.next = third
# third.prev = second

# temp = head

# while temp:
#     print(temp.data)
#     temp = temp.next

# Question :Create a sample linked list with about 5 entries using class. Insert 
# a new entry before or after a given id. Delete an
# entry of a given id.
# Menu Items 
# 1. Insert Entry 
# 2. Delete Entry 
# 3. Display List 
# 4. Exit
# class StackNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# top = None

# while True:

#     print("\n1.Push")
#     print("2.Pop")
#     print("3.Display")
#     print("4.Exit")

#     ch = int(input("Enter Choice: "))

#     if ch == 1:

#         val = int(input("Enter Value: "))

#         newnode = StackNode(val)
#         newnode.next = top
#         top = newnode

#     elif ch == 2:

#         if top is None:
#             print("Stack Empty")

#         else:
#             print("Popped =", top.data)
#             top = top.next

#     elif ch == 3:

#         temp = top

#         while temp:
#             print(temp.data)
#             temp = temp.next

#     elif ch == 4:
#         break

# Question :Write a program to create a queue using linked list. Use add and
# remove. Add will insert the entry in top of the list. Remove will get
# bottom of the list and display. Display will show from top to bottom.
# Menu Items
# 1. Add
# 2. Remove
# 3. Display Stack
# 4. Exit


# class QueueNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# front = None
# rear = None

# while True:

#     print("\n1.Add")
#     print("2.Remove")
#     print("3.Display")
#     print("4.Exit")

#     ch = int(input("Enter Choice: "))

#     if ch == 1:

#         val = int(input("Enter Value: "))

#         newnode = QueueNode(val)

#         if front is None:
#             front = rear = newnode

#         else:
#             rear.next = newnode
#             rear = newnode

#     elif ch == 2:

#         if front is None:
#             print("Queue Empty")

#         else:
#             print("Removed =", front.data)
#             front = front.next

#     elif ch == 3:

#         temp = front

#         while temp:
#             print(temp.data)
#             temp = temp.next

#     elif ch == 4:
#         break
    
# def is_valid_number(num):
#     return num.isdigit()

# Question :Write a Calculator program that will give the "Calc" prompt and
# always stay on this prompt. When a user types one of the
# following commands, the program will calculate and give the
# result.
# Typing "Exit" will exit from the Calculator program. This program
# accepts up to 50-digit numbers. Then, the division will give the
# quotient and remainder.
# Note:
# Do not accept Invalid numbers.
# Do not print leading zeros.
# Use functions and write a professional program use Linux coding style.
# Each number can be of a different digit.
# Make sure that all the Input conditions are taken care.
# Try to minimize the execution speed.

# def calculate(expression):
#     if '+' in expression:
#         num1, num2 = expression.split('+')
#         if is_valid_number(num1) and is_valid_number(num2):
#             print(int(num1) + int(num2))
#         else:
#             print("Invalid Number")
#     elif '-' in expression:
#         num1, num2 = expression.split('-')
#         if is_valid_number(num1) and is_valid_number(num2):
#             print(int(num1) - int(num2))
#         else:
#             print("Invalid Number")
#     elif '*' in expression:
#         num1, num2 = expression.split('*')
#         if is_valid_number(num1) and is_valid_number(num2):
#             print(int(num1) * int(num2))
#         else:
#             print("Invalid Number")
#     elif '/' in expression:
#         num1, num2 = expression.split('/')
#         if is_valid_number(num1) and is_valid_number(num2):
#             dividend = int(num1)
#             divisor = int(num2)
#             if divisor == 0:
#                 print("Division by Zero Not Allowed")
#             else:
#                 quotient = dividend // divisor
#                 remainder = dividend % divisor
#                 print("Quotient :", quotient)
#                 print("Remainder:", remainder)

#         else:
#             print("Invalid Number")

#     else:
#         print("Invalid Expression")

# while True:
#     exp = input("Calc> ").strip()
#     if exp.lower() == "exit":
#         print("Calculator Closed")
#         break
#     calculate(exp)

# Common Prime Function

# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False

#     return True



# # Total Number of Two Digit Prime Numbers
# # Output: 21

# count = 0

# for i in range(10, 100):
#     if is_prime(i):
#         count += 1

# print("Two Digit Prime Count =", count)



# # Total Number of Three Digit Prime Numbers
# # Output: 143


# count = 0

# for i in range(100, 1000):
#     if is_prime(i):
#         count += 1

# print("Three Digit Prime Count =", count)



# # Sum of Single Digit Prime Numbers
# # Output: 17


# total = 0

# for i in range(2, 10):
#     if is_prime(i):
#         total += i

# print("Sum of Single Digit Primes =", total)



# # Sum of Two Digit Prime Numbers
# # Output: 1043


# total = 0

# for i in range(10, 100):
#     if is_prime(i):
#         total += i

# print("Sum of Two Digit Primes =", total)



# # Sum of Three Digit Prime Numbers
# # Output: 75067


# total = 0

# for i in range(100, 1000):
#     if is_prime(i):
#         total += i

# print("Sum of Three Digit Primes =", total)



# # Smallest Three Digit Prime Number
# # Output: 101

# for i in range(100, 1000):
#     if is_prime(i):
#         print("Smallest Three Digit Prime =", i)
#         break



# # Largest Three Digit Prime Number
# # Output: 997


# for i in range(999, 99, -1):
#     if is_prime(i):
#         print("Largest Three Digit Prime =", i)
#         break



# # Smallest Four Digit Prime Number
# # Output: 1009


# for i in range(1000, 10000):
#     if is_prime(i):
#         print("Smallest Four Digit Prime =", i)
#         break



# # Largest Four Digit Prime Number
# # Output: 9973


# for i in range(9999, 999, -1):
#     if is_prime(i):
#         print("Largest Four Digit Prime =", i)
#         break



# # Largest Eight Digit Prime Number
# # Output: 99999989


# for i in range(99999999, 9999999, -1):
#     if is_prime(i):
#         print("Largest Eight Digit Prime =", i)
#         break