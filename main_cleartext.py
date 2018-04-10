#created by primaananda
import re
file = open('hasil/final/finaltesaurus.txt','r')
files = open('hasil/final/tesaurus.txt','w')
lines = file.readline()

dicts = []
dicts2 = []


while lines:
    if(not lines.startswith('\t')):
        #sentences = lines.replace('\n','')
        dicts.append(lines)
        lines = file.readline()
    if not lines:
        break
'''
for x in range(0,len(dicts)):
    test = ''
    print(dicts[x])
    if (dicts[x].startswith('#')) or (dicts[x].endswith(',\n')) or (dicts[x].endswith('-\n')):
        temp = ''
        while dicts[x].endswith(',\n') or dicts[x].endswith('-\n') :
            temp += dicts[x]
            x = x+1
        dicts2.append(temp)
        
for x in dicts2:
    files.write(x)
'''

for ln in dicts:
    file.write(ln):

file.close()
files.close()