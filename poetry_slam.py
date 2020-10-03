import random #to use with part #2, randomizer
from random import choice #to use for menu

#first declaration function
def get_file_lines(filename):
    poem_file = "/Users/jay/courses/cs1.0/poetry_slam/poem.txt" #calls the file for use inside the code
    infile = open(poem_file, 'r').readlines
    infile.close()
    return infile
#string of the filename
#return list of strings containing lines of the file

#-------Backwards Lines-------#
#print everything in order but backwards
def lines_printed_backwards(lines_list):
    lines_list = open("/Users/jay/courses/cs1.0/poetry_slam/poem.txt", "r").readlines() #calls poem.txt so the program can read it
    lines_list = lines_list[:: -1] #starts the poem from the end and reverses it
    num_lines = len(lines_list) #measures length of the lines so it knows how many lines to print
    for line in range(len(lines_list)):
        reverse = str(num_lines - line) + " " + lines_list[line] #format to print number of the line, then space, then string associated with the line number
        print(reverse) #print lines in reverse, include original line number

# #-------Random Lines---------#
#random lines, can repeat, just have same number of lines as original.
def lines_printed_random(lines_list):
    lines_list = open("/Users/jay/courses/cs1.0/poetry_slam/poem.txt", "r").readlines() #calls it here to read when printed
    for line in lines_list:
        line = random.randrange(len(lines_list)) #random generator
        rand_line = str(line) + " " + lines_list[line] #formatting to print the number of the line, a space, then the string
        print(rand_line) 

#-------Custom Lines---------#
#print() #some unique way, switch it so it prints only odds, then only evens. hope they make sense
def lines_printed_custom(lines_list):
    lines_list = open("/Users/jay/courses/cs1.0/poetry_slam/poem.txt", "r").readlines()
    #printing all odd lines in the poem
    print("Odd: \n")
    for line in range(len(lines_list)):
        if line % 2 == 0: #checking if line is even
            print(line + 1, lines_list[line]) #added 1 to print odd number with the odd line
    print() #spacing to separate odd and even a little more
    print("Even: \n")
    for line in range(len(lines_list)):
        if line % 2 == 1: #checking if line is odd
            print(line + 1, lines_list[line]) #added 1 to print even number along with the even line

#------Menu--------#
#ask user to select which poem to read
print("Welcome to 'Haunted Houses' -by Henry Wadsworth Longfellow.")
print("Prepare for a spooky poem for your spooky Halloween!")
choice = input("""Please pick one of these poem formats at your own risk:
                    1. Read Poem Backwards
                    2. Read Poem at Random
                    3. Read Odd Lines, Then Even Lines
                    Which would you like? """)

#print the choice they selected
if choice == "1":
    print()
    print(lines_printed_backwards('poem.txt'))

elif choice == "2":
    print()
    print(lines_printed_random('poem.txt'))

elif choice == "3":
    print()
    print(lines_printed_custom('poem.txt'))


#i'm really sad i didnt have time to figure out how to get rid of that pesky "None" that shows up. 