import os.path
import time
from colorama import Fore

f_open = open('quiz.txt')
f_write = open('quiz(1).txt', 'w')

full_text = f_open.read()
print(full_text)

find_word = input('Find what: ')
replace_word = input('Replace with: ')

if find_word in full_text:
    text = full_text.replace(find_word, Fore.BLUE + replace_word + Fore.RESET)
    text.strip()
    print(text)
    f_write.write(text)
else:
    print("Can't find the text", find_word)

print('File created: quiz(1).txt')
print('Last modified: %s' %time.ctime(os.path.getmtime('quiz(1).txt')))
