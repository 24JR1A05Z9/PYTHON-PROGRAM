word = input("Enter a word ")
a=['a','e','i','o','u','A','E','I','O','U'];
if any(vowel in word for vowel in "aeiou"):
    print("The word contains vowels.")
else:
    print("The word does not contain any vowels.")
