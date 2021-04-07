# Tugas Kecil 3 IF2211 - Strategi Algoritme:<br> Implementasi Algoritme A* untuk Menentukan Lintasan Terpendek
> Algoritma A* (atau A star) dapat digunakan untuk menentukan lintasan terpendek dari suatu titik ke titik lain. Pada tugas kecil 3 ini, anda diminta menentukan lintasan terpendek berdasarakan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan di peta dibentuk graf. Simpul menyatakan persilangan jalan atau ujung jalan. Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul. Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara lainnya yang disediakan oleh Google Map. 
Langkah pertama di dalam program ini adalah membuat graf yang merepresentasikan peta (di area tertentu, misalnya di sekitar kampus ITB). Sisi diperoleh dari jalan antar dua simpul dan bobot sisi adalah jarak Euclidean. Berdasarkan graf yang dibentuk, lalu program A* menerima input simpul asal dan simpul tujuan, lalu menentukan lintasan terpendek antara keduanya. Lintasan terpendek dapat ditampilkan pada peta/graf. Nilai heuristik yang dipakai adalah jarak garis lurus dari suatu titik ke tujuan.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [About Us](#about-us)

## General Info
Program ini dibuat dalam rangka memenuhi tugas kecil ke-3 mata kuliah IF2211 - Strategi Algoritme di Prodi Sarjana Teknik Informatika Institut Teknologi Bandung.

## Technologies
* Python 3.9.0
* matplotlib 3.4.1

## Setup
Sebelum menggunakan program, Anda harus menginstal library yang disediakan Python yaitu <b>matplotlib</b> untuk mempermudah dalam proses visualisasi graf.
Untuk menginstal matplotlib, ikuti langkah-langkah di bawah ini:
1. Buka Command Prompt di Windows lalu instal library <b>matplotlib</b> dengan menjalankan perintah berikut:<br>
```python -m pip install -U pip```<br>
```python -m pip install -U matplotlib```<br>
Setelah matplotlib berhasil di-install, Anda dapat menggunakan program dengan mengikuti langkah-langkah berikut:
1. Buka Command Prompt di Windows.
2. Clone repository ini ke direktori yang dikehendaki.
3. Pindahkan direktori ke dalam folder repo tempat program disimpan (folder repo berisi folder doc, src, test, dan file README)
4. Jalankan perintah ```py src/main.py```
5. Masukkan file input graf yang dikehendaki. Tuliskan nama file input sesuai yang ada dalam folder test, contoh: ```input1.txt```
6. Jika nama file input benar, akan muncul jendela baru yang menampilkan visualisasi grafnya. Untuk memasukkan input berikutnya, tutup jendela visualisasi graf terlebih dahulu.
7. Masukkan lokasi awal dan lokasi akhir yang mau dicari lintasan terpendek beserta jaraknya. Format input dapat dilihat pada program.
8. Jika terdapat jalur yang menghubungkan antarlokasi, program akan menampilkan lintasan terpendek beserta jaraknya.
Jika tidak ada jalur, program akan mengeluarkan pesan "Tidak terdapat jalan yang menghubungkan kedua lokasi."
8. Ketik '#' atau tutup Command Prompt bila sudah selesai menggunakan program.

## Misc
Jika anda ingin menggunakan file txt sendiri, berikut format file txt yang harus dibuat:<br>
```
<jumlah simpul>
<nama setiap simpul dengan format: x y nama simpul>
<matriks adjacency yang merepresentasikan keterhubungan antarsimpul>
```
Contoh:
```
3
0 0 Koor1
0 1 Koor2
1 0 Koor3
0 1 0
1 0 1
0 1 0
```
## About Us
* Andrew (13519036)
* Leonardus Brandon Luwianto (13519102)
