"""
Introduction
Pig Latin is a language where words are made by modifying 
English words. The rules are as follows:

If the letter starts with a consonant:
Step 1: Remove the first letter of the word.

Step 2: Add a “-” to the end of the word.

Step 3: Add the letter you removed in step 1 to the end of 
the word.

Step 4: Add ”ay” to the end of the word. 
If the letter starts with a vowel:
Just add “-yay“ to the end of the word.

Task
Write a program that translates a word into Pig Latin.

Input format
A single English word. The word will only consist of 
uppercase and lowercase letters.
Output format
The same word in Pig Latin. 
"""
message = input("Enter your message: ").split()
vowels = "aeiouAEIOU"
pig_latin_list = []

for word in message:
    if word[0] not in vowels:
        pig_latin = word[1:] + "-" + word[0] + "ay"
    else:
        pig_latin = word + "-yay"
    pig_latin_list.append(pig_latin)

print(" ".join(pig_latin_list))
