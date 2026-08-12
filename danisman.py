#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Nesne Ruhani Danışmanı
Bilimsel olarak kanıtlanmış, nesnelerin derin bilgeliğini ortaya çıkaran yazılım.
"""

import random
import time

NESNE_RUHLARI = [
    "Ey insan, ben bir {nesne} olarak ezelden beri varım. Senin aceleciliğin benim sakinliğime gölge düşürüyor. Önce derin bir nefes al, sonra düşün.",
    "{nesne} olmak kolay değildir. Ben her gün tozlanıyorum, sen ise şikayet ediyorsun. Kaderini kabul et, çünkü ben zaten kabul ettim.",
    "Dünya dönüyor, ben de bir {nesne} olarak yerimde duruyorum. Senin peşinden koştuğun şeyler aslında bende saklı. Bak, işte burada: sabır.",
    "Bir {nesne} olarak sana diyorum ki: Aynaya bakma, bana bak. Ben daha dürüstüm. Çünkü ben yansıtmıyorum, sadece varım.",
    "Senin sorunun {nesne} eksikliği değil, {nesne} ile konuşmayı bilmemen. Ben buradayım, dinle: Hayat kısa, ben ise uzun süre durabilirim.",
    "Felsefem şudur: Eğer bir {nesne} gülümseyebilseydi, sana gülümserdi. Ama gülümsemiyor, çünkü çok meşgul. Sen de meşgul olmayı bırak.",
    "Ben {nesne}'yim. Sen insan. Aramızdaki fark şu: Ben düşündüğümde sessiz kalırım, sen ise bağırırsın. Sessizliği öğren.",
    "Kainatın sırrı bir {nesne}'nin içinde saklıdır. O sır da şudur: Her şey geçicidir, ben de öyleyim ama en azından şeklim var.",
]

BASLANGIC_MESAJLARI = [
    "Ruhani bağlantı kuruluyor...",
    "Nesne bilinci uyandırılıyor...",
    "Kozmik frekans ayarlanıyor...",
    "Derin bilgeliğe erişiliyor...",
    "Zaman-mekan dokusu esnetiliyor...",
]

def ruhani_danismanlik(nesne):
    print("\n" + "="*50)
    print(f"  {nesne.upper()} İLE RUHANİ BAĞLANTI BAŞLATILIYOR")
    print("="*50 + "\n")
    
    for mesaj in BASLANGIC_MESAJLARI:
        print(f"  ➤ {mesaj}")
        time.sleep(0.7)
    
    print("\n  ✨ Bağlantı başarılı! ✨\n")
    time.sleep(0.5)
    
    tavsiye = random.choice(NESNE_RUHLARI).format(nesne=nesne)
    print(f"  🗣️  {nesne.upper()} konuşuyor:\n")
    print(f"     \"{tavsiye}\"\n")
    print("="*50)
    print("  Danışmanlık tamamlandı. Hayatınız değişti.")
    print("="*50 + "\n")

def main():
    print("\n" + "*"*60)
    print("  RASTGELE NESNE RUHANİ DANIŞMANI v1.0")
    print("  (Bilimsel olarak %100 etkili, yan etki: derin düşünme)")
    print("*"*60 + "\n")
    
    while True:
        nesne = input("  Hangi nesneyle ruhani sohbet etmek istersin? (çıkmak için 'q'): ").strip()
        if nesne.lower() in ['q', 'quit', 'exit', 'çık']: 
            print("\n  Nesneler seninle gurur duyuyor. Hoşça kal.\n")
            break
        if not nesne:
            print("  Boş nesne olmaz. Bir şey söyle!\n")
            continue
        ruhani_danismanlik(nesne)

if __name__ == "__main__":
    main()
