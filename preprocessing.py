#created by primaananda
import re
import csv

types = ['v','a','n','adv', 'p', 'pron', 'num']

#perulangan untuk menghilangkan baris tab dan hanya mengambil yang tidak ada tabnya dan dimasukan kedalam tampungan dicts
def clear_tab(file):
    dicts = []
    lines = file.readline()
    while lines:
        if(not lines.startswith('\t')):
            dicts.append(lines.rstrip())
        lines = file.readline()
        if not lines:
            break
    return dicts

#merapikan text untuk yang kata"nya kepotong dan mengambil text yang diperlukan perulangan untung membaca dan menampung huruf sesuai yang di awali oleh kress(#) : contoh bila #A maka yang ditampung huruf awalny A
def add_specific_text(dicts):
    dicts2 = []
    letter = '###'
    for x in range(0,len(dicts)):
        temp = ''
        if(dicts[x].startswith('#')):
            letter = dicts[x][1].lower() #.lower berfungsi untuk membuat huruf kapital menjadi kecil
        if(dicts[x].startswith(letter)):
            temp += dicts[x]
            while(dicts[x].endswith(',')) or (dicts[x].endswith('-')):
                if(dicts[x].endswith(',')): #kalau diakhiri ',' maka kata/kalimat digabung dengan kata/kalimat berikutnya
                    temp = temp + ' '
                    temp += dicts[x+1]
                    x =  x+1
                elif(dicts[x].endswith('-')): #kalau diakhiri '-' maka huruf terakhir yaitu - dihilangkan lalu digabungkan dengan kata berikutnya
                    temp = temp[:-1]
                    temp += dicts[x+1]
                    x = x+1
            dicts2.append(temp)
    return dicts2

#hapus whiespace yang berlebihan dan hapus kata kata yang tidak diperlukan seperti (cak), k, adv
def delete_specific_char(dicts):
    dicts2 = []
    temp = ''
    '''
    stopwords = ['  ',
    '    ',
    ' (cak)',
    '1 ',
    '2 ',
    ' (ki)',
    'pron ',
    '(kan) ',
    '(pen) ',
    '(an)']
    
    print stopwords
    
    '''
    for k in dicts:
        #k = re.sub(r'\(.+\)','',k) #menghilangkan kata yang dalam '(kata)'
        for ch in ['  ','	 ', '1 ', '2 ', '3 ', '4 ', '5', '6']:
            if ch in k:
                k = k.replace(ch,'')
        for ch2 in [';']:
            if k.endswith(ch2):
                k = k.replace(ch2,'')
            else:
                k = k.replace(ch2,',')
        temp = k
        dicts2.append(temp)
    
    return dicts2
    
#perulangan untuk menulis hasil yang ada di dicts2 kedalam file txt bernama tesaurus_clear_text.txt
def add_file(dicts2, files):
    for x in dicts2:
        files.write(x+'\n')

def get_lowest_type_index(line):
    value = []
    for type in types :
        if(type in line):
            value.append(line.index(type))
    return min(value)

def get_type_sequence(line):
    sequence = []
    for word in line:
        if(len(word) == 1):
            sequence.append(word)
    return sequence

def get_type_index(types, line):
    sequence = []
    for type in types:
        sequence.append(line.index(type))
    return sequence

#merubah ke csv
def txt_to_csv(file, files):
    dicts = []
    writer = csv.writer(files)
    writer.writerow(["Kata","Noun","Verb","Adjektiva","Adverb"])
    for line in file:
        dicts = [x.rstrip(',') for x in line.split()]
        #print dicts
        #####
        '''
        for x in range(0, len(dicts)):
            if dicts[x] == 0:
                word = dicts[0:get_lowest_type_index(dicts)]
            elif dicts[x] == types:
                dicts = dicts[get_lowest_type_index(dicts):]
        '''
        #####
        word = dicts[0:get_lowest_type_index(dicts)]
        dicts = dicts[get_lowest_type_index(dicts):]
        sequence = get_type_sequence(dicts)
        index_sequence = get_type_index(sequence, dicts)
        index_sequence.append(len(dicts))
        type = []
        for x in range(0, len(index_sequence)-1):
            type.append(dicts[index_sequence[x]:index_sequence[x+1]])
        print word
        writer.writerow(dicts)
        
    
def main():
    file = open('hasil/final/tesaurus_hasil_convert_from_pdf.txt','r')
    file_text_write = open('hasil/final/tesaurus_clear_text.txt','w')
    file_csv = open('hasil/final/tesaurus.csv','w')
    
    d_clear = clear_tab(file)
    d_add = add_specific_text(d_clear)
    d_specific = delete_specific_char(d_add)
    
    #import to txt
    add_file(d_specific, file_text_write)
    
    #txt to csv
    txt_to_csv(d_specific, file_csv)
    
    file.close()
    file_text_write.close()

    #testing
    '''
    s = 'abcd (aaaa) efgh'
    abcd = re.sub(r'\(.+\)','',s)
    print abcd
    x='dasdasdsafs[image : image name : image]vvfd gvdfvg dfvgd'
    hsak = re.sub(r'\[.+\]','',x)
    print hsak
    '''
main()