# Laporan Proyek Machine Learning - Wahyu Krisna Aji

## Project Overview

Perpustakaan Daerah Provinsi Kalimantan Selatan merupakan salah satu
perpustakaan dan pusat penyedia layanan informasi yang ada di Kalimantan
Selatan. Namun. selama ini pengunjung perpustakaan kesulitan dalam mencari
buku yang berkaitan dengan buku yang dipilih sebelumnya dan juga dalam
menemukan alternatif buku lain ketika buku yang diinginkan tersebut telah
dipinjam. dengan adanya rekomendasi atau saran buku-buku lain yang
berhubungan diharapkan membantu dalam mendapatkan buku yang sesuai dan
diinginkan pengunjung perpustakaan. Pada penelitian ini penerapan sistem
rekomendasi menggunakan metode Content Based Filtering dalam
memberikan rekomendasi buku yang bekerja dengan melihat kemiripan item
yang dianalisis dari fitur yang dikandungnya dengan Weighted Tree Similarity.
Berdasarkan hasil pengujian yang telah dilakukan pada 5 skenario pengujian
yang diujikan dihasilkan nilai precision sebesar 88%.

referensi dari proyek overview yang saya buat dapat dilihat dari tautan berikut : [Jurnal Manajemen, Teknik Informatika dan Rekayasa Komputer](https://journal.universitasbumigora.ac.id/index.php/matrik/article/download/617/587/)

## Business Understanding

### Problem Statements

Bagaimana cara merekomendasikan buku yang disukai oleh pengguna dapat direkomendasikan juga ke pengguna lainnya ?

### Goals

Membuat sistem rekomendasi yang akurat berdasarkan ratings dan aktivitas pengguna pada masa lalu

### Solution statements

- Content Based Filtering adalah algoritma yang merekomendasikan item serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit.

Algoritma Content Based Filtering digunakan untuk merekemondesikan buku berdasarkan aktivitas pengguna pada masa lalu.

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah Best Books (10k) Multi-Genre Data. Berikut merupakan link untuk mendownload dataset: [Best Books (10k) Multi-Genre Data](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data).

Variabel-variabel pada dataset Best Books (10k) Multi-Genre Data adalah sebagai berikut:

- Book: merupakan judul buku
- Author: merupakan pengarang buku
- Description: merupakan deskripsi buku
- Genres: merupakan genre buku
- Avg_Rating: mmerupakan rating rata-rata
- Num_Ratings: merupakan rating secara keseluruhan
- URL: merupakan link untuk mendownload buku

Tahapan yang dilakukan adalah exploratory data analysis, yaitu dengan melihat-lihat hubungan antar variabel bersarkan judul buku.

## Data Preparation

Berikut beberapa data preparation yang dilakukan :

- Mengatasi missing value : menyeleksi data apakah data tersebut ada yang kosong atau tidak, jika ada data kosong maka saya akan.menghapusnya
- Membagi data menjadi data training dan validasi : untuk membagi data untuk dilatih dan validasi.
- Konversi data menjadi iist : untuk mengubah data menjadi list
- Membuat dictionary : Untuk membuat dictionary dari data yang ada.
- Menggunakan TfidfVectorizer : untuk melakukan pembobotan.
- Melakukan preprocessing : untuk menghilangkan permasalahan-permasalahan yang dapat mengganggu hasil daripada proses data
- mapping data : untuk memetakan data

## Modeling

- Proses modeling yang dilakukan pada proyek ini adalah dengan membuat algoritma machine learning, yaitu content based filtering. Algoritma content based filtering dibuat dengan apa yang disukai pengguna pada masa lalu.
- Berikut konten buku yang disukai pengguna di masa lalu

![FireShot Capture 002 - Proyek Akhir _ Membuat Model Sistem Rekomendasi ipynb - Colaboratory_ - colab research google com](https://github.com/aliftech/sistem-recomendasi-buku/assets/47414125/f97c9637-8629-4383-ab14-792957577387)

Berdasarkan hasil di atas, terlihat bahwasanya pengguna menyukai buku berjudul "The Emigrants" yang bergenre 'Fiction', 'German Literature', 'Historical Fiction', 'Germany', 'Novels', 'Literature', '20th Century' sehingga akan memunculkan top 5 rekomendasi buku sebagai berikut:

![FireShot Capture 003 - Proyek Akhir _ Membuat Model Sistem Rekomendasi ipynb - Colaboratory_ - colab research google com](https://github.com/aliftech/sistem-recomendasi-buku/assets/47414125/71cfa649-e6e0-489e-91ad-cefa658ed23b)

## Evaluation

Pada bagian ini, saya merekomendasikan sebuah buku berjudul The Emigrants.

![FireShot Capture 002 - Proyek Akhir _ Membuat Model Sistem Rekomendasi ipynb - Colaboratory_ - colab research google com](https://github.com/aliftech/sistem-recomendasi-buku/assets/47414125/f97c9637-8629-4383-ab14-792957577387)

hasil dari Top-N 5 dari buku yang saya rekomendasikan adalah sebagai berikut :

![FireShot Capture 003 - Proyek Akhir _ Membuat Model Sistem Rekomendasi ipynb - Colaboratory_ - colab research google com](https://github.com/aliftech/sistem-recomendasi-buku/assets/47414125/71cfa649-e6e0-489e-91ad-cefa658ed23b)

Dari hasil rekomendasi di atas, diketahui bahwa The Emigrants termasuk ke dalam genre 'Fiction', 'German Literature', 'Historical Fiction', 'Germany', 'Novels', 'Literature', '20th Century'. Dari 5 item yang direkomendasikan, 4 item memiliki genre yang sama (similar). Artinya, precision sistem kita sebesar 4/5 atau 80%.

Teknik Evaluasi di atas adalah dengan menggunakan precission, rumus dari teknik ini adalah :

![dos_819311f78d87da1e0fd8660171fa58e620211012160253 (1)](https://github.com/aliftech/sistem-recomendasi-buku/assets/47414125/93e927b9-2831-412a-960c-7412011e7e06)
