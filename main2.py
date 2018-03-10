"""
created by : Prima Ananda
"""
import json

#untuk membaca data tesaurus
file_tesaurus = open('resources/tesaurus2008.json','r')
#untuk baca file json tesaurus
with file_tesaurus as jsonf:
    tesaurus = json.load(jsonf)

#untuk baca detail data
#for kata in tesaurus:
#    for synset in tesaurus[kata] :
#        print(kata, synset)

def CariPasangan(kata):
    hasilKata = []
    for synset in tesaurus[kata] :
        hasilKata.append(synset)
    return hasilKata

def EkstraksiSynsetIndonesiaMonolingualResources():
    daftarPasangan = []
    daftarPasanganTesaurus = []
    CalonSynsetTesaurus = []
    for kata in tesaurus:
        daftarPasangan = CariPasangan(kata)
        for kataPasangan in daftarPasangan:
            if kataPasangan in tesaurus:
                daftarPasanganTesaurus.append(kataPasangan)
                if kata in daftarPasanganTesaurus:
                    CalonSynsetTesaurus.append((kata, kataPasangan))
                else:
                    CalonSynsetTesaurus.append(kata)
        print(CalonSynsetTesaurus)

EkstraksiSynsetIndonesiaMonolingualResources()

#def main():
#    CariPasangan()

#main()