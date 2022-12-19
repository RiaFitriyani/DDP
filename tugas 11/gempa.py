class Gempa:
    # member 1 variabel

    lokasi = ''
    skala = ''
    Gempa = "Dampak dari terjadi Gempa"
    
    # member 2 konstrruktur
    def _init_(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        self.dampak = ""
        
        # member 3 method
    def dampak(self):
        if(self.skala <= 2):
             self.dampak ="tidak terasa"
        elif(self.skala >=2 and self.skala <4):
            self.dampak = "Bangunan retak - retak"
        elif(self.skala >=4 and self.skala <6):
           self.dampak = "Bangunan pada roboh"
        else:
                self.dampak = "Bangunan roboh dan berpotensi tsunami"

    def cetak(self):
        print(
                '\n==========================='
                '\nLokasi \t:',self.lokasi,
                '\nSkala\t\t:',self.skala,
                '\nDampak Gempa\t\t:',self.dampak,
                '\n===============================')
            