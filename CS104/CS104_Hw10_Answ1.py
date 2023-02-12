print("ÜÇGEN Mİ DÖRTGEN Mİ?")
print("Üçgen için 3 yazınız!")
print("Dörtgen için 4 yazınız!")
a = int(input("Lütfen seçim yapınız: "))
while not (a == 3 or a == 4):
    print("Yanlış sayı tuşladınız!")
    a = int(input("Lütfen tekrar seçim yapınız: "))

if a == 3:
    k1 = int(input("Üçgenin birinci kenarını giriniz: "))
    while k1 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        k1 = int(input("Üçgenin birinci kenarını tekrar giriniz: "))
    k2 = int(input("Üçgenin ikinci kenarını giriniz: "))
    while k2 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        k2 = int(input("Üçgenin ikinci kenarını tekrar giriniz: "))
    k3 = int(input("Üçgenin üçüncü kenarını giriniz: "))
    while k3 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        k3 = int(input("Üçgenin üçüncü kenarını tekrar giriniz: "))
    if abs(k1 - k2) < k3 < abs(k1 + k2):
        if k1 == k2 == k3:
            print("Eşkenar üçgen!!!")
        elif k1 == k2:
            print("İkizkenar üçgen!!!")
        elif k1 == k3:
            print("İkizkenar üçgen!!!")
        elif k2 == k3:
            print("İkizkenar üçgen!!!")
        else:
            print("Çeşitkenar üçgen!!!")
    else:
        print("Seçtiğiniz kenarlar bir üçgen belirtmiyor!")
else:
    m1 = int(input("Dörtgenin birinci kenarını giriniz: "))
    while m1 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        m1 = int(input("Dörtgenin birinci kenarını tekrar giriniz: "))
    m2 = int(input("Dörtgenin ikinci kenarını giriniz: "))
    while m2 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        m2 = int(input("Dörtgenin ikinci kenarını tekrar giriniz: "))
    m3 = int(input("Dörtgenin üçüncü kenarını giriniz: "))
    while m3 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        m3 = int(input("Dörtgenin üçüncü kenarını tekrar giriniz: "))
    m4 = int(input("Dörtgenin dördüncü kenarını giriniz: "))
    while m4 <= 0:
        print("Hatalı kenar girişi yaptınız!")
        m4 = int(input("Dörtgenin dördüncü kenarını tekrar giriniz: "))
    if m1 == m2 == m3 == m4:
        print("Kare!!!")
    elif (m1 == m2 and m3 == m4):
        print("Dikdörtgen ya da paralelkenar!!!")
    elif (m1 == m3 and m2 == m4):
        print("Dikdörtgen ya da paralelkenar!!!")
    elif (m1 == m4 and m2 == m3):
        print("Dikdörtgen ya da paralelkenar!!!")
    else:
        print("Sıradan bir dörtgen!!!")
