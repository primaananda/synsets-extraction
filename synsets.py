import json

def synsets_gen(word, thesa):
    thesaurus = json.load(thesa)
    lines = thesaurus[word]
    output = []
    for line in lines:
        
        synsets = set([])
        
        for sense in line:
            check_inner_senses = False
            if thesaurus.get(sense) != None:
                for inner_senses in thesaurus[sense]:

                    print sense, synsets, inner_senses, synsets <= set(inner_senses)
                    # TODO: NOT COVERING ALL CASES
                    if len(synsets) == 0:
                        if word in inner_senses:
                            print 'added "{}" by init'.format(sense)
                            synsets.add(sense)
                            check_inner_senses = True
                    else:
                        if synsets <= set(inner_senses):
                            print 'added "{}"'.format(sense)
                            synsets.add(sense)
                    print
            # add word itself
            if check_inner_senses == True:
                synsets.add(word)

        output.append(sorted(synsets))
    return output
