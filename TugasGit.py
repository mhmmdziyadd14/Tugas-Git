data_panen = {
  'lokasi1': {
    'nama_lokasi': 'Kebun A',
    'hasil_panen': {
      'padi': 1200,
      'jagung': 800,
      'kedelai': 500
    }
  },
  'lokasi2': {
    'nama_lokasi': 'Kebun B',
    'hasil_panen': {
      'padi': 1500,
      'jagung': 900,
      'kedelai': 450
    }
  },
  'lokasi3': {
    'nama_lokasi': 'Kebun C',
    'hasil_panen': {
      'padi': 1100,
      'jagung':750,
      'kedelai': 600
    }
  },
  'lokasi4': {
    'nama_lokasi': 'Kebun D',
    'hasil_panen': {
      'padi': 1300,
      'jagung': 850,
      'kedelai': 550
    }
  },
  'lokasi5': {
    'nama_lokasi': 'Kebun E',
    'hasil_panen': {
      'padi': 1400,
      'jagung': 950,
      'kedelai': 480
    }
  }
}

#No 1
for i,j in data_panen.items():
    print(f"Nama Lokasi: {j['nama_lokasi']} \nHasil Panen:") 
    print(f"Padi: {j['hasil_panen']['padi']}, Jagung: {j['hasil_panen']['jagung']}, Kedelai: {j['hasil_panen']['kedelai']}") 
    print() 
    
#No 2
print(f"Hasil jagung dari Lokasi 2: {data_panen['lokasi2']['hasil_panen']['jagung']}")

#No 3
print(f"Nama Lokasi 3: {data_panen['lokasi3']['nama_lokasi']}")
