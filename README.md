# Netflix Original Films & IMDb Scores Analysis

## Kelompok 8: Data Mining

1. Salwa Khalipa
2. Dillan Gustav Alfaro
3. Melaty Ngesti Lestari
4. Ersya Nur Rahmah
5. Mochamad Aldrin Alfariz
6. Ahmad Ya'isy Ramdhani
7. Monicha Destuty
8. Chelsea Micheal Prayitno

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis dataset Netflix Original Films & IMDb Scores guna memahami karakteristik film Netflix Original berdasarkan bahasa, skor IMDb, dan genre film yang dirilis pada tahun 2020.

Analisis dilakukan menggunakan Python dengan bantuan Pandas untuk pengolahan data serta Matplotlib untuk visualisasi.

## Pertanyaan Analisis

1. Bahasa apa yang paling banyak digunakan dalam film Netflix Original?
2. Film Netflix Original apa saja yang memperoleh skor IMDb minimal 8,0?
3. Genre apa yang paling banyak muncul pada film Netflix Original yang dirilis pada tahun 2020?

## Dataset

Dataset yang digunakan adalah **Netflix Original Films & IMDb Scores**, yang berisi informasi mengenai film Netflix Original.

- Nama dataset: Netflix Original Films & IMDb Scores
- Sumber: Kaggle
- Link: https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores?select=NetflixOriginals.csv
- Format: CSV
- Jumlah data awal: 584 baris dan 6 kolom

Kolom utama yang digunakan meliputi: 

- `Title`: Judul film.
- `Genre`: Genre film.
- `Premiere`: Tanggal perilisan film.
- `Runtime`: Durasi film dalam menit.
- `IMDB Score`: Skor IMDb film.
- `Language`: Bahasa yang digunakan dalam film.

Dataset terdiri dari 584 baris dan 6 kolom.

## Tools dan Library

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Visual Studio Code

## Tahapan Analisis

### 1. Data Understanding

Memahami struktur dataset, jumlah baris dan kolom, tipe data, serta kondisi awal data.

### 2. Data Cleaning dan Exploratory Data Analysis (EDA)

Melakukan pemeriksaan missing value, duplikasi, tipe data, serta mengeksplorasi distribusi bahasa, genre, dan skor IMDb.

### 3. Visualisasi dan Analisis Insight

Membuat tiga visualisasi berdasarkan pertanyaan bisnis yang telah ditentukan.

#### Visualisasi 1: Bahasa Film Terbanyak

Hasil analisis menunjukkan bahwa bahasa Inggris (*English*) merupakan bahasa yang paling banyak digunakan, dengan 401 film dari total 584 film.

**Insight:** Bahasa Inggris mendominasi dataset film Netflix Original yang dianalisis.

**Rekomendasi:** Netflix dapat mempertahankan produksi film berbahasa Inggris sekaligus mengevaluasi peluang pengembangan film dalam bahasa lain untuk menjangkau audiens yang lebih luas.

#### Visualisasi 2: Film dengan Skor IMDb Minimal 8,0

Hasil analisis menemukan 17 film Netflix Original dengan skor IMDb minimal 8,0.

**Insight:** Film-film tersebut memperoleh penilaian IMDb yang tinggi dan dapat menjadi referensi untuk mengevaluasi karakteristik konten.

**Rekomendasi:** Karakteristik film tersebut dapat dipelajari lebih lanjut dan dibandingkan dengan data jumlah penonton untuk mendukung keputusan produksi konten berikutnya.

#### Visualisasi 3: Genre Film Tahun 2020

Genre *Documentary* menjadi genre yang paling banyak muncul pada tahun 2020, dengan 39 film dari total 183 film.

**Insight:** Genre *Documentary* mendominasi jumlah film Netflix Original dalam dataset pada tahun 2020.

**Rekomendasi:** Pengembangan konten dokumenter dapat dievaluasi dengan membandingkan skor IMDb dan data penonton dari genre lainnya.

## Dashboard

Dashboard dikembangkan untuk menyajikan hasil analisis Netflix Original Films & IMDb Scores secara interaktif. Dashboard ini bertujuan memudahkan pengguna dalam memahami distribusi bahasa film, skor IMDb, dan genre film yang dirilis pada tahun 2020.

Dashboard menampilkan visualisasi data dan informasi penting berdasarkan hasil analisis yang telah dilakukan.

## Dokumentasi

Dokumentasi proyek mencakup tahapan analisis data, mulai dari *data understanding*, *data cleaning*, *exploratory data analysis* (EDA), visualisasi dan analisis insight, hingga pembangunan dashboard.

Seluruh proses analisis didokumentasikan dalam Jupyter Notebook, sedangkan ringkasan proyek, pertanyaan analisis, hasil temuan, dan rekomendasi disajikan dalam README.md.

## Kesimpulan

Berdasarkan hasil analisis, bahasa Inggris mendominasi penggunaan bahasa dalam dataset Netflix Original Films. Selain itu, ditemukan 17 film dengan skor IMDb minimal 8,0, sementara genre *Documentary* menjadi genre yang paling banyak muncul pada tahun 2020.

Hasil analisis ini memberikan gambaran mengenai karakteristik film dalam dataset. Namun, jumlah film, bahasa, dan skor IMDb belum cukup untuk menyimpulkan popularitas atau keberhasilan komersial suatu film tanpa data tambahan, seperti jumlah penonton dan pendapatan.

## Cara Menjalankan Proyek
[BELUM DIISI]

## Penutup

Proyek ini menerapkan proses analisis data menggunakan Python, mulai dari memahami dan membersihkan dataset, melakukan eksplorasi data, membuat visualisasi, menyusun insight dan rekomendasi, hingga membangun dashboard serta mendokumentasikan hasil analisis.

Melalui proyek ini, diharapkan karakteristik Netflix Original Films dapat dipahami berdasarkan bahasa, skor IMDb, dan genre film tahun 2020. Hasil analisis dapat menjadi gambaran awal untuk evaluasi konten, dengan mempertimbangkan bahwa data jumlah film dan skor IMDb saja belum cukup untuk menyimpulkan popularitas atau keberhasilan komersial suatu film.
