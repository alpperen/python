
def hesapla(ifade):
    try:
        return eval(ifade)
    except:
        return "Geçersiz ifade!"

def hesap_makinesi():
    print("Matematiksel İfadeler Hesap Makinesine Hoş Geldiniz!")
    print("Çıkış yapmak için 'exit' yazın.")

    while True:
        ifade = input("Hesaplamak istediğiniz ifadeyi girin: ")

        if ifade.lower() == "exit":
            print("Hesap Makinesinden çıkılıyor...")
            break

        sonuc = hesapla(ifade)
        print("Sonuç:", sonuc)

if __name__ == "__main__":
    hesap_makinesi()

# I know it's so bad
