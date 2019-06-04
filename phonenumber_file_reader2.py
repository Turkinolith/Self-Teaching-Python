import re
phoneNumRegex = re.compile(r'\d-\d\d\d-\d\d\d-\d\d\d\d')

with open('text_text.txt') as file:
    choppeddocument = file.read().split()
    joineddoc = ' '.join(choppeddocument)
mo = phoneNumRegex.findall(joineddoc)
for i in range(len(mo)):
    print('Phone Numbers Found: ' + mo[i])
