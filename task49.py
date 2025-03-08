import re
txt = 'We are happy to see you'
pattern = '[a-zA-Z0-9]'
x = re.search(pattern, txt)

if x:
    print('no, it allows certain characters')
else:
    print('yes, string allow characters(a-z, A-Z, 0-9)')