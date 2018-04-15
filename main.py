#created by prima ananda

import csv

def txt_to_csv(file, files):
    dicts = []
    for line in file:
        dicts = line.split()
        
        #print dicts
        writer = csv.writer(files)
        writer.writerow(line)

def main():
    file_text = open('hasil/final/tesaurus_clear_text.txt','r')
    file_csv = open('hasil/final/tesaurus.csv','w')
    
    hasil = txt_to_csv(file_text, file_csv)
    
main()