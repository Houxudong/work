import os
os.chdir('F:/Code/pythoncode')
"""通过异常处理来解决错误"""
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':', 1)
            print(role,end=' ')
            print('said: ',end='')
            print(line_spoken,end='')
        except:
            print(each_line)
except:
    print('the data file is missing')