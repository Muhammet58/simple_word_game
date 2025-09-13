contacts = dict()

def print_contacts():
    if not contacts:
        print("Rehberde kayıtlı kişi yok.")
        return False
    print("📒 Rehberdeki kişiler:")
    for idx, item in enumerate(contacts.items(), start=1):
        print(f"{idx}. {item[0]} - {', '.join(item[1])}")
    return True


def phone_number_control(number):
    if not number.isdigit() or len(number) != 10:
        return False
    return True


def add_contact(name, number):
    if phone_number_control(number):
        contacts.setdefault(name.lower(), []).append(number)
        return True
    else:
        return False


def call_contact(name):
    numbers = contacts.get(name.lower())
    if numbers:
        if len(numbers) > 1:
            while True:
                print(f"{name} kişisinin numaraları")
                for i, j in enumerate(numbers, start=1):
                    print(f"{i}. {j}")
                choice = input(f"Hangi numarayı aramak istiyorsunuz? (1-{len(numbers)}): ")
                if choice.isdigit():
                    choice = int(choice)
                    if choice < 1 or choice > len(numbers):
                        print('Geçerli bir sayı giriniz')
                    else:
                        print(f'📞 {name} aranıyor: {numbers[choice-1]}')
                        break
                else:
                    print('Lütfen sayı giriniz')
        else:
            print(f"📞 {name} aranıyor...")
    else:
        print(f"{name} rehberde yok.")


def delete_contact(name):
    if name.lower() in contacts:
        del contacts[name.lower()]
        print(f"{name} silindi.")
    else:
        print(f"{name} rehberde yok.")


def menu():
    while True:
        print(
            "\n--- Telefon Rehberi ---",
            "1 = Kişi ekle",
            "2 = Ara",
            "3 = Sil",
            "4 = Listele",
            "5 = Çıkış",
            sep="\n"
        )
        choice = input("Seçiminizi girin: ")

        if choice == "1":
            while True:
                name = input("İsim: ")
                number = input("Telefon numarası (örn: 5554567890): ")
                if add_contact(name, number):
                     print(f"{name} başarıyla eklendi.")
                     break
                else:
                     print('⚠ Numara eksik veya geçersiz (10 karakter uzunluğunda olmalı ve sayılardan oluşmalı)')


        elif choice == "2":
            if print_contacts():
                name = input("Aramak istediğiniz kişinin ismi: ")
                call_contact(name)

        elif choice == "3":
            if print_contacts():
                name = input("Silmek istediğiniz kişinin ismi: ")
                delete_contact(name)

        elif choice == "4":
            print_contacts()

        elif choice == "5":
            print("👋 Görüşmek üzere!")
            break
        else:
            print("❌ Geçersiz seçim. Tekrar deneyin.")

menu()
