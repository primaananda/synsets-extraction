import json

def synsets_gen(word, thesa):
    thesaurus = json.load(thesa)
    lines = thesaurus[word]
    output = []
    for line in lines: #[ ["minggu"], ["esa", "tunggal", "satu"] ]
        
        synsets = set([])
        
        for sense in line: # "minggu" / "esa", "tunggal", "satu"
            check_inner_senses = False
            if thesaurus.get(sense) != None:
                for inner_senses in thesaurus[sense]:
                    if word in inner_senses:
                        synsets.add(sense)
                        check_inner_senses = True
                
            # add word itself
            if check_inner_senses == True:
                synsets.add(word)
        output.append(sorted(synsets))
    return output
