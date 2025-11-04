import time 

KONTROL_HARFİ = 'a'
led_durumu = False 


def toggle_led_simulasyonu():
    """LED'in durumunu tersine çevirir ve sonucu ekrana yazdırır."""
    global led_durumu    
    led_durumu = not led_durumu
    if led_durumu:
        mesaj = "LED AÇILDI"
    else:
        mesaj = "LED KAPANDI"        
    print(f"[{time.strftime('%H:%M:%S')}] '{KONTROL_HARFİ}' tuşuna basıldı. -> {mesaj}")
def run_simulasyon():
    print("-" * 50)
    print("BASİT LED ANAHTARI SİMÜLASYONU BAŞLATILDI")
    print(f"Kontrol Harfi: '{KONTROL_HARFİ}' | Çıkış için 'q'")
    print("-" * 50)
    try:
        while True:           
            komut = input(f"'{KONTROL_HARFİ}' tuşuna basarak durumu değiştirin: ").strip().lower()            
            if komut == KONTROL_HARFİ:
                               toggle_led_simulasyonu()
            elif komut == 'q':
                break
            else:
                print("Geçersiz komut. Lütfen kontrol harfini veya 'q'yu kullanın.")
    except (KeyboardInterrupt, EOFError):        
        pass     
    finally:
        print("\nSimülasyon sonlandırıldı.")
run_simulasyon()