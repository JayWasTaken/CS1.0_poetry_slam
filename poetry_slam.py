import random
from random import choice 

def get_file_lines(filename):
    poem_file = "/Users/jay/courses/cs1.0/poetry_slam/poem.txt"
    infile = open(poem_file, 'r').readlines
    infile.close()
    return infile
#string of the filename
#return list of strings containing lines of the file

#-------Backwards Lines-------#
def lines_printed_backwards(lines_list):
    lines_list = open("/Users/jay/courses/cs1.0/poetry_slam/poem.txt", "r").readlines()
    lines_list = lines_list[:: -1]
    num_lines = len(lines_list)
    print()
    for line in range(len(lines_list)):
        reverse = str(num_lines - line) + " " + lines_list[line]
        print(reverse) #print lines in reverse, include original line number

# #-------Random Lines---------#
def lines_printed_random(lines_list):
    lines_list = open("/Users/jay/courses/cs1.0/poetry_slam/poem.txt", "r").readlines()
    for line in lines_list:
        line = random.randrange(len(lines_list))
        rand_line = str(line) + " " + lines_list[line]
        print(rand_line)
    
        #random lines, can repeat, just have same number of lines as original. 

#-------Custom Lines---------#
#     print() #some unique way, switch it so instead of 1234 its 2143? somethin, or evens and then odds?
def lines_printed_custom(lines_list):
    lines_list = open("/Users/jay/courses/cs1.0/poetry_slam/poem.txt", "r").readlines()
    # lines_list_odd
    print("Odd: \n")
    for line in range(len(lines_list)):
        if line % 2 == 0: #checking if line is even
            print(line + 1, lines_list[line]) #added 1 to print odd number with the odd line
    print()
    print("Even: \n")
    for line in range(len(lines_list)):
        if line % 2 == 1:
            print(line + 1, lines_list[line])

choice = input("""Please enter from options below:
                    1. Read Poem Backwards
                    2. Read Poem at Random
                    3. Read Odd Lines, Then Even Lines
                    Which would you like? """)

if choice == "1":
    print(lines_printed_backwards('poem.txt'))

elif choice == "2":
    print(lines_printed_random('poem.txt'))

elif choice == "3":
    print(lines_printed_custom('poem.txt'))