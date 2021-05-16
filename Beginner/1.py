#User Input
a=input("Enter a letter: ")

#List of vowels
vowels=['a','e','i','o','u']

#convert the input into lowercase if it is in uppercase
b=a.lower()

#condition to check the given input is vowel or consonant
if(b in vowels):
    print(str(a)+' is a vowel.')
else:
    print(str(a)+' is a consonant')
