import os
os.chdir('F:/Code/pythoncode')
"""通过增加额外的逻辑来解决问题"""
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end=' ')
            print('said:',end=' ')
            print(line_spoken)
        else:
            print(each_line)

else:
    print('the data file is missing')