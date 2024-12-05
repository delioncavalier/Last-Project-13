#dataframe kosong
halo = pd.DataFrame()
print(halo)

#dataframe dari list
anak = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df = pd.DataFrame(anak, columns=["Random"])
df.index += 1
print(df)

#dataframe dari multiple list, header kolom buat sendiri, buat isinya dulu
hewan = [["Anjing", "Hidup"], ["Kucing", "Mati"]]
deef = pd.DataFrame(hewan, columns=["Hewan", "Status"])
deef.index += 1
print(deef)

#dataframe dari list, buat isinya dulu, terus kolom bisa buat sendiri
pembeli = [["Anak Kosan", "Ilham", "Bandung"], ["Anak Kosan", "Andre", "Ambulu"]]
tabelatas = ["Kategori", "Nama", "Asal"]
defi = pd.DataFrame(pembeli, columns=tabelatas)
defi.index += 1
print(defi)

#dataframe dari dictionary, langsung ada headernya coy
barang = {'Organik': ['Bola', 'Kerang', 'Pisang'],
        'Anorganik': ['Bakso', 'Sapi', 'Kambing']}
delfi = pd.DataFrame(barang)
delfi.index += 1
print(delfi)

#menyimpan ke csv
delfi.to_csv(stok_data_harga_barang, index=False)

#membaca csv dari variabel csv
with open(stok_data_harga_barang, 'r') as bacaan:
    barange = bacaan.read()
    print(barange)
    
#membaca csv dengan pandas
wede = pd.read_csv(stok_data_harga_barang)
wede.index += 1
print(wede)

#cek head dan tail
print(delfi.head(2)) #->daftar 2 baris pertama
print("="*24)
print(delfi.tail(2)) #->daftar 2 baris terakhir

#cek info dataframe
print(delfi.info())

print("="*24)
#cek kolom tertentu
print(delfi.Organik)
print("="*24)
print(delfi.Anorganik)

print(delfi)
#cek baris tertentu
print(delfi.iloc[1:2])
#cek baris dan kolom tertentu
print(delfi.iloc[0,1])