s = "))"

stack = list()

for par in s:
    if par == '(' or par == '[' or par == '{':
        stack.append(par)
    elif par == ')' and len(stack) > 0:
        if stack.pop() != '(':
            print(False)
    elif par == ']' and len(stack) > 0:
        if stack.pop() != '[':
            print(False)
    elif par == '}' and len(stack) > 0:
        if stack.pop() != '{':
            print(False)
#                ,        ,
#               /(        )`
#               \ \___   / |
#               /- _  `-/  '
#              (/\/ \ \   /\
#              / /   | `    \
#              O O   ) /    |
#              `-^--'`<     '
#             (_.)  _  )   /
#              `.___/`    /
#                `-----' /
#   <----.     __ / __   \
#   <----|====O)))==) \) /====
#   <----'    `--' `.__,' \
#                |        |
#                 \       /       /\
#            ______( (_  / \______/
#          ,'  ,-----'   |
#          `--{__________)
if len(stack) == 0:
    print(False)
else:
    print(True)
