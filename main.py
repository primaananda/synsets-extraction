import json
from synsets_extraction import synsets_extraction

#open file
files = open('datatest/1.json')

#input = del_redundant('perdamaian', file)
synsets = synsets_extraction(files)
print()
print()
for x in synsets:
    print(x)