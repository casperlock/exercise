import random
import time
sayi = random.randint(1,30)
deneme=0
hak=5

yuksek_mesajlar = ["biraz fazla oldu sanki",
                   "o kadar uçma in biraz",
                   "düş kızz",
                   "az daha in"]
dusuk_mesajlar = ["yukarıı",
                  "korkmaa çık",
                  "seviyeni düşürme cnm çık yukarı",
                  "hadi az daha yükselt"]

print("sayı tahmin oyununa hoşgeldin")
time.sleep(1)
print("ben 1-30 arası bir sayı tutacağım, bakalım bilebilecek misin?")
time.sleep(2)
print("sadece 5 hakkın var haberin olsun")
time.sleep(2)
print("hazırsan başlıyoruz ilk tahminle başla bakalım")
time.sleep(2)

while deneme<hak:
    try:
        tahmin= int(input("tahminin nedir? "))
    except ValueError:
        print("yanlıs tuşa basmış olmalısın")
        continue
    
    deneme+=1
    kalan = hak-deneme
    
    if tahmin > sayi:
        print(random.choice(yuksek_mesajlar))
    elif tahmin < sayi:
        print(random.choice(dusuk_mesajlar))
    else:
        print("helal olsun bildin:p")
        print(f"{deneme}. denemede bulabildin")
        
        time.sleep(1)
        break
        
if deneme < 3:
    print("tahmin isinde cok iyisin")
    
                 
elif kalan==0:
    print("oyun bitti,kaybettin canın sağolsun:( ")
    print("tuttuğum sayı buydu:")
    time.sleep(1)
    print(sayi)
else:
    print("eh fena degilsin diyelim")
                   
    
    
               
