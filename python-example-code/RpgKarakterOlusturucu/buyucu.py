from karakter import Karakter
import random

class Buyucu(Karakter):
    def __init__(self,isim):
        super().__init__(isim,"Büyücü")
        self.hadsizlik=2
        self.fabrika=2
        self.ask=2
        self.sarayKontrolu=2
        self.can=300
        self.buyuNufuzu=2
        self.savasciKontrolSkoru = 1
        self.hasar=2



    def seviye_arttir(self):
        self.seviye += 1
        self.xp = 0
        self.yeniXpdegeri += 10
        print(f"{self.isim} seviye atladı! yeni seviye: {self.seviye}")

    def buyucuPasif(self):
        if self.can < 80 or self.can > 40:
            self.hasar += 10
            self.xp += 3
        if self.buyuNufuzu>=5:
            self.hasar+=5
        return self.hasar
        
            
    def saldir(self,diger):
        if self.can <= 0:
            self.cani_degistir(-self.can)
            print(f"{self.isim} baygın! saldıramaz")
            return
        if diger.can <= 0:
            diger.cani_degistir(-diger.can)
            print(f"{diger.isim} zaten baygın")
            return
        
        if self.ultiSeviye > 6:
            self.hasar = random.randint(25,35)
            if self.hasar>30:
                diger.zırh -=5
                if diger.zırh<0:
                    diger.zırh=0
        else:
            self.hasar = random.randint(15,35)
            if self.hasar>25:
                diger.zırh=0
                if self.savasciKontrolSkoru>0:
                    self.savasciKontrolSkoru-=1


        if diger.tur=="Savaşçı":
            if diger.buyucuKontrolSkoru>=3:
                self.hasar = 0
                diger.buyucuKontrolSkoru=0
                print(f"{self.isim}, {diger.isim} adlı karaktere {self.hasar} hasar verdi!")
        else:
            self.hasar = self.buyucuPasif()
            diger.cani_degistir(-(self.hasar - diger.zırh)) 
            self.xp += 15
            print(f"{self.isim}, {diger.isim} adlı karaktere {self.hasar} büyü hasarı verdi!")
        
        
        if self.xp >= self.yeniXpdegeri:
            self.seviye_arttir()
            self.buyuNufuzu+=1
            if self.seviye >=2:
                self.ultiSeviye += 1
                self.buyuNufuzu+=1
                self.savasciKontrolSkoru+=1
                diger.cani_degistir(10)

        


