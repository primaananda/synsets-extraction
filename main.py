import json
from alt_gen import alt_gen

#open file
files = open('datatest/1.json')

# count synset
count_synset = 0
count_synset_after = 0
# end count synset

#delete redundant synsets
def del_redundant(synsets):
    print('Menghapus data redundant')
    new_synset = []
    count = 0
    for synset in synsets:
        #print(len(synset))
        #remove zero synset in list
        if len(synset) != 0:
            new_synset.append(synset)

    #remove duplicate synsets
    new_set = set(tuple(syns) for syns in new_synset)
    new_synset = [list(syns) for syns in new_set]

    #sum synset after delete redundant and zero list
    for x in new_synset:
        count += 1
    count_synset_after = count
    print('done\nTerdapat : ' + str(count_synset_after) + ' synsets setelah menghapus data duplikat')
    return new_synset

#ekstraksi synset
def synsets_extraction(file):
    print('Proses ekstraksi synset')
    thesa = json.load(file)
    calon_synsets = []
    count = 0
    for word in thesa:
        output = alt_gen(word, open('datatest/1.json'))
        for synsets in output:
            calon_synsets.append(synsets)
            count += 1
    file.close()
    count_synset = count
    print('done\n'+'Terdapat : ' + str(count_synset) + ' synsets yang berhasil di ekstrak')
    return calon_synsets

#input = alt_gen('perdamaian', file)
dat1 = synsets_extraction(files)
dat2 = del_redundant(dat1)
for x in dat2:
    print(x)