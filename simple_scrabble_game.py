from random import sample
import requests
from googletrans import Translator


def rastgele_harf_sec(harfler, kalan_yenileme):
    if kalan_yenileme > 0:
        yeni_harfler = sample(harfler, k=7)
        print(', '.join(yeni_harfler))
        return yeni_harfler, kalan_yenileme - 1
    else:
        print('Harf yenileme hakkınız bitmiş')
        return None, kalan_yenileme


def harf_tablosu(harfler):
    print('+--------+--------+--------+')
    print('|  HARF  |  ADET  |  PUAN  |')
    print('+--------+--------+--------+')
    for harf, (adet, puan) in harfler.items():
        print(f"|   {harf}    |{f'   {adet}   ' if len(str(adet)) == 2 else f'   {adet}    '}|{f'   {puan}   ' if len(str(puan)) == 2 else f'   {puan}    '}|")
    print('+--------+--------+--------+')


def harfler_gecerlimi(kelime, harfler):
    temp = harfler.copy()
    for item in kelime:
        if item in temp:
            temp.remove(item)
        else:
            return False
    return True


def oyunu_baslat_devam_et(harfler, rastgele_harfler, kullanici_puani, adedince_harfler):
    print('Harfler çekiliyor...')
    print(', '.join(rastgele_harfler))
    kelime = input('Yukarıdaki harfler ile anlamlı bir ingilizce kelime giriniz: ').strip().upper()

    if not harfler_gecerlimi(kelime, rastgele_harfler):
        print("Girilen kelime eldeki harfler ile oluşturulamıyor!")
        return rastgele_harfler, kullanici_puani
    
    if len(harfler) == 1:
        print("Lütfen sadece tek harf değil, anlamlı bir kelime giriniz!")
        return rastgele_harfler, kullanici_puani
    
    try:
        sozluk_api = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{kelime}")
        sozluk_api.raise_for_status()
    except Exception:
        print('Kelime bulunamadı')
        return rastgele_harfler, kullanici_puani

    for harf in kelime:
        if harf in harfler and harfler[harf][0] > 0:
            harfler[harf][0] -= 1
            kullanici_puani += harfler[harf][1]
            rastgele_harfler.remove(harf)
            adedince_harfler.remove(harf)

            if harfler[harf][0] == 0:
                del harfler[harf]
                print(f"{harf} harfi kalmadı!")            

    yeni_harfler = sample(adedince_harfler, k=7-len(rastgele_harfler))
    rastgele_harfler.extend(yeni_harfler)
    
    translator = Translator()
    kelime_tr = translator.translate(kelime, src='en', dest='tr').text
    tanim_tr = translator.translate(sozluk_api.json()[0]['meanings'][0]['definitions'][0]['definition'], src='en', dest='tr').text
    print(f"Kelimenin Türkçe anlamı ve sözlükteki karşılığı: {kelime_tr}, {tanim_tr}")
    print(f'Kelime kabul edildi! Toplam puanınız: {kullanici_puani}')
    return rastgele_harfler, kullanici_puani


def main():
    harfler_adetler_puanlar_en = {
        "A": [9, 1], "B": [2, 3], "C": [2, 3], "D": [4, 2], "E": [12, 1],
        "F": [2, 4], "G": [3, 2], "H": [2, 4], "I": [9, 1], "J": [1, 8],
        "K": [1, 5], "L": [4, 1], "M": [2, 3], "N": [6, 1], "O": [8, 1],
        "P": [2, 3], "Q": [1, 10], "R": [6, 1], "S": [4, 1], "T": [6, 1],
        "U": [4, 1], "V": [2, 4], "W": [2, 4], "X": [1, 8], "Y": [2, 4],
        "Z": [1, 10]
    }

    adedince_harf = []
    harfler = list(harfler_adetler_puanlar_en.keys())
    adetler = [item[0] for item in list(harfler_adetler_puanlar_en.values())]

    for harf, adet in list(zip(harfler, adetler)):
        adedince_harf.extend([harf] * adet)

    rastgele_harfler = sample(adedince_harf, k=7)
    kullanici_puani = 0
    harf_yenileme = 3

    while True:
        print('\nKelime oyununa Hoşgeldiniz', 
            f'1 - Harfleri Yenile (Kalan Harf Yenileme: {harf_yenileme})', 
            '2 - Harf Tablosu', 
            '3 - Oyunu başlat/Devam et',
            '4 - Çıkış\n', sep='\n')
        secim = input('Lütfen yapmak istediğiniz işleme karşılık gelen numarayı giriniz: ')

        match secim:
            case '1':
                yeni_harfler, harf_yenileme = rastgele_harf_sec(adedince_harf, harf_yenileme)
                if yeni_harfler:
                    rastgele_harfler = yeni_harfler
            case '2':
                harf_tablosu(harfler_adetler_puanlar_en)
            case '3':
                rastgele_harfler, kullanici_puani = oyunu_baslat_devam_et(harfler_adetler_puanlar_en, rastgele_harfler, kullanici_puani, adedince_harf)
            case '4':
                print(f'Toplam Puan: {kullanici_puani}')
                print('👋 Görüşürüz...')
                break
            case _:
                print('Geçersiz tuşlama')


if __name__ == "__main__":
    main()
