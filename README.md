# Studi-_Kasus_4_Aura-Rizki-Tariti

Nama: Aura Rizki Tariti
NIM: 2609116032
Kelas: A
Angkatan: 2026

Dalam program kali ini, saya membuat dictionary berupa daftar novel yang dijual di sebuah toko. Dictionary itu masih dibagi lagi dalam sejumlah sub-dictionary untuk mengelompokkan judul novel sesuai genre atau kategorinya. Key dari setiap genre (sub-dictionary) adalah judul novel, dan value dari masing-masing key adalah sebuah list dengan indeks nol yang memuat harga dan indeks satu yang memuat jumlah eksemplar (ketersediaan stok) dari judul tersebut.
Di sini, saya juga menyediakan 3 opsi pemrosesan data pada dictionary tersebut yaitu edit harga dan informasi stok (UPDATE), tambahkan judul atau genre baru (CREATE), dan cek informasi per judul (READ). Saya juga menerapkan konsep DELETE dengan pernyataan kondisi: jika nilai indeks satu (stok) dari sebuah key (judul) sama dengan 0, maka key (judul) tersebut dihapus dari dictionary karena berarti stoknya sudah habis dan tidak dijual lagi, kecuali jika pengguna kembali menambahkan judul tersebut lewat opsi tambah judul baru.

Yang pertama: opsi UPDATE dengan edit informasi dari segi stok dan harga. Pada tampilan akhir dari semua data di dalam gambar ini, terlihat bahwa ada novel dengan data stok dan atau harga yang sudah berubah.
<img width="1851" height="582" alt="Screenshot 2026-09-15 210149" src="https://github.com/user-attachments/assets/c71297dd-d83d-4dad-8b21-e384e5381c93" />

Yang kedua: opsi CREATE dengan menambah judul baru, baik dari genre yang sudah ada (dalam hal ini: No Tell to Hearts dari kategori teenlit lokal) maupun yang belum ada (misalnya Kilau Gadang di Dunia Imaji yang bergenre fantasi). Jika genre dari novel yang baru ditambahkan belum ada, maka judul tersebut akan dijadikan key dari sub-dictionary baru.
<img width="1720" height="283" alt="Screenshot 2026-09-15 214747" src="https://github.com/user-attachments/assets/a6094fc0-aae6-4c14-b2ef-fe9c97e5deea" />

Yang ketiga: opsi READ dengan menampilkan data stok dan harga dari salah satu judul secara lebih rapi. Di sini saya juga menunjukkan bahwa program akan mengeluarkan output dengan bahasa sesopan mungkin jika input (judul yang diketik pengguna) ternyata salah atau tidak ada dalam dictionary.
<img width="1706" height="341" alt="Screenshot 2026-09-15 215813" src="https://github.com/user-attachments/assets/1b818d3b-220a-4dfe-bc34-d09051904470" />

Mekanisme REMOVE: dalam gambar ini, salah satu key (novel) dihapus dari dictionary yang ditampilkan di akhir karena stoknya habis (nol).
<img width="1698" height="471" alt="Screenshot 2026-09-15 223555" src="https://github.com/user-attachments/assets/5d58144e-0765-4573-aa4b-3ccd22573cc4" />

Terakhir, ini yang terjadi jika pengguna memasukkan input yang tidak memungkinkan untuk dijalankan program. Ini kata-katanya saya copas dari poin ketiga tapi dengan sedikit perubahan.
<img width="1142" height="95" alt="Screenshot 2026-09-15 220624" src="https://github.com/user-attachments/assets/3bb1b724-2984-4e2a-bdb2-b51b1de2149e" />

