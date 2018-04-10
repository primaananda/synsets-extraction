#created by primaananda
file = open('hasil/final/tesaurus_hasil_convert_from_pdf.txt','r')
files = open('hasil/final/tesaurus_clear_text.txt','w')

lines = file.readline()

dicts = []
dicts2 = []

while lines:
    if(not lines.startswith('\t')):
        dicts.append(lines.rstrip())
    lines = file.readline()
    if not lines:
        break

letter = '###'
for x in range(0,len(dicts)):
    temp = ''
    if(dicts[x].startswith('#')):
        letter = dicts[x][1].lower()
    if(dicts[x].startswith(letter)):
        temp += dicts[x]
        while(dicts[x].endswith(',')) or (dicts[x].endswith('-')):
            temp += dicts[x+1]
            x =  x+1
        dicts2.append(temp)

for x in dicts2:
    files.write(x+'\n')
    
file.close()
files.close()