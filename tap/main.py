import json

file_data = open('sample.json')
data = json.load(file_data)
# print(data)

def synsets_gen(word):
    lines = data[word]
    output = []
    for line in lines: #[ ["minggu"], ["esa", "tunggal", "satu"] ]
        
        synsets = set([])
        
        for sense in line: # "minggu" / "esa", "tunggal", "satu"
            check_inner_senses = False
            if data.get(sense) != None:
                for inner_senses in data[sense]:
                    if word in inner_senses:
                        synsets.add(sense)
                        check_inner_senses = True
                
            # add word itself
            if check_inner_senses == True:
                synsets.add(word)
        output.append(sorted(synsets))
    return output


def main():
    for x in data:
        print synsets_gen(x)

main()

print(synsets_gen("ahad"))