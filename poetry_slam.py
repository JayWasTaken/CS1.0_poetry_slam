def foo(jj)
    num_lines = len(jj)
    jj = jj[::-1] # reverses the list
    # 1 -> num_lines
    for i in range(len(jj)):
        #print(num_lines - 1)
        print(jj[i])
        variable = str(num_lines - i) + " " + jj[i]
        print(variable)

f = open('./poem.txt', 'r') # open a file

#foo([1, 2, 3, 4])
foo(f.read().splitlines()) #pass the list of lines to foo