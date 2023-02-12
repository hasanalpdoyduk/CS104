import sys

#     Vize1 toplam notun %30'una etki edecek.
#     Vize2 toplam notun %30'una etki edecek.
#     Final toplam notun %40'ına etki edecek.
#
#     Toplam Not >=  90 -----> AA
#     Toplam Not >=  85 -----> BA
#     Toplam Not >=  80 -----> BB
#     Toplam Not >=  75 -----> CB
#     Toplam Not >=  70 -----> CC
#     Toplam Not >=  65 -----> DC
#     Toplam Not >=  60 -----> DD
#     Toplam Not >=  55 -----> FD
#     Toplam Not <  55 -----> FF

vize1 = int(input("Birinci vizenin sonucunu giriniz: "))
while vize1 > 100:
    print("Birinci vize sonucunuzu hatalı girdiniz.\nTekrar deneyiniz!")
    vize1 = int(input("Birinci vizenin sonucunu tekrar giriniz: "))
vize2 = int(input("İkinci vizenin sonucunu giriniz: "))
while vize2 > 100:
    print("İkinci vize sonucunuzu hatalı girdiniz.\nTekrar deneyiniz!")
    vize2 = int(input("İkinci vizenin sonucunu tekrar giriniz: "))
vize3 = int(input("Üçüncü vizenin sonucunu giriniz: "))
while vize3 > 100:
    print("Üçüncü vize sonucunuzu hatalı girdiniz.\nTekrar deneyiniz!")
    vize3 = int(input("Üçüncü vizenin sonucunu tekrar giriniz: "))

toplam_not = (vize1 * 3 + vize2 * 3 + vize3 * 4) / 10

if toplam_not >= 90:
    print("AA")
elif toplam_not >= 85:
    print("BA")
elif toplam_not >= 80:
    print("BB")
elif toplam_not >= 75:
    print("CB")
elif toplam_not >= 70:
    print("CC")
elif toplam_not >= 65:
    print("DC")
elif toplam_not >= 60:
    print("DD")
elif toplam_not >= 55:
    print("FD")
else:
    print("FF")
