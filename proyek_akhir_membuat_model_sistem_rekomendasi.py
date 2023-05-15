# -*- coding: utf-8 -*-
"""Proyek Akhir : Membuat Model Sistem Rekomendasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u824J6Dkx04BOZFMr8ZmfOQguHW974D3

Nama : Wahyu Krisna Aji

Datasets : Best Books (10k) Multi-Genre Data

Source : Kaggle

Link : [Best Books (10k) Multi-Genre Data](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data)

## **Project Overview**

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

# **Data Understanding**
"""

# Install opendataset
!pip install opendatasets

# import all needed libraries
import pandas as pd
import opendatasets as od

od.download('https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data')

books = pd.read_csv('/content/best-books-10k-multi-genre-data/goodreads_data.csv')
books

print('Books data numbers : ', len(books.Book.unique()))

# Drop Unnamed: 0	column
books = books.drop('Unnamed: 0', axis=1)
books

"""## **Univariate Exploratory Data Analysis**

Variabel-variabel pada dataset Best Books (10k) Multi-Genre Data adalah sebagai berikut :

- Book: merupakan judul buku
- Author:  merupakan pengarang buku
- Description: merupakan deskripsi buku
- Genres: merupakan genre buku
- Avg_Rating: mmerupakan rating rata-rata
- Num_Ratings: merupakan rating secara keseluruhan
- URL: merupakan link untuk mendownload buku

### **Book Variable**

Mari kita eksplorasi variabel book yang merupakan judul buku dalam dataset
"""

books.Book.info()

"""### **Author Variable**

Eksplorasi variabel author, merupakan variabel yang menyimpan informasi mengenai nama-nama penulis buku
"""

books.Author.info()

"""### **Description Variable**

Eksplorasi variabel description, yang menyimpan deskripsi/sinopsis dari masing-masing buku.
"""

books.Description.info()

"""### **Genres Variable**

Explorasi variabel genres - merupakan variabel yang berisi data genre dari masing-masing buku

"""

books.Genres.info()

"""### **Avg_Rating Variable**

Eksplorasi variabel avg_rating - merupakan rating rata-rata dari masing-masing buku

"""

books.Avg_Rating.info()

"""### **Num_Ratings Variable**

Eksplorasi variabel num_rating - merupakan rating keseluruhan dari masing-masing buku

"""

books.Num_Ratings.info()

"""### **URL Variable**

Eksplorasi variabel url - merupakan link tempat untuk mengunduh buku
"""

books.URL.info()

"""## **Data Preprocessing**

Dikarenakan data telah rapi, maka kita akan lanjut ke data preparation

## **Data Preparation**

### **Mengatasi Missing Value**

Mencari apakah di dalam data yang kita miliki terdapat missing value
"""

books.isnull().sum()

"""Berdasarkan hasil di atas, ternyata terdapat kolom dengan missing value, yaitu pada variabel Description sebanyak 77 buah. Jika demikian, kita akan menghapus semua data yang kosong tersebut."""

books = books.dropna()

books.isnull().sum()

"""#### **Membersihkan Data Genres**"""

fix_books['Genres'] = fix_books['Genres'].map(lambda x: x.lstrip('[').rstrip(']'))
fix_books['Genres'] = fix_books['Genres'].str.replace("'", "")
fix_books.head()

fix_books = books
fix_books

"""#### **Mengecek jumlah fix_books**

"""

len(fix_books.Book.unique())

"""### **Mengubah Data book, author, dan genres menjadi list**"""

book = fix_books['Book'].tolist()
author = fix_books['Author'].tolist()
genres = fix_books['Genres'].tolist()

print(len(book))
print(len(author))
print(len(genres))

# Membuat dictionary untuk data ‘book’, ‘author’, dan ‘genres’
new_books = pd.DataFrame({
    'title': book,
    'author': author,
    'genre': genres
})
new_books

"""### **Modelling**

Pada tahap modelling, saya membuat sebuah model machine learning dengan menggunakan algoritma **Content Based Filtering**

### **Content Based Filtering**
"""

from sklearn.feature_extraction.text import TfidfVectorizer
 
# Inisialisasi TfidfVectorizer
vector = TfidfVectorizer()
 
# Melakukan perhitungan idf pada data genre
vector.fit(new_books['genre']) 
 
# Mapping array dari fitur index integer ke fitur nama
vector.get_feature_names_out()

matrix = vector.fit_transform(new_books['genre']) 
matrix.shape

matrix.todense()

pd.DataFrame(
    matrix.todense(), 
    columns=vector.get_feature_names_out(),
    index=new_books.title
).sample(22, axis=1).sample(10, axis=0)

from sklearn.metrics.pairwise import cosine_similarity

kemiripan = cosine_similarity(matrix) 
kemiripan

data_kemiripan = pd.DataFrame(kemiripan, index=new_books['title'], columns=new_books['title'])
print('Shape:', data_kemiripan.shape)
 
data_kemiripan.sample(5, axis=1).sample(10, axis=0)

"""#### **Mendapatkan Rekomendasi**"""

def books_recommendations(title, kemiripan=data_kemiripan, items=new_books[['title', 'genre']], k=5):
   
 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = kemiripan.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = kemiripan.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_movie agar nama movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

new_books[new_books.title.eq('The Emigrants')]

books_recommendations('The Emigrants')