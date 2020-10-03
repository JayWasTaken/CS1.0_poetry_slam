import random

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
    for line in range(len(lines_list)):
        reverse = str(num_lines - line) + " " + lines_list[line]
        print(reverse) #print lines in reverse, include original line number
#-------Random Lines---------#
    
        #random lines, can repeat, just have same number of lines as original. 

#-------Custom Lines---------#
# def lines_printed_custom(lines_list):
#     lines_list = "/Users/jay/courses/cs1.0/poetry_slam/poem.txt"

#     print() #some unique way, switch it so instead of 1234 its 2143? somethin
print(lines_printed_backwards('poem.txt'))





# def foo(jj)
#     num_lines = len(jj)
#     jj = jj[::-1] # reverses the list
#     # 1 -> num_lines
#     for i in range(len(jj)):
#         #print(num_lines - 1)
#         print(jj[i])
#         variable = str(num_lines - i) + " " + jj[i]
#         print(variable)

# f = open('./poem.txt', 'r') # open a file

# #foo([1, 2, 3, 4])
# foo(f.read().splitlines()) #pass the list of lines to foo