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

Berikut informasi pada dataset:

1. Dataset memiliki format csv(Comma Separated Value).
2. Dataset memiliki 10000 sampel dengan 8 fitur.
3. Dataset memiliki 6 fitur bertipe objek dan 1 fitur bertipe float64 dan 1 fitur bertipe int.
4. Terdapat missing value pada fitur Description sebanyak 77 buah.

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

---

Berikut beberapa data preparation yang dilakukan :

### **Mengatasi Missing Value**

Pada fitur description terdapat sebanyak 77 missing value. Supaya tidak menimbulkan kesalahan, maka kita akan menghapus seluruh data kosong tersebut.

### **Membersihkan Data Genres**

Karena pada fitur Genres terdapat noise pada konten (terbungkus pada kurung kotak seperti pada tabel), maka kita harus membersihkan kurung kotak tersebut

| Book                                     | Author       | Description                                       | Genres                                              |
| ---------------------------------------- | ------------ | ------------------------------------------------- | --------------------------------------------------- |
| To Kill a Mockingbird                    | Harper Lee   | The unforgettable novel of a childhood in a sl... | ['Classics', 'Fiction', 'Historical Fiction', ... ] |
| Harry Potter and the Philosopher’s Stone | J.K. Rowling | Harry Potter thinks he is an ordinary boy - un... | ['Fantasy', 'Fiction', 'Young Adult', 'Magic',... ] |
| Pride and Prejudice                      | Jane Austen  | Since its immediate success in 1813, Pride and... | ['Classics', 'Fiction', 'Romance', 'Historical...]  |

Genres yang telah dibersihkan akan terlihat seperti berikut.

| Book                                     | Author       | Description                                       | Genres                                            |
| ---------------------------------------- | ------------ | ------------------------------------------------- | ------------------------------------------------- |
| To Kill a Mockingbird                    | Harper Lee   | The unforgettable novel of a childhood in a sl... | Classics, Fiction, Historical Fiction, School,... |
| Harry Potter and the Philosopher’s Stone | J.K. Rowling | Harry Potter thinks he is an ordinary boy - un... | Fantasy, Fiction, Young Adult, Magic, Children... |
| Pride and Prejudice                      | Jane Austen  | Since its immediate success in 1813, Pride and... | Classics, Fiction, Romance, Historical Fiction... |

### **Mengecek Jumlah Buku**

Setelah kita membersihkan data dari missing value dengan cara menghapus data yang kosong, maka jumlah buku akan berkurang dari jumlah awalnya. Jumlah awal buku pada data adalah 10000 buah, akan tetapi, setelah dilakukan pembersihan menjadi 9795 buah.

### **Mengubah Data book, author, dan genres menjadi list**

kita perlu melakukan konversi data series menjadi list. Dalam hal ini, kita menggunakan fungsi tolist() dari library numpy. Kemudian list data tersebut akan kita membuat dictionary untuk menentukan pasangan key-value pada data book, author, dan genres yang telah kita siapkan sebelumnya.

## Modeling

---

Proses modeling yang dilakukan pada proyek ini adalah dengan membuat algoritma machine learning, yaitu content based filtering. Algoritma content based filtering dibuat dengan apa yang disukai pengguna pada masa lalu.

### **Content-Based Filtering**

Content based filtering menggunakan informasi tentang beberapa item/data untuk merekomendasikan kepada pengguna sebagai referensi mengenai informasi yang digunakan sebelumnya. Tujuan dari content based filtering adalah untuk memprediksi persamaan sejumlah informasi yang didapat dari pengguna. Sebagai contoh, seorang pembaca sedang membaca buku tentang saham. Platform baca buku online secara sistem akan merekomendasikan si pengguna untuk membaca buku lain yang berhubungan dengan saham.

Dalam pembuatannya, content based filtering menggunakan konsep perhitungan vectoru, TF-IDF, dan Cosine Similarity yang intinya dikonversikan dari data/teks menjadi berbentuk vector.

![](https://miro.medium.com/max/1400/1*BcXAhvp6xChQ85B7yYbkXA.png)

## Evaluation

---

Evaluasi dari sistem rekomendasi pada proyek ini dengan pendekatan content based filtering dengan menggunakan metrik evaluasi precission.

Precision adalah perbandingan antara True Positive (TP) dengan banyaknya data yang diprediksi positif. Atau juga bisa ditulis secara matematis sebagai berikut :

![rumus precision](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:819311f78d87da1e0fd8660171fa58e620211012160253.png)

Pada bagian ini, saya merekomendasikan sebuah buku berjudul The Emigrants.

| title         | author      | genre                                          |
| ------------- | ----------- | ---------------------------------------------- |
| The Emigrants | W.G. Sebald | Fiction, German Literature, Historical Fiction |

hasil dari Top-N 5 dari buku yang saya rekomendasikan adalah sebagai berikut :

| title                   | genre                                          |
| ----------------------- | ---------------------------------------------- |
| Atemschaukel            | Fiction, Historical Fiction, German Literature |
| Crabwalk                | Fiction, German Literature, Historical Fiction |
| Chess Story             | Fiction, Classics, German Literature           |
| Heaven Has No Favorites | Classics, Fiction, German Literature           |
| The Clown               | Fiction, German Literature, Classics           |

Dari hasil rekomendasi di atas, diketahui bahwa The Emigrants termasuk ke dalam genre Fiction, German Literature, Historical Fiction. Dari 5 item yang direkomendasikan, 2 item memiliki genre yang sama (similar). Artinya, precision sistem kita sebesar 2/5 atau 40%.
