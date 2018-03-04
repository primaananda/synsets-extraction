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
#for kata, synset in tesaurus.items():
#    print("kata : ", kata)
#    print("synset : ",str(synset))

def CariPasangan(kata):
    for kata, synset in tesaurus.items():
        hasilKata = kata
    return hasilkata

def TambahCalonSynset():
    print('hello')

def EkstraksiSynsetIndonesiaMonolingualResources():
    for kata in tesaurus.items():
        daftarPasangan = CariPasangan(kata)
        print("kata : ",daftarPasangan)
    for kataPasangan in daftarPasangan():
        if kataPasangan in tesaurus.items():
            DaftarPasanganTesaurus = kataPasangan
            if kata in DaftarPasanganTesaurus:
                CalonSynsetTesaurus = kata
            else:
                CalonSynsetTesaurus = kataPasangan
    print(CalonSynsetTesaurus)

EkstraksiSynsetIndonesiaMonolingualResources()