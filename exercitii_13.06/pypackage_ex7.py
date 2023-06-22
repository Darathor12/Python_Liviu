# 4.Write a program that generates 26 text files, called A.txt, B.txt, … Z.txt.
# Each file will contain the sentences below:
# My name is letter X.
# I am the 24th letter of the alphabet.
# Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
alphabet = []
start = ord('A')
#print(start)
for i in range(26):
    alphabet.append(chr(start + i))
print(alphabet)
for letter in alphabet:
    with open(f'FILES/{letter}.txt', 'w') as new_file:
        new_file.writelines(f'My name is letter {letter}. \n')
        if letter == 'A':
            var = 'st'
            #new_file.writelines('I am the 1st letter of the alphabet. \n')
        elif letter == 'B':
            #new_file.writelines('I am the 2nd letter of the alphabet. \n')
            var = 'nd'
        elif letter == 'C':
            #new_file.writelines('I am the 3rd letter of the alphabet. \n')
            var = 'rd'
        else:
            #new_file.writelines(f'I am the {ord(letter)-ord("A")+1}th letter of the alphabet. \n')
            var = 'th'
        new_file.write(f'I am the {ord(letter)-ord("A")+1}{var} letter of the alphabet.')


for letter in alphabet:
    with open(f'FILES/{letter}.txt') as my_file:
        for line in my_file:
            print(line)