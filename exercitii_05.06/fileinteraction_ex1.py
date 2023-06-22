"""
Create a text file called “hello.txt” and add the following text inside of it:

"""

with open('hello.txt') as f:
    lines = f.read()
    print(lines)