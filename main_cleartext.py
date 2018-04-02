#created by primaananda
file = open('hasil/finaltesaurus.txt','r')

lines = file.readline()
while lines:
    print lines
    lines = file.readline()
file.close()