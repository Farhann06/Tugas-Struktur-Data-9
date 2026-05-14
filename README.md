# Tugas Rekursif — Algoritma Backtracking

Program Python yang mengimplementasikan tiga algoritma klasik menggunakan **rekursi** dan **backtracking**.

---

## 📋 Daftar Isi

- [Deskripsi Program](#deskripsi-program)
- [Soal 1 — N-Queens](#soal-1--n-queens-n-ratu)
- [Soal 2 — Knight's Tour](#soal-2--knights-tour-tur-kuda)
- [Soal 3 — Knapsack Problem](#soal-3--knapsack-problem-masalah-knapsack)
- [Cara Menjalankan](#cara-menjalankan)
- [Contoh Output](#contoh-output)
- [Struktur File](#struktur-file)
- [Teknologi](#teknologi)

---

## Deskripsi Program

File `tugas_rekursif.py` berisi implementasi tiga soal algoritma rekursif dalam satu program dengan menu interaktif. Pengguna dapat memilih soal yang ingin dijalankan, memasukkan input, dan melihat hasilnya langsung di terminal.

---

## Soal 1 — N-Queens (N-Ratu)

### Deskripsi

Menempatkan **N buah ratu** di papan catur berukuran N×N sehingga tidak ada dua ratu yang saling menyerang (tidak sebaris, sekolom, maupun sediagonal).

### Algoritma

- **Metode:** Backtracking rekursif baris per baris
- **Fungsi utama:** `solve_nqueens(board, row, n, solutions)`
- **Pengecekan keamanan** `is_safe_queen()` memeriksa:
  - Kolom yang sama di baris sebelumnya
  - Diagonal kiri atas
  - Diagonal kanan atas

### Cara Kerja

```
Tempatkan ratu di baris ke-row, kolom 0..N-1
  └─ Jika posisi AMAN → lanjut ke baris berikutnya (rekursi)
  └─ Jika posisi TIDAK AMAN → coba kolom berikutnya (backtrack)
  └─ Jika row == N → solusi ditemukan, simpan
```

### Input / Output

| Parameter | Keterangan |
|-----------|-----------|
| Input | Ukuran papan `N` (integer ≥ 1) |
| Output | Jumlah solusi + tampilan papan solusi pertama |

---

## Soal 2 — Knight's Tour (Tur Kuda)

### Deskripsi

Menemukan urutan langkah kuda catur sehingga **mengunjungi setiap petak tepat satu kali** di papan N×N, dimulai dari posisi yang ditentukan pengguna.

### Algoritma

- **Metode:** Backtracking rekursif + Heuristik **Warnsdorff**
- **Fungsi utama:** `solve_knights_tour(board, x, y, move_num, n, path)`
- **Heuristik Warnsdorff:** Pada setiap langkah, pilih petak berikutnya yang memiliki **jumlah gerakan valid paling sedikit** (derajat terkecil). Strategi ini sangat mempercepat pencarian solusi.

### 8 Gerakan Legal Kuda

```
  .  .  .  .  .
  .  8  .  1  .
  7  .  .  .  2
  .  .  K  .  .
  6  .  .  .  3
  .  5  .  4  .
```

### Cara Kerja

```
Dari posisi (x, y) pada langkah ke-move_num:
  └─ Urutkan 8 kemungkinan gerakan berdasarkan derajat (Warnsdorff)
  └─ Untuk setiap gerakan valid (dalam papan & belum dikunjungi):
       ├─ Tandai papan[nx][ny] = move_num
       ├─ Rekursi ke (nx, ny) dengan move_num + 1
       └─ Jika gagal → hapus tanda (backtrack)
  └─ Jika move_num == N² → semua petak dikunjungi, solusi ditemukan!
```

### Input / Output

| Parameter | Keterangan |
|-----------|-----------|
| Input | Ukuran papan `N` (≥ 5) dan posisi awal `(baris, kolom)` |
| Output | Papan berisi nomor urutan langkah + daftar langkah |

> **Catatan:** Disarankan ukuran papan minimal 5×5. Untuk papan 2×2 atau 3×3, tur kuda tidak mungkin diselesaikan.

---

## Soal 3 — Knapsack Problem (Masalah Knapsack)

### Deskripsi

Diberikan sekumpulan barang dengan berat berbeda-beda, cari kombinasi barang yang **totalnya tepat sama dengan berat target** tanpa melebihinya.

### Algoritma

- **Metode:** Backtracking rekursif (subset sum / decision tree)
- **Fungsi utama:** `knapsack_recursive()` — mencari **satu** solusi pertama
- **Fungsi tambahan:** `knapsack_all_solutions()` — mencari **semua** solusi

### Cara Kerja

```
Untuk setiap barang pada indeks ke-i:
  ├─ PILIH barang ke-i → tambah ke berat saat ini → rekursi ke i+1
  │    └─ Jika berat == target → solusi ditemukan!
  │    └─ Jika berat > target atau i habis → backtrack
  └─ TIDAK PILIH barang ke-i → rekursi ke i+1 (tetap backtrack jika gagal)
```

### Contoh Kasus

```
Barang  : [2, 5, 6, 9, 12, 14, 20]
Target  : 30
Solusi  : [2, 5, 9, 14]  →  2 + 5 + 9 + 14 = 30 ✓
```

### Input / Output

| Parameter | Keterangan |
|-----------|-----------|
| Input | Daftar berat barang (dipisah spasi) + berat target |
| Output | Satu solusi pertama (atau semua solusi jika diminta) |

---

## Cara Menjalankan

### Prasyarat

- Python 3.x (tidak memerlukan library tambahan)

### Perintah

```bash
python tugas_rekursif.py
```

### Menu Interaktif

```
##################################################
#   TUGAS REKURSIF - ALGORITMA BACKTRACKING    #
##################################################

Pilih soal yang ingin dijalankan:
  1. N-Queens (N-Ratu)
  2. Knight's Tour (Tur Kuda)
  3. Knapsack Problem (Masalah Knapsack)
  4. Jalankan Semua
  0. Keluar
```

---

## Contoh Output

### N-Queens (N=6)

```
N=6: Ditemukan 4 solusi

  +---+---+---+---+---+---+
0 | . | Q | . | . | . | . |
  +---+---+---+---+---+---+
1 | . | . | . | Q | . | . |
  +---+---+---+---+---+---+
2 | . | . | . | . | . | Q |
  +---+---+---+---+---+---+
3 | Q | . | . | . | . | . |
  +---+---+---+---+---+---+
4 | . | . | Q | . | . | . |
  +---+---+---+---+---+---+
5 | . | . | . | . | Q | . |
  +---+---+---+---+---+---+
    0   1   2   3   4   5
```

### Knight's Tour (5×5, mulai dari (0,0))

```
  +----+----+----+----+----+
0 |  0 | 19 |  8 | 13 |  2 |
  +----+----+----+----+----+
1 |  9 | 14 |  1 | 18 | 23 |
  +----+----+----+----+----+
2 | 20 |  7 | 22 |  3 | 12 |
  +----+----+----+----+----+
3 | 15 | 10 |  5 | 24 | 17 |
  +----+----+----+----+----+
4 |  6 | 21 | 16 | 11 |  4 |
  +----+----+----+----+----+
```

### Knapsack (target=30)

```
Barang  : [2, 5, 6, 9, 12, 14, 20]
Target  : 30

✓ Solusi ditemukan: [2, 5, 9, 14]
  Total berat      : 30

Semua solusi (1 total):
  Solusi   1: [2, 5, 9, 14]  (total=30)
```

---

## Struktur File

```
tugas_rekursif/
│
├── tugas_rekursif.py   ← Program utama (semua soal dalam satu file)
└── README.md           ← Dokumentasi ini
```

---

## Teknologi

| Item | Detail |
|------|--------|
| Bahasa | Python 3.x |
| Library | Hanya `sys` (built-in) |
| Paradigma | Rekursi + Backtracking |
| Platform | Windows / macOS / Linux |

---

## Perbandingan Algoritma

| Soal | Kompleksitas Waktu | Teknik Optimasi |
|------|-------------------|-----------------|
| N-Queens | O(N!) worst case | Pruning diagonal & kolom |
| Knight's Tour | O(8^(N²)) worst case | Heuristik Warnsdorff |
| Knapsack | O(2^n) worst case | Early termination (berat > target) |

---

*Dibuat untuk memenuhi Tugas Algoritma Rekursif.*
