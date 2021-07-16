# author: Lyric Marner
# date: July 13, 2021

# --------------- Section 1 --------------- #

# 1 | String Methods
#
# 1 - Save your name to a variable named name.
#   a. Center that variable within 30 characters. Print it.
#   b. Print the variable in all upper case.
#   c. Print the variable in all lower case.
#   d. Print the variable capitalized (Look to documentation.)
name = 'Lyric Marner'
print(name. center(30, '-'))
print(name.upper())
print(name.lower())
print(name.capitalize())
print()
# 2 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first instance of the letter a. Print that position.
#   b. Find the first instance of the letter b. Print that position.
#   c. Find the first instance of a word of your choice. Print that position.
text = input('Please enter a sentence: ')
print('Position of the letter a: ', text.find('a'))
print('Position of the letter b: ', text.find('b'))
print('Position of the word lovely: ', text.find('lovely'))
print()
# 3 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first appearence of every vowel in the text.
#   b. Using a built-in function, print the position of the vowel that shows up last.
#   c. Using a built-in function, print the position of the vowel that shows up first.
text = input('Please enter a sentence: ')
text = text.lower()
a_position = text.find('a')
e_position = text.find('e')
i_position = text.find('i')
o_position = text.find('o')
u_position = text.find('u')

print('Position of the vowel a: ', a_position)
print('Position of the vowel e: ', e_position)
print('Position of the vowel i: ', i_position)
print('Position of the vowel o: ', o_position)
print('Position of the vowel u: ', u_position)
print()

# 4 | String Indexing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the 0th letter of the text using string indexing.
#   b. Print the 1st, 2nd, and 3rd letters of the text using string indexing.
#   c. Print the last letter of the text using string indexing.
#       HINT: There are multiple ways of doing this. Is there a function that we can use that will find
#           the position of the last letter, or atleast one off from it?

text = input('Enter a sentence: ')
print('The 0th letter in the text is', text[0])
print('The first letter of the text is:', text[1])
print('The second letter of the text is:', text[2])
print('The third letter of the text is:', text[3])
#print(text[1], text[2], text[3])
length = len(text)
print('The last letter of the text is:', text[length - 1])
print()

# 5 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Slice text from the 2nd position to the 5th. Print that.
#   b. Slice text from the 0th position to the 8th. Print that.
#   c. Slice text from 3rd position to end. Print that.
#   d. Slice text from the beginning to 5 positions before the last character. Print that.
#       HINT: Use a function to get the last position of the string.
text = input('Please enter a sentence: ')
print(text[2:5])
print(text[0:8])
print(text[3:])
last_char = len(text)
print(text[0:last_char - 5])
print()

# 6 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the text, but only every 2nd character.
#   b. Print the text, but only every 3rd character.
#   c. Print the text, but in reverse order.
text = input('Enter a sentence: ')
print(text[::2])
print(text[::3])
print(text[::-1])