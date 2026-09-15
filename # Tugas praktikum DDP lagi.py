# Sebenarnya saya suka buku
# Tapi NIM saya genap....
# Jadi... saya buat program tentang penjualan novel di toko buku saja Bang
print("Judul yang Tersedia: Khusus Novel")

# Pertama: Ini daftar novel beserta harga dan stoknya
novel = {
    "teenlit lokal" : {
        "Malioboro at Midnight" : [99000, 9],
        "Galaksi Andromeda" : [100000, 5],
        "Bandung After Rain" : [99000, 11],
        "Nabastala Juang" : [89000, 7],
        "Janji di Negeri Belanda" : [119000, 7]
    },
    "kanon Indonesia" : {
        "Lintang Kemukus Dini Hari" : [40000, 3],
        "Jantera Bianglala" : [40000, 4],
        "Gadis Kretek" : [80000, 9],
        "Anak Semua Bangsa" : [180000, 8],
        "Salah Asuhan" : [115000, 3]
    },
    "misteri" : {
        "Malice" : [100000, 6],
        "Kesetiaan Mr. X" : [85000, 6],
        "Misteri Penginapan Tua" : [79000, 5],
        "Penelusuran Benang Merah" : [70000, 5],
        "24 Jam Bersama Gaspar" : [68000, 4]
    },
    "fiksi umum" : {
        "Bedebah di Ujung Tanduk" : [90000, 12],
        "Orang-Orang Biasa" : [109000, 9],
        "Kudasai" :[130000, 7],
        "Dompet Ayah Sepatu Ibu" : [88000, 8],
        "A Man Called Otto" : [98000, 3]
    }
}

# Kedua: Manajemen Harga dan Informasi Stok
print(novel)
while True:
     print()
     pilihan = input("Edit informasi/Tambah judul baru/Cek informasi per judul/Tampilkan informasi semua judul yang tersedia? ")
     if pilihan == "Edit informasi":
          while True:
               print()
               tombol = input("Edit: Harga/Stok? ")
               if tombol == "Harga":
                    judul = input("Pilih judul buku yang akan diubah harganya: ")
                    genre = input("Dari genre apa? ")
                    harga = int(input("Masukkan harga terbaru: "))
                    novel[genre][judul][0] = harga
               elif tombol == "Stok":
                    judul = input("Pilih judul buku yang akan mengalami perubahan stok: ")
                    genre = input("Dari kategori apa? ")
                    tombol_baru = input("Restock/Terjual? ")
                    if tombol_baru == "Restock":
                          restock = int(input("Berapa eksemplar yang baru datang? "))
                          novel[genre][judul][1] += restock
                    elif tombol_baru == "Terjual":
                          terjual = int(input("Berapa eksemplar yang sudah terjual? "))
                          novel[genre][judul][1] -= terjual
                          if novel[genre][judul][1] == 0:
                               del novel[genre][judul]
                          else:
                               break
                    else:
                          print("Maaf, seharusnya program ini menggunakan metode input berupa tombol saja untuk membatasi kemungkinan kesalahan input")
                          print("Tapi karena dev program ini belum paham cara membuatnya, program ini baru bisa menyediakan input dalam bentuk teks di terminal saja")
                          print("Mohon ketik input tipe perubahan stok dengan benar dan sama persis sesuai ketentuan yang dicontohkan")
               else:
                    print("Maaf, seharusnya program ini menggunakan metode input berupa tombol saja untuk membatasi kemungkinan kesalahan input")
                    print("Tapi karena dev program ini belum paham cara membuatnya, program ini baru bisa menyediakan input dalam bentuk teks di terminal saja")
                    print("Mohon ketik input pilihan edit dengan benar dan sama persis sesuai ketentuan yang dicontohkan")
               keputusan = input("Lanjutkan/Selesai? ")
               if keputusan == "Lanjutkan":
                    continue
               else:
                    print(novel)
                    break
     elif pilihan == "Tambah judul baru":
          while True:
               judul_baru = input("Ketik judul: ")
               genrenya = input("Apa genre atau kategorinya? ")
               stoknya = int(input("Berapa eksemplar yang didatangkan ke toko? "))
               harganya = int(input("Akan dijual dengan harga berapa? "))
               if genrenya in novel:
                    judul_ini = []
                    judul_ini.append(harganya)
                    judul_ini.append(stoknya)
                    novel[genrenya][judul_baru] = judul_ini
               else:
                    judul_ini = []
                    judul_ini.append(harganya)
                    judul_ini.append(stoknya)
                    novel[genrenya] = {judul_baru : judul_ini}
               tombol_sekian = input("Lanjutkan/Selesai? ")
               if tombol_sekian == "Lanjutkan":
                    continue
               else:
                    print(novel)
                    break
     elif pilihan == "Cek informasi per judul":
          while True:
               judul_dicari = input("Judul apa yang ingin Anda lihat rinciannya? ")
               kategori = input("Dari kategori atau genre apa? ")
               if kategori in novel:
                    if judul_dicari in novel[kategori]:
                         print("Harga per eksemplar di toko ini: Rp", novel[kategori][judul_dicari][0])
                         print("Jumlah stok yang tersedia di toko ini:", novel[kategori][judul_dicari][1], " eksemplar")
                    else:
                         print("Judul tidak ditemukan di database toko ini")
                         print("Coba periksa ejaan judul yang Anda ketik dan pastikan Anda tidak salah mengetik judul")
               else:
                    print("Kategori atau genre yang Anda maksud tidak tersedia di toko ini")
                    print("Mungkin novel yang Anda cari datanya, dikategorikan dalam genre lain")
               tombol_lagi = "Lanjutkan/Selesai? "
               if tombol_lagi == "Lanjutkan":
                    continue
               else:
                    print(novel)
                    break
     elif pilihan == "Tampilkan informasi semua judul yang tersedia":
          print(novel)
          break
     else:
          print("Maaf, seharusnya program ini menggunakan metode input berupa tombol saja untuk membatasi kemungkinan kesalahan input")
          print("Tapi karena dev program ini belum paham cara membuatnya, program ini baru bisa menyediakan input dalam bentuk teks di terminal saja")
          print("Mohon ketik input pilihan pemrosesan data buku dengan benar dan sama persis sesuai ketentuan yang dicontohkan")
          klik = input("Lanjutkan/Selesai? ")
          if klik == "Lanjutkan":
               continue
          else:
               break