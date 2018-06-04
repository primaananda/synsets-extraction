import json
import pandas

file = open('datatest/1.json')
thesa = json.load(file)

def synsets_extraction(word):
    list_set = []
    for val in thesa[word]:
        word_set = set(val)
        word_set.add(word)
        list_set.append(word_set)
    dt = list_set
    list_dataframe = []

    for ls in dt:
        df = pandas.DataFrame(index=ls, columns=ls)
        list_dataframe.append(df)

    for line in word:
        for sense in line:
            print (sense)
        # if thesaurus.get(sense) != None:
        #     for inner_senses in thesaurus[sense]:
        #
        #         # TODO: NOT COVERING ALL CASES
        #         if len(synsets) == 0:
        #             if word in inner_senses:
        #                 synsets.add(sense)
        #                 check_inner_senses = True
        #         else:
        #             if synsets <= set(inner_senses):
        #                 synsets.add(sense)
    #return list_dataframe

synsets_extraction("ahad")