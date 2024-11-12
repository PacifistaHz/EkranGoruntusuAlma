import time
from PIL import ImageGrab

def ekranGoruntusuAlAl():
    baslangic=time.time()
    goruntu=ImageGrab.grab()
    dosyaAdi="EkranGoruntusu_"+str(time.time_ns())+".jpg"
    goruntu.save(dosyaAdi,"JPEG")
    bitis=time.time()
    print(bitis-baslangic)
ekranGoruntusuAlAl()