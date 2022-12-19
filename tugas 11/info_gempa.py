from gempa import Gempa

# buat object

g1 = Gempa('Banten', 1.2)
g2 = Gempa('Palu', 6.1)
g3 = Gempa('Cianjur', 5.6)
g4 = Gempa('Jayapura', 3.3)
g5 = Gempa('Garut', 4.0)

# panggil funsi di class Gempa

g1.dampak()
g2.dampak()
g3.dampak()
g4.dampak()
g5.dampak()


print(Gempa.GEMPA,
    "\n---------------------")
g1.cetak()
g2.cetak()
g3.cetak()
g4.cetak()
g5.cetak()
