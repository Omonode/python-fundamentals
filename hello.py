# for items in range (1,100):
#     items = items + 4
#     # print(items)
#
# count= 0
# while count <=8:
#     # print (count)
#     count += 1
#
# number = 0
# total = 1
#
# while number < 100:
#     # print (total)
#     number = number + total
#
# total = 0
# number = 1
#
# while number <= 100:
#     total += number
#     number +=1
#     # print (total)

# age = int(input("How old are you "))
# while age <= 0:
#     print ("Kindly input a valid Age")
#     age = int(input("Enter your Age again "))
# # print (age)

# price accumulator
# total = 0
# price = int(input("type a digit. Type 0 to end the process and get your total"))
# while price != 0:
#     total += price
#     price = int(input(""))
# print (total)


# while True:
#     answer = str(input("Select yes to continue"))
#     if answer == "yes":
#         break
#     print("You choice is not looking like a yes)")
# print("Continuing")

# word = "Python"
# for char in word:
#     print (char, end="-")
# print() #The final print() with nothing inside ends that line.

# vowels = "aeiouAEIOU"
# sentence = "Programming is fun"
# count = 0
# for char in sentence:
#     if char in vowels:
#         count = count +1
#     # print (count)
# print(f"Vowels: {count}")

# for i in range(5):
#     pass
# print(i)

# for _ in range(3): #_ means i dont need the value
#     print ("Hello Drake")

# for i in range (5,0,-1):
#     print (i, end="-")

# number = 5
# for items in range(2):
#     print(f"your number is {items} x {number}. The total is {items * number}")

# for n in range (8, 69):
#     if n % 8 == 0:
#         print(f"i found {n}")
#         break
# print(f" there no numbers that fit {n}")

# for i in range(12, 87):
#     if i % 2 == 0:
#         continue
#     print(i, end="-") #continue is mostly used to get your choice of data by testing for the opposite

# points = 0
# for score in range(12, 156):
#     if score % 7 != 0:
#         continue
#     if score % 2 != 0:
#         continue
#     points += 1
#     print(score, end="-")
# print()

# found = 0
# n = 1
# while n <= 1000:
#     if n % 3 != 0 or n % 5 != 0:   # not divisible by BOTH 3 and 5
#         n += 1
#         continue
#     print(n)                        # 15, 30, 45
#     found += 1
#     n += 1
#     if found == 3:
#         break

# found = 0
# n = 1
# while n <= 1000:
#     if n % 3 != 0 or n % 5 != 0:
#         n += 1
#         continue
#     print(n)
#     found += 7
#     n+=1
#     if found % 9 == 0:
#         break

# number = 9
# for item in range(1, number):
#     if number % item == 0:
#         print(f"The number is not prime {number}") # number is 9, so this is range(2, 9). So 9 is never checked
#         break
#     else:
#         print(f"The number is a prime {number}")

# for row in range (1,13):
#     for column in range (1,13):
#         print(f"{row * column:4d}", end="")
#     print()


# for row in range (1,14):
#     for column in range (1,14):
#         print (f"{row * column:5d}", end="")
# #     print()
# n = int(input("Enter a number"))
# if n < 1 or n > 20:
#     print("Please enter a number between 1 and 20")
# for row in range (1, n+1):
#     for number in range(n, row-1, -1):
#         print(number, end="")
#     print()

# n = int(input("Enter a number: "))
# if n < 1 or n > 20:
#     print("kindly enter a number between 1 to 20")
# for row in range (1, n +1):
#     for number in range (9, row-1, -1):
#         print(number, end="")
#     print()
#
# found = 0
# for number in range (1, n*2+1):
#     if number % 9 == 0:
#         continue
#     print(number, end="")
#     found += 1
#     if found % 6 == 0:
#         break
# print()

n = 10
#
# for row in range (1, n +1):
#     for number in range (n, row-1, -1):
#         print(number, end="")
#     print()

# while n < 10:
#     if n in range (n, row-1, -1) == True:
#         print(n)
#          break
# found = 0
# for n in range (2, 20 +1):
#     if n % 2 != 0:
#         continue
#     print(n, end="-")
#
# found = 0
# for n in range (2, 20, 2):
#     if n % 2 != 0:
#         continue
#     print(n, end="-")
#while in steps of 2
# n =0
# while n < 20:
#     print(n, end=" ")
#     n += 2

# for letter in "LAGOS":
#     if letter == "G":
#         break
#     print(letter, end="")

# x = 10
# while x > 10:
#     x = x//2
# print(x)


# Exercise 4: Score averager. Ask how many students there are. Then ask
# for each student('s score in a loop: Score for student 1:,
# Score for student 2:, and so on. Print the total, the average
# (2 decimal places), and
# how many scored 50 or above.)

# student_count = int(input("Enter the total number of students: "))
# student_Id = int(x)
# student_sum_score = int()
# while student_Id != 0:
#     student_Id = int(input("what is your student number: "))
#     student_score = int(input("what is your score: "))
#     student_sum_score += student_score
#     print(f"student {student_Id} scored:  {student_score}")
# print(f"sum total of student score is: {student_sum_score}")
# Average_score = student_sum_score/student_count
# print(f"Average score is: {Average_score}")

# Total_students = int(input("Enter the number of students:"))
# Total_student_score = int()
# student_id = int()
#
# for students in range (1,3):
#     if student_id < 1 or student_id > 3:
#         print("kindly enter a valid number: ")
#     student_id =int(input("Enter your student id: "))
#     student_score = int(input("Enter your score: "))
#     Total_student_score += student_score
# print(Total_student_score)

# Total_score = int()
# score = int(1)
# while score != 0:
#     score = int(input("Enter a price: "))
#     print("Enter zero (0) when you are done shopping")
#     Total_score += score
#     continue
# print(f"your total shopping cost is {Total_score}")

# count = 0
# password = "python123"
# n = input("Enter a password: ")
# if n == password:
#     print("Password match")
# else:
#     while n != password:
#         n = input("Try again: ")
#         count +=1
#         if count % 4 == 0:
#             break
#     print("you have failed to enter a correct password")

# Exercise 7: FizzBuzz (a classic job-interview question). Print 1 to 30, but:
#
# for multiples of 3, print Fizz
# for multiples of 5, print Buzz
# for multiples of both, print FizzBuzz

# for items in range (1,31):
#     if items % 3 == 0:
#         print ("fizz")
#     elif items % 5 == 0:
#         print ("Buzz")
#     elif items % 3 == 0 and items % 5 == 0:
#         print ("FizzBuzz")

# number = input("Enter a number: ")
# x = 0
# found = 0
# for n in range(2,50+1):
#     if n % 2 == 0:
#         x +=1
#         continue
#     print(n, end="-")

# (a) N = 4            (b) N = 4
# *                    1
# * *                  1 2
# * * *                1 2 3
# * * * *              1 2 3 4

# for row in range (1,9+1):
#     for column in range (row-1, -1, -1):
#         print(column, end=" ")
#     print()
# star = int(*)
# for row in range (1,9+1):
#     for * in range (row-1, -1, -1):
#         print("*", end=" ")
#     print()

# city = "Lagos"
# # print(city[:3])
# # print(city[1:3])
# # print(city[3:])
# # print(city[1:3:1])
# # print(city[:])
# #
# # print(city[-1])    # s  (last, counting from the end)
# # print(city[-5])
# print(city[4:1:-2])

# for ch in "Lagos":
#     print(ch, end="")

# word = "Lagos"
# for i in range(len(word)):
#     print(i, word[i])
# result below
# i	word[i]
# 0	L
# 1	a
# 2	g
# 3	o
# 4	s

# words = "Programming is fun"
# vowels = "aeiouAEIOU"
# count = 0
#
# for ch in "Programming is fun":
#     if ch in vowels:
#         count +=1
#         # print(ch, end="")
# print(count)

# for ch in "GhOst":
#     if ch.upper() in "GhOst":
#         print(ch.upper(), end="")

# reversed_word= ""
# for ch in "Lagos":
#     reversed_word = ch + reversed_word
# print(reversed_word, end="")

# x = "hello"
# x.upper()
# print (x)
#
# c = "hello"
# print(x.upper())

# Company =  "Toyota yaris"
# print(Company.strip())
# print(Company.lstrip())
# print(Company.rstrip())

# print("2026-11-24".split("-"))         # ['2026', '11', '24']
# print("Amara,22,Ghana".split(","))     # ['Amara', '22', 'Ghana']
# print("The quick brown fox".split())   # ['The', 'quick', 'brown', 'fox']
# print("My brother my friend will this be the end".split())
# print("My brother my friend will this be the end".split())
#
# word = ["Drake Omonode"]
# print (" ".join(word))

# 7.3 Split, change, join: the classic pattern

# email = "amara.mensah@gmail.com"
# print(email.split("@"))      # ['amara.mensah', 'gmail.com']
#
# at = email.find("@")
# print(email[:at])            # amara.mensah  (everything before @)
# print(email[at + 1:])        # gmail.com     (everything after @)

# Part 8: f-strings in depth
#
# Put f before the quotes, and anything inside {} is worked out first:
#
# python
# price, qty = 1234.5, 3
# print(f"Total: {price * qty:,.2f}")     # Total: 3,703.50
# print(f"{'amara'.title()}")             # Amara
# 8.1 Format specifiers (after a colon)
# Code	Result	Meaning
# f"{3703.5:,.2f}"	3,703.50	thousands comma, 2 decimals
# f"{'Hi':<6}|"	Hi |	left-aligned in a width of 6
# f"{'Hi':>6}|"	Hi|	right-aligned
# f"{'Hi':^6}|"	Hi |	centred
# f"{'Hi':*^8}"	***Hi***	centred, padded with *
# f"{7:03d}"	007	whole number padded with zeros to 3
# f"{0.4567:.1%}"	45.7%	as a percentage
#
# How to read :*^8: fill with *, centre (^), total width 8.
#
# 8.2 The one-line if inside an f-string
# python
# is_member = True
# print(f"Status: {'Member' if is_member else 'Guest'}")
#
# Use single quotes inside the {} when the f-string itself uses double quotes.

# Part 9: Putting it together
#
# Initials:
#
# python
# full = "amara ama mensah"
# initials = ""
# for w in full.split():
#     initials += w[0].upper() + "."
# print(initials)                 # A.A.M.
#
# w[0] is the first letter of each word: indexing inside a loop over split().
#
# Palindrome check, ignoring spaces and capitals:
#
# python
# phrase = "Never odd or even"
# cleaned = phrase.replace(" ", "").lower()    # neveroddoreven
# print(cleaned == cleaned[::-1])              # True
#
# Masking a phone number:
#
# python
# phone = "08031234567"
# masked = phone[:4] + "*" * (len(phone) - 6) + phone[-2:]
# print(masked)                   # 0803*****67
#
# The first 4, then stars for the middle (11 − 6 = 5 of them), then the last 2. "*" * 5 repeats text, from Day 1.
#
# Word frequency (bridging to Day 9):
#
# python
# counts = {}
# for w in "the cat sat on the mat".split():
#     counts[w] = counts.get(w, 0) + 1
# print(counts)     # {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
# Part 10: Useful extras (not in the course, but common)
#
# Checking what text contains:
#
# Method	"12"	"12.5"	"abc"
# .isdigit() (all digits?)	True	False (the dot isn't a digit)	False
# .isalpha() (all letters?)	False	False	True
# .isalnum() (letters or digits?)	True	False	True
#
# Comparing text works letter by letter, by character code:
#
# "abc" < "abd" is True (c comes before d).
# "Zebra" < "apple" is True ⚠️ (all capitals come before all small letters).
# "10" < "9" is True ⚠️ (it compares "1" with "9", not the numbers 10 and 9).
#
# So convert to numbers before comparing amounts.
#
# Common mistakes
# Mistake	What happens	Fix
# name.upper() without =	Nothing changes	name = name.upper()
# text[len(text)]	IndexError	text[-1]
# Expecting the stop to be included	One character short	[0:3] gives 3 characters (0, 1, 2)
# text[0] = "X"	TypeError (immutable)	Build a new string
# .replace() with different capitals	No match	Lowercase first
# split(" ") for words	Empty items appear	split()
# join() with numbers in the list	TypeError	str() each item first
# Comparing "10" < "9"	Compares as text	Convert with int() first
# Summary
#
# ✅ A string is a sequence of characters; spaces count; len() counts them.
# ✅ Indexing: [0] first, [-1] last; going past the end gives IndexError.
# ✅ Slicing: [start:stop:step], stop never included (fence posts); never crashes.
# ✅ Loop through characters with for ch in text, or positions with range(len(text)).
# ✅ Strings are immutable: methods return new strings, so save the result with =.
# ✅ Methods: case, cleaning, searching, replacing; chains run left to right.
# ✅ split() turns text into a list; "glue".join(list) turns a list into text.
# ✅ f-strings: {value:.2f}, {text:<10}, {n:03d}, and 'A' if x else 'B'.

# Exercises
#
# Write each as its own .py file. Predict the output in a comment before running. Use only Days 1 to 7.
#
# Level 1: Warm-up
#
# 1. Predict, then check:
#
# python
# w = "Abuja"
# print(w[1], w[-2], w[1:4], w[::-1], w[5:])
#
# 2. Clean a name. Ask for a full name. Print it with the spaces removed from both ends and in title case, its length without spaces, and its initials (e.g. "A.M.").
#
# 3. Email parts. Ask for an email address. Print the username (before the @), the domain (after the @), and whether it ends with ".com" (True or False).
#
# Level 2: Core
#
# 4. Character counter. For one sentence, count the vowels, consonants and spaces using a single loop and three counters.
#
# Hint: check vowels first, then ch.isalpha() for consonants, then ch == " ".
#
# 5. Reverse each word. "I love Python" becomes "I evol nohtyP". Keep the word order; reverse each word's letters.
#
# Hint: split(), reverse each with [::-1], append to a list, then " ".join().
#
# 6. Mask a card number. "1234567812345678" becomes "************5678". Only the last 4 digits show.
#
# Hint: "*" * (len(card) - 4) plus card[-4:].
#
# 7. Palindrome without [::-1]. Check whether a word is a palindrome by comparing letters from both ends in a loop.
#
# Hint: compare word[i] with word[-1 - i] for i in range(len(word) // 2). If any pair differs, it's not a palindrome. Try break with a loop else.
#
# Level 3: Challenge
#
# 8. Name formatter. Turn "amara,kofi,ama,yaw" into "Amara | Kofi | Ama | Yaw".
#
# 9. Longest word. Find the longest word in a sentence and print it with its length. Use the "best so far" pattern from Day 6.
#
# 10. Receipt printer. For 3 items with names, quantities and prices, print a receipt using f-strings:
#
# names left-aligned in 15;
# quantities centred in 5;
# prices right-aligned in 10, with 2 decimals;
# a border, and a total line lined up under the prices.
#
# How to get the most from these:
#
# Draw the fence posts for any slice you're unsure about.
# Write a trace table for every loop that builds a string.
# Try strange inputs: an empty string, extra spaces, all capitals, one letter.
#
# Send me your solutions, one at a time or all together, and I'll run them and show you exactly where anything goes wrong.

# names = ["Drake", "Tunde,", "Monic"]
# slot = (list(enumerate(names,start=1)))
# print (slot)
