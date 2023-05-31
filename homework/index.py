#question 1
#Accept two user ages as inputs and give us the difference between them. (The Answer should always be a positive output)

age1 = int(input("Enter the first age: "))
age2 = int(input("Enter the second age: "))
age_difference = abs(age1 - age2)
print("The age difference is:", age_difference)

#Question 2
#Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
print("The", adjective, noun, verb, "over the lazy dog.")

#Question 3
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors.

age = int(input("Enter your age: "))
if age < 18:
    print("You are a kid.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")

#Question 4
#Take in a number from a user input, output the number squared.

number = float(input("Enter a number: "))
squared_number = number ** 2
print("The square of", number, "is", squared_number)

#Question 5
#Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False
word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

print(len(word1) > 5)
print(len(word2) > 5)
print(len(word3) > 5)
print(len(word4) > 5)
print(len(word5) > 5)











