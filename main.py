#Love_Calculator
#Created with Python
#Made with 💖 by Cephas Cardozo

print('''              
88                                     
88                                     
88                                     
88  ,adPPYba,  8b       d8  ,adPPYba,  
88 a8"     "8a `8b     d8' a8P_____88  
88 8b       d8  `8b   d8'  8PP"""""""  
88 "8a,   ,a8"   `8b,d8'   "8b,   ,aa  
88  `"YbbdP"'      "8"      `"Ybbd8"' 
''')

print("Welcome to the Love Calculator!\n")
print("💖💖💖💖💖💖💖💖💖💖💖💖💖\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love is {love_score}, you go together like coke and mentos.\n")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.\n")  
else:
    print(f"Your score is {love_score}\n")


