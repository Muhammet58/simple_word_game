print("Metin Analiz Programı")
text = input('Bir metin girin: ')

splited_text = text.split()
text_dict = {}

for item in splited_text:
    if item not in text_dict:
        text_dict[item] = {
            'count': 1,
            'length': len(item)
        }
    else:
        text_dict[item]['count'] += 1

tekrar_eden = []
tekrar_etmeyen = []
for key, value in text_dict.items():
    print(f"{key} -> {value['count']} adet kullanılmış, {value['length']} karakterden oluşuyor")
    if value['count'] > 1:
        tekrar_eden.append(key)
    else:
        tekrar_etmeyen.append(key)

info_text = f"""
Metindeki Toplam Kelime Sayısı: {len(splited_text)}
En Çok Tekrar Eden Kelimeler: {', '.join(tekrar_eden)}
Tekrar etmeyen Kelimeler: {', '.join(tekrar_etmeyen)}
En Kısa Kelime: {min(text_dict.items(), key=lambda x: x[1]['length'])[0]} - {len(min(text_dict.items(), key=lambda x: x[1]['length'])[0])} Karakter 
En Uzun Kelime: {max(text_dict.items(), key=lambda x: x[1]['length'])[0]} - {len(max(text_dict.items(), key=lambda x: x[1]['length'])[0])} Karakter 
"""

print(info_text)