import json
from alt_gen import alt_gen

#open file
files = open('datatest/1.json')

def del_redundant(synsets):
    new_synset = []
    for synset in synsets:
        #print(len(synset))
        #remove zero synset in list
        if len(synset) != 0:
            new_synset.append(synset)
        #end remove zero synset
    #remove duplicate synsets
    new_set = set(tuple(syns) for syns in new_synset)
    new_synset = [ list(syns) for syns in new_set]
    #end remove duplicate synsets
    print(new_synset)
    return new_synset

def synsets_extraction(file):
    thesa = json.load(file)
    calon_synsets = []
    for word in thesa:
        output = alt_gen(word, open('datatest/1.json'))
        for synsets in output:
            calon_synsets.append(synsets)
    file.close()
    return calon_synsets

#input = alt_gen('perdamaian', file)
dat = synsets_extraction(files)
del_redundant(dat)