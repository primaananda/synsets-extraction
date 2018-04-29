#created by primaananda
import csv
import pandas as pd
from collections import defaultdict

def cari_pasangan(file_csv):
    '''
    columns = defaultdict(list) # each value in each column is appended to a list
    reader = csv.DictReader(file_csv)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
    #print columns['Noun']
    #print columns['Verb']
    #print columns['Adjektiva']
    #print columns['Adverb']
    '''
    noun = []
    verb = []
    adje = []
    adve = []
    reader = csv.reader(file_csv)
    for row in reader:
        noun.append(row[1])
        verb.append(row[2])
        adje.append(row[3])
        adve.append(row[4])
    for x in noun:
        print x


def main():
    open_csv = open('hasil/final/tesaurus.csv','r')
    
    cari_pasangan(open_csv)
    
main()