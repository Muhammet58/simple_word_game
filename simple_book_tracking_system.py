from collections import Counter

def arama_siralama_kategorileri(process_type):
    category_list = ["\n1 = İsim", "2 = Yazar", "3 = Sayfa", "4 = Tür", "5 = Okundu", "6 = Okunmadı"]
    if process_type != "search":
        category_list.pop(-1)
        category_list[-1] = "5 = Okundu Bilgisi"

    print(*category_list, sep="\n")


def kitap_ekle(library):
    isim = input("Kitap adını giriniz: ").strip()
    yazar = input("Kitap yazarını giriniz: ").strip()
    sayfa = input("Kitabın sayfa sayısını giriniz: ").strip()
    tür = input("Kitap türünü giriniz: ").strip()

    library.append(
        {
            "name": isim, 
            "writer": yazar,
            "page": sayfa,
            "type": tür,
            "is_read": False, 
        }
    )

    print("✅ Kitap başarıyla eklendi")


def kitap_duzenle(library):
    if not library:
        print('Sistemde kayıtlı kitap bulunamadı kitap eklemeyi deneyebilirsiniz')
    else:
        print(*[f"{number} = {item}" for number, item in enumerate(library, start=1)], sep="\n")
        while True:
            secim = input("Düzenlemek istediğiniz kitabın sıra numarasını giriniz: ")

            match secim:
                case s if s.isdigit():
                    secim = int(s)
                    if 1 <= secim <= len(library):
                        secilen_kitap = library[secim-1]

                        while True:
                            print(f"\n1 = İsim: {secilen_kitap['name']}", 
                                f"2 = Yazar: {secilen_kitap['writer']}",
                                f"3 = Sayfa: {secilen_kitap['page']}", 
                                f"4 = Tür: {secilen_kitap['type']}", 
                                f"5 = Okundu Bilgisi: {'Okundu' if secilen_kitap['is_read'] == True else 'Okunmadı'}", sep="\n")
                            
                            düzenlencek_kisim = input("Düzenlemek istediğiniz kısmın sıra numarasını giriniz: ")
                            match düzenlencek_kisim:
                                case '1' | '2' | '3' | '4' | '5':
                                    if düzenlencek_kisim != '5':
                                        yeni_deger = input('Lütfen yeni değeri giriniz: ')
                                        düzenlencek_kisim_dict = {'1': "name", '2': "writer", '3': "page", '4': "type"}
                                        secilen_kitap[düzenlencek_kisim_dict[düzenlencek_kisim]] = yeni_deger
                                    else:
                                        secilen_kitap['is_read'] = False if secilen_kitap['is_read'] == True else True
                                    print(f"✅ Seçilen kitap başarıyla düzenlendi")
                                    break
                                case _:
                                    print('Lütfen geçerli bir sayı giriniz!')
                        break
                    else:
                        print("Geçersiz sıra numarası! Tekrar deneyin.")
                case _:
                    print("Lütfen geçerli bir sayı giriniz!")


def kitap_sil(library):
    if not library:
        print('Sistemde kayıtlı kitap bulunamadı kitap eklemeyi deneyebilirsiniz')
    else:
        print(*[f"{number} = {item}" for number, item in enumerate(library, start=1)], sep="\n")
        while True:
            secim = input("Silmek istediğiniz kitabın sıra numarasını giriniz: ")

            match secim:
                case s if s.isdigit():
                    secim = int(s)
                    if 1 <= secim <= len(library):
                        silinen = library.pop(secim - 1)
                        print(f'"{silinen}" başarıyla silindi.')
                        break
                    else:
                        print("Geçersiz sıra numarası! Tekrar deneyin.")
                case _:
                    print("Lütfen geçerli bir sayı giriniz!")


def kitap_ara(library, key_type, keyword=None):
    filtered_books = []
    key_type_dict = {'1': "name", '2': "writer", '3': "page", '4': "type"}

    match key_type:
        case '5' | '6':
            is_read = True if key_type == '5' else False
            filtered_books = list(filter(lambda x: x["is_read"] == is_read, library))
        case _:
            filtered_books = list(filter(lambda x: keyword in x[key_type_dict[key_type]].lower(), library))

    print(*filtered_books, sep="\n")
                

def kitap_sirala(library, key_type, order_type):
    reversed = order_type == '2'
    key_type_dict = {'1': "name", '2': "writer", '3': "page", '4': "type", '5': "is_read"}
    sorted_library = sorted(library, key=lambda x: x[key_type_dict[key_type]], reverse=reversed)

    print(*sorted_library, sep="\n")


def analiz_yap(library):
    if not library:
        print('Sistemde kayıtlı kitap bulunamadı kitap eklemeyi deneyebilirsiniz')
    else:
        is_readed_books = list(filter(lambda x: x['is_read'] == True, library))
        is_not_readed_books = list(filter(lambda x: x['is_read'] == False, library))
        page_length = list(map(lambda x: x['page'], library))
        type_list = list(map(lambda x: x['type'], library))

        print(
            f"\nToplam Kitap Sayısı: {len(library)}", 
            f"Okunmuş Kitap Sayısı: {len(is_readed_books)}", 
            f"Okunmamış Kitap Sayısı: {len(is_not_readed_books)}",
            f"Ortalama Sayfa Sayısı: {sum(page_length) // len(page_length)}",
            f"En Uzun Kitabın Sayfa Sayısı: {max(page_length)}",
            f"En Kısa Kitabın sayfa Sayısı: {min(page_length)}",
            f"Tür Bazlı Kitap Sayısı: {dict(Counter(type_list))}", sep="\n"
        )


def menu():
    kitaplar = []

    while True:
        print("\nKitap Takip Sistemine Hoşgeldiniz 📚",
            "1 = Kitap Ekle",
            "2 = Kitap Düzenle",
            "3 = Kitap Sil",
            "4 = Kitap Ara", 
            "5 = Kitap Sırala", 
            "6 = Analiz Yap", 
            "7 = Sistemden Çıkış Yap", sep="\n")
        
        secim = input("Yapmak istediğiniz işlemin sıra numarasını giriniz: ").strip()

        match secim:
            case '1':
                kitap_ekle(kitaplar)
            case '2':
                kitap_duzenle(kitaplar)
            case '3':
                kitap_sil(kitaplar)
            case '4':
                if not kitaplar:
                    print('Sistemde kayıtlı kitap bulunamadı kitap eklemeyi deneyebilirsiniz')
                    continue
                arama_siralama_kategorileri("search")
                while True:
                    arama_secimi = input("Arama yapmak istediğiniz kategorinin sıra numarasını giriniz: ").strip()
                    match arama_secimi:
                        case '1' | '2' | '3' | '4':
                            anahtar_kelime = input("Anahtar kelime giriniz: ").strip().lower()
                            kitap_ara(kitaplar, arama_secimi, anahtar_kelime)
                            break
                        case '5' | '6':
                            kitap_ara(kitaplar, arama_secimi)
                            break
                        case _:
                            print("Lütfen geçerli bir seçim yapınız")
            case '5':
                if not kitaplar:
                    print('Sistemde kayıtlı kitap bulunamadı kitap eklemeyi deneyebilirsiniz')
                    continue

                arama_siralama_kategorileri("order")
                while True:
                    siralama_secimi = input("Sıralama yapmak istediğiniz kategorinin sıra numarasını giriniz: ").strip()
                    match siralama_secimi:
                        case '1' | '2' | '3' | '4' | '5' | '6':
                            while True:
                                print("\n1 = Küçükten Büyüğe", "2 = Büyükten Küçüğe", sep="\n")
                                siralama_tipi = input("Sıralama türünü seçin: ").strip()
                                match siralama_tipi:
                                    case '1' | '2':
                                        kitap_sirala(kitaplar, siralama_secimi, siralama_tipi)
                                        break
                                    case _:
                                        print("Lütfen geçerli bir seçim yapınız")
                            break
                        case _:
                            print("Lütfen geçerli bir seçim yapınız")
            case '6':
                analiz_yap(kitaplar)
            case '7':
                print("👋 Görüşürüz...")
                break
            case _:
                print("Geçersiz seçim lütfen belirtilen işlemlerden birini seçiniz.")


if __name__ == "__main__":
    menu()