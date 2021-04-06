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
* pyvis 0.1.3.1
* matplotlib 3.4.1

## Setup
Sebelum menggunakan program, Anda harus menginstal library yang disediakan Python yaitu <b>pyvis</b> dan <b>matplotlib</b> untuk mempermudah dalam proses visualisasi graf.
Untuk menginstal kedua library tersebut, ikuti langkah-langkah di bawah ini:
1. Buka Command Prompt di Windows lalu instal library <b>matplotlib</b> dengan menjalankan perintah berikut:<br>
```python -m pip install -U pip```<br>
```python -m pip install -U matplotlib```
<br><br>
2. Instal library <b>pyvis</b> dengan menjalankan perintah berikut di CMD:<br>
```$ pip install pyvis```
<br><br>

Setelah kedua library tersebut berhasil diinstal, Anda dapat menggunakan program dengan mengikuti langkah-langkah berikut:<br>
3. Buka Command Prompt di Windows.<br>
4. Pindahkan direktori ke dalam folder repo tempat program disimpan (folder repo berisi folder bin, doc, src, test, dan file README)<br>
5. Jalankan perintah ```py src/main.py```<br>
6. Masukkan file input graf yang dikehendaki. Tuliskan nama file input sesuai yang ada dalam folder test, contoh: ```input1.txt```<br>
7. Jika nama file input benar, akan muncul jendela baru yang menampilkan visualisasi grafnya. Untuk memasukkan input berikutnya, tutup jendela visualisasi graf terlebih dahulu.<br>
8. Masukkan lokasi awal dan lokasi akhir yang mau dicari lintasan terpendek beserta jaraknya. Format input dapat dilihat pada program.<br>
9. Jika terdapat jalur yang menghubungkan antarlokasi, program akan menampilkan lintasan terpendek beserta jaraknya.<br>
Jika tidak ada jalur, program akan mengeluarkan pesan "Tidak terdapat jalan yang menghubungkan kedua lokasi."<br>
10. Ketik '#' atau tutup Command Prompt bila sudah selesai menggunakan program.

## About Us
* Andrew (13519036)
* Leonardus Brandon Luwianto (13519102)