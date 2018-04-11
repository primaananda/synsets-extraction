#created by primaananda

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
    
    for k in dicts:
        temp = k.replace('  ','')
        dicts2.append(temp)
    '''
    for k in dicts:
        for ch in ['   ','  ']:
            if ch in k:
                temp = k.replace(ch,'')
                dicts2.append(temp)
    '''
    return dicts2
    
#perulangan untuk menulis hasil yang ada di dicts2 kedalam file txt bernama tesaurus_clear_text.txt
def add_file(dicts2, files):
    for x in dicts2:
        files.write(x+'\n')

def main():
    file = open('hasil/final/tesaurus_hasil_convert_from_pdf.txt','r')
    files = open('hasil/final/tesaurus_clear_text.txt','w')
    
    d_clear = clear_tab(file)
    d_add = add_specific_text(d_clear)
    d_specific = delete_specific_char(d_add)
    
    add_file(d_specific, files)
    
    file.close()
    files.close()

main()