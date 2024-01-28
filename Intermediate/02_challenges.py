### CHALLENGES ###

"""
THE "FIZZ BUZZ":
Write a program that shows through the console (with a print) the
numbers from 1 to 100 (both included and with a line break between
each print), replacing the following:
- Multiples of 3 for the word "fizz".
- Multiples of 5 for the word "buzz".
- Multiples of 3 and 5 at the same time for the word "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else: 
            print(index)

fizzbuzz()


"""
IS IT AN ANAGRAM?
Write a function that takes two words (String) and returns
true or false (Bool) depending on whether or not they are anagrams.
- An Anagram consists of forming a word by rearranging ALL of them
   the letters of another initial word.
- It is NOT necessary to check that both words exist.
- Two exactly the same words are not an anagram.
"""

def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower())


is_anagram("Amor", "Roma")


"""
THE FIBONACCI SEQUENCE
Write a program that prints the first 50 numbers of the Fibonacci sequence
starting at 0.
- The Fibonacci sequence is made up of a succession of numbers in
   which the next one is always the sum of the two previous ones.
   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():

    prev=0
    next=1

    for i in range(0,50):
        print(prev)
        fib = prev + next 
        prev = next
        next = fib

fibonacci()


"""
IS IT A PRIME NUMBER?
Write a program that is responsible for checking whether a number is prime or not.
Once this is done, print the prime numbers between 1 and 100.
"""

def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

is_prime()


"""
INVESTING CHAINS
Create a program that reverses the order of a text string
without using language functions that do it automatically.
- If we pass it "Hola mundo" it would return "odnum aloH"
"""

def reverse(text):
    reversed_text = ""
    text_length = len(text)

    for index in range(0, text_length):
        reversed_text += text[text_length - index - 1]
    return reversed_text

print(reverse("Hello world"))


