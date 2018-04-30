#created by primaananda
import csv
import pandas as pd
from collections import defaultdict

def cari_pasangan(file_csv):
    noun = []
    verb = []
    adje = []
    adve = []
    pasangan = []
    reader = csv.reader(file_csv, delimiter=',')
    for row in reader:
        noun.append(row[1])
        verb.append(row[2])
        adje.append(row[3])
        adve.append(row[4])
        pasangan.append(row[1]+row[2]+row[3]+row[4])
        #pasangan.append(row[2])
        #pasangan.append(row[3])
        #pasangan.append(row[4])
        #pasangan.append([row[1],row[2],row[3],row[4]])
    for x in pasangan:
        print x
    #    line = x.split(',')
    #print line
    return pasangan

#def ekstraksi_synset_indonesia():

def main():
    open_csv = open('hasil/final/tesaurus.csv','r')
    
    cari_pasangan(open_csv)
    
main()