# dss-wisata-kawa
# LAPORAN PROJECT STRUKTUR DATA

# IMPLEMENTASI GRAPH MENJADI DSS

## DSS Wisata Kampung Adat Kawa Desa Labolewa Menggunakan Algoritma Dijkstra



# Disusun Oleh

Nama : Maria indriani lelu_2501010335
       
Ni putu indahning sasmita_25010104


Kelas/Prodi : D/teknik informatika

Mata Kuliah : Struktur Data



# BAB 1

# PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi menyebabkan kebutuhan akan sistem pendukung keputusan semakin meningkat. Decision Support System (DSS) digunakan untuk membantu pengguna dalam mengambil keputusan berdasarkan data dan analisis tertentu.

Salah satu penerapan DSS dapat dilakukan pada bidang pariwisata, khususnya dalam menentukan rute wisata terbaik. Wisatawan sering mengalami kesulitan menentukan jalur perjalanan yang efisien karena banyaknya lokasi wisata dan perbedaan jarak antar lokasi.

Desa Labolewa memiliki beberapa lokasi wisata seperti Kampung Adat Kawa, Pantai Labolewa, Bukit Labolewa, Homestay, dan fasilitas umum lainnya yang saling terhubung.

Permasalahan tersebut dapat dimodelkan menggunakan struktur data graph karena graph mampu merepresentasikan hubungan antar lokasi dalam bentuk node dan edge.

Pada project ini digunakan algoritma Dijkstra untuk mencari jalur terpendek berdasarkan bobot jarak sehingga dapat membantu pengguna menentukan rute wisata terbaik.



## 1.2 Rumusan Masalah

1. Bagaimana cara merepresentasikan lokasi wisata menggunakan graph?
2. Bagaimana cara menentukan jalur wisata terbaik?
3. Bagaimana implementasi algoritma Dijkstra pada DSS?
4. Bagaimana visualisasi graph membantu pengambilan keputusan?



## 1.3 Tujuan

1. Mengimplementasikan struktur data graph pada DSS.
2. Membuat sistem rekomendasi wisata berbasis graph.
3. Mengimplementasikan algoritma Dijkstra untuk pencarian rute terbaik.
4. Membantu pengguna menentukan jalur wisata tercepat.
5. Menampilkan visualisasi graph secara interaktif.



## 1.4 Manfaat

1. Membantu wisatawan menentukan rute wisata terbaik.
2. Mempermudah analisis hubungan antar lokasi wisata.
3. Menjadi media pembelajaran implementasi graph.
4. Menunjukkan penerapan nyata algoritma graph.



# BAB 2

# DASAR TEORI

## 2.1 Struktur Data Graph

Graph merupakan struktur data yang terdiri dari kumpulan vertex (node) dan edge (sisi) yang digunakan untuk merepresentasikan hubungan antar objek.

Dalam project ini:

* Node digunakan untuk merepresentasikan lokasi wisata.
* Edge digunakan untuk merepresentasikan hubungan antar lokasi.
* Bobot digunakan untuk merepresentasikan jarak tempuh.

Jenis graph yang digunakan:

### 1. Weighted Graph

Graph yang memiliki bobot pada setiap edge.

### 2. Undirected Graph

Graph yang hubungan antar node dapat dilalui dua arah.

### 3. Adjacency List

Representasi graph menggunakan daftar tetangga setiap node.



## 2.2 Decision Support System (DSS)

Decision Support System merupakan sistem yang digunakan untuk membantu proses pengambilan keputusan berdasarkan data dan analisis tertentu.

Pada project ini DSS digunakan untuk membantu pengguna menentukan rute wisata terbaik berdasarkan jarak tempuh.



## 2.3 Algoritma Dijkstra

Algoritma Dijkstra merupakan algoritma graph yang digunakan untuk mencari jalur terpendek dari satu node ke node lainnya pada weighted graph.

Langkah kerja algoritma:

1. Menentukan node awal.
2. Menghitung jarak sementara ke node tetangga.
3. Memilih node dengan jarak terkecil.
4. Mengulangi proses hingga tujuan ditemukan.

Kompleksitas algoritma:

O((V + E) log V)

Keterangan:

* V = jumlah vertex
* E = jumlah edge

---

# BAB 3

# ANALISIS DAN PERANCANGAN

## 3.1 Analisis Masalah

Pengguna membutuhkan sistem yang dapat:

* menentukan rute tercepat,
* menghitung total jarak,
* memberikan rekomendasi jalur wisata.

Dengan menggunakan graph, hubungan antar lokasi wisata dapat direpresentasikan secara jelas.

---

## 3.2 Desain Graph

### Node

1. Kampung Adat Kawa
2. Pantai Labolewa
3. Bukit Labolewa
4. Pasar Desa
5. Pelabuhan
6. Homestay
7. Restoran Lokal

---

### Edge dan Bobot

| Dari              | Ke              | Jarak |
| ----------------- | --------------- | ----- |
| Kampung Adat Kawa | Pasar Desa      | 3 km  |
| Kampung Adat Kawa | Bukit Labolewa  | 4 km  |
| Pasar Desa        | Pantai Labolewa | 5 km  |
| Pasar Desa        | Pelabuhan       | 2 km  |
| Pantai Labolewa   | Homestay        | 3 km  |
| Pelabuhan         | Homestay        | 4 km  |
| Homestay          | Restoran Lokal  | 1 km  |

---

## 3.3 Flowchart Sistem

1. User memilih lokasi awal.
2. User memilih tujuan wisata.
3. Sistem membaca graph.
4. Algoritma Dijkstra dijalankan.
5. Sistem menghitung jalur terbaik.
6. Hasil rekomendasi ditampilkan.

---

## 3.4 Use Case

### Aktor

User

### Aktivitas

* memilih lokasi awal,
* memilih tujuan,
* menjalankan pencarian,
* melihat hasil rekomendasi.

---

# BAB 4

# IMPLEMENTASI SISTEM

## 4.1 Teknologi yang Digunakan

1. Python
2. Streamlit
3. NetworkX
4. Matplotlib

---

## 4.2 Implementasi Graph

Graph direpresentasikan menggunakan adjacency list.

Contoh implementasi:

graph = {
"Kampung Adat Kawa": {
"Pasar Desa": 3,
"Bukit Labolewa": 4
}
}

---

## 4.3 Implementasi Algoritma Dijkstra

Algoritma Dijkstra digunakan untuk mencari jalur dengan total bobot terkecil.

Contoh implementasi:

cost, path = dijkstra(graph, start, goal)

---

## 4.4 Tampilan Sistem

Sistem memiliki fitur:

* memilih lokasi awal,
* memilih tujuan wisata,
* menampilkan rute terbaik,
* menampilkan total jarak,
* visualisasi graph.

---

# BAB 5

# PENGUJIAN DAN ANALISIS

## 5.1 Skenario Pengujian

Input:

Lokasi awal : Pelabuhan
Lokasi tujuan : Kampung Adat Kawa

---

## 5.2 Hasil Pengujian

Hasil sistem:

Pelabuhan → Pasar Desa → Kampung Adat Kawa

Total jarak : 5 km

---

## 5.3 Analisis Hasil

Sistem berhasil menentukan jalur terpendek berdasarkan total bobot terkecil.

Algoritma Dijkstra mampu menghitung rute terbaik dengan efisien pada weighted graph.

Visualisasi graph membantu pengguna memahami hubungan antar lokasi wisata.

---

## 5.4 Kelebihan Sistem

1. Mudah digunakan.
2. Visualisasi graph interaktif.
3. Pencarian jalur cepat.
4. Implementasi graph nyata.

---

## 5.5 Kekurangan Sistem

1. Data masih statis.
2. Belum menggunakan data real-time.
3. Belum terintegrasi Google Maps API.

---

# BAB 6

# KESIMPULAN DAN SARAN

## 6.1 Kesimpulan

Project ini berhasil mengimplementasikan struktur data graph pada Decision Support System rekomendasi wisata Kampung Adat Kawa di Desa Labolewa.

Graph digunakan untuk merepresentasikan hubungan antar lokasi wisata, sedangkan algoritma Dijkstra digunakan untuk menentukan jalur terbaik berdasarkan total bobot terkecil.

Hasil implementasi menunjukkan bahwa graph dapat digunakan sebagai dasar pengambilan keputusan pada sistem nyata.

---

## 6.2 Saran

Sistem dapat dikembangkan menjadi:

1. Sistem real-time.
2. Integrasi Google Maps API.
3. AI recommendation.
4. Mobile application.
5. Multi-user system.

---

# DAFTAR PUSTAKA

1. Cormen, T. H. Introduction to Algorithms.
2. Pressman, R. S. Software Engineering.
3. Sedgewick, Robert. Algorithms.
4. Dokumentasi Python.
5. Dokumentasi Streamlit.

---

# PENUTUP

“Graph bukan hanya teori dalam struktur data, tetapi dapat digunakan sebagai dasar pengambilan keputusan pada sistem nyata melalui Decision Support System berbasis algoritma graph.”

