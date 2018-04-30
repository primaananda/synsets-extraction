#created by primaananda
import csv

#berisi list noun
def get_noun():
    noun = []
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            noun.append(row[1])
    return noun

#berisi list verb
def get_verb():
    verb = []
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            verb.append(row[2])
    return verb

#berisi list adjektiva
def get_adje():
    adje = []
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            adje.append(row[3])
    return adje

#berisi list adverb
def get_adve():
    adve = []
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            adve.append(row[4])
    return adve

#berisi list gabungan antara noun, verb, adjektiva, dan adverb
def get_pasangan(kata):
    pasangan = []
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            pasangan.append(row[1]+row[2]+row[3]+row[4])
    return pasangan

#berisi list kata pertama
def get_kata():
    kata = []
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            kata.append(row[0])
    return kata

def ekstraksi_synset_indonesia():
    daftar_pasangan = []
    daftar_pasangan_tesaurus = []
    calon_synset_tesaurus = []
    count = 0
    with open('hasil/final/tesaurus.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            daftar_pasangan.append(row[1]+row[2]+row[3]+row[4])
            for kata_pasangan in daftar_pasangan:
                count += 1
                print count
                if kata_pasangan in row[0]:
                    daftar_pasangan_tesaurus.append(kata_pasangan)
                    if row[0] in daftar_pasangan_tesaurus:
                        calon_synset_tesaurus.append((row[0], kata_pasangan))
                    else:
                        calon_synset_tesaurus.append(row[0])
    print calon_synset_tesaurus

def main():
    
    noun = get_noun()
    #for x in noun:
    #    print x
    verb = get_kata()
    for x in verb:
        print x
    
ekstraksi_synset_indonesia()