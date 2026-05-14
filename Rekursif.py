"""
Tugas Rekursif - Algoritma Backtracking
=======================================
1. N-Queens (N-Ratu)
2. Knight's Tour (Tur Kuda)
3. Knapsack Problem (Masalah Knapsack)
"""

import sys

# ==============================================================
# SOAL 1: N-QUEENS (N-RATU)
# ==============================================================

def is_safe_queen(board, row, col, n):
    """Cek apakah aman menempatkan ratu di posisi (row, col)."""
    # Cek kolom yang sama di baris sebelumnya
    for i in range(row):
        if board[i] == col:
            return False
    # Cek diagonal kiri atas
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    # Cek diagonal kanan atas
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True


def solve_nqueens(board, row, n, solutions):
    """Rekursif backtracking untuk N-Queens."""
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe_queen(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1  # backtrack


def print_nqueens_board(solution, n):
    """Cetak papan catur dengan posisi ratu."""
    print()
    border = "  +" + ("---+" * n)
    for row in range(n):
        print(border)
        row_str = f"{row} |"
        for col in range(n):
            if solution[row] == col:
                row_str += " Q |"
            else:
                row_str += " . |"
        print(row_str)
    print(border)
    col_labels = "    " + "   ".join(str(c) for c in range(n))
    print(col_labels)


def nqueens_main():
    print("=" * 50)
    print("       SOAL 1: N-QUEENS (N-RATU)")
    print("=" * 50)
    try:
        n = int(input("Masukkan ukuran papan (N): "))
        if n < 1:
            print("Ukuran papan harus >= 1.")
            return
    except ValueError:
        print("Input tidak valid.")
        return

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    if not solutions:
        print(f"\nTidak ada solusi untuk N={n}.")
    else:
        print(f"\nDitemukan {len(solutions)} solusi untuk N={n}.")
        print(f"\nMenunjukkan solusi pertama:")
        print_nqueens_board(solutions[0], n)
        print(f"\nPosisi ratu (baris -> kolom): {solutions[0]}")


# ==============================================================
# SOAL 2: KNIGHT'S TOUR (TUR KUDA)
# ==============================================================

# 8 kemungkinan gerakan kuda
KNIGHT_MOVES = [
    (-2, -1), (-2, +1),
    (-1, -2), (-1, +2),
    (+1, -2), (+1, +2),
    (+2, -1), (+2, +1),
]


def get_degree(board, x, y, n):
    """Warnsdorff: hitung jumlah gerakan valid dari (x, y)."""
    count = 0
    for dx, dy in KNIGHT_MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
            count += 1
    return count


def solve_knights_tour(board, x, y, move_num, n, path):
    """Rekursif backtracking dengan heuristik Warnsdorff."""
    if move_num == n * n:
        return True

    # Urutkan gerakan berdasarkan derajat (heuristik Warnsdorff)
    moves = []
    for dx, dy in KNIGHT_MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
            degree = get_degree(board, nx, ny, n)
            moves.append((degree, nx, ny))
    moves.sort()  # pilih gerakan dengan paling sedikit pilihan berikutnya

    for _, nx, ny in moves:
        board[nx][ny] = move_num
        path.append((nx, ny))
        if solve_knights_tour(board, nx, ny, move_num + 1, n, path):
            return True
        # backtrack
        board[nx][ny] = -1
        path.pop()

    return False


def print_knights_board(board, n):
    """Cetak papan Tur Kuda dengan nomor langkah."""
    print()
    width = len(str(n * n))
    border = "  +" + (("-" * (width + 2)) + "+") * n
    for row in range(n):
        print(border)
        row_str = f"{row} |"
        for col in range(n):
            row_str += f" {board[row][col]:>{width}} |"
        print(row_str)
    print(border)
    col_labels = "    " + "   ".join(f"{c:>{width}}" for c in range(n))
    print(col_labels)


def knights_tour_main():
    print("\n" + "=" * 50)
    print("     SOAL 2: KNIGHT'S TOUR (TUR KUDA)")
    print("=" * 50)
    try:
        n = int(input("Masukkan ukuran papan (N, rekomendasi 5-8): "))
        if n < 5:
            print("Ukuran papan minimal 5 agar solusi lebih mungkin ditemukan.")
            return
        start_x = int(input(f"Masukkan posisi awal baris kuda (0-{n-1}): "))
        start_y = int(input(f"Masukkan posisi awal kolom kuda (0-{n-1}): "))
        if not (0 <= start_x < n and 0 <= start_y < n):
            print("Posisi awal di luar papan.")
            return
    except ValueError:
        print("Input tidak valid.")
        return

    board = [[-1] * n for _ in range(n)]
    board[start_x][start_y] = 0
    path = [(start_x, start_y)]

    print(f"\nMencari solusi Tur Kuda {n}x{n} dari posisi ({start_x}, {start_y})...")

    if solve_knights_tour(board, start_x, start_y, 1, n, path):
        print("Solusi ditemukan!\n")
        print_knights_board(board, n)
        print(f"\nUrutan langkah kuda ({len(path)} langkah):")
        for i, (r, c) in enumerate(path):
            print(f"  Langkah {i+1:>3}: ({r}, {c})", end="")
            if (i + 1) % 4 == 0:
                print()
        print()
    else:
        print("Tidak ada solusi yang ditemukan dari posisi tersebut.")


# ==============================================================
# SOAL 3: KNAPSACK PROBLEM (MASALAH KNAPSACK)
# ==============================================================

def knapsack_recursive(weights, target, index, current_weight, chosen, result):
    """
    Rekursif backtracking untuk Knapsack.
    Mencari subset barang dengan total berat == target.
    """
    if current_weight == target:
        result.append(chosen[:])
        return True  # kembalikan True jika hanya ingin 1 solusi

    if index >= len(weights) or current_weight > target:
        return False

    # Pilih barang ke-index
    chosen.append(weights[index])
    if knapsack_recursive(weights, target, index + 1,
                          current_weight + weights[index], chosen, result):
        return True
    chosen.pop()  # backtrack

    # Tidak pilih barang ke-index
    if knapsack_recursive(weights, target, index + 1,
                          current_weight, chosen, result):
        return True

    return False


def knapsack_all_solutions(weights, target, index, current_weight, chosen, all_results):
    """Cari SEMUA subset yang memenuhi target (tidak melebihi)."""
    if current_weight == target:
        all_results.append(chosen[:])
        return
    if index >= len(weights) or current_weight > target:
        return

    # Pilih barang ke-index
    chosen.append(weights[index])
    knapsack_all_solutions(weights, target, index + 1,
                           current_weight + weights[index], chosen, all_results)
    chosen.pop()  # backtrack

    # Tidak pilih barang ke-index
    knapsack_all_solutions(weights, target, index + 1,
                           current_weight, chosen, all_results)


def knapsack_main():
    print("\n" + "=" * 50)
    print("   SOAL 3: KNAPSACK PROBLEM (MASALAH KNAPSACK)")
    print("=" * 50)

    print("\nContoh default: barang=[2, 5, 6, 9, 12, 14, 20], target=30")
    use_default = input("Gunakan contoh default? (y/n): ").strip().lower()

    if use_default == 'y':
        weights = [2, 5, 6, 9, 12, 14, 20]
        target = 30
    else:
        try:
            raw = input("Masukkan berat barang (pisahkan dengan spasi): ")
            weights = list(map(int, raw.split()))
            target = int(input("Masukkan berat target: "))
            if any(w <= 0 for w in weights) or target <= 0:
                print("Semua berat dan target harus positif.")
                return
        except ValueError:
            print("Input tidak valid.")
            return

    print(f"\nBarang  : {weights}")
    print(f"Target  : {target}")

    # Cari satu solusi cepat
    result_one = []
    knapsack_recursive(weights, target, 0, 0, [], result_one)

    if not result_one:
        print("\nTidak ada kombinasi yang tepat mencapai berat target.")
    else:
        print(f"\n✓ Solusi ditemukan: {result_one[0]}")
        print(f"  Total berat      : {sum(result_one[0])}")

    # Tawarkan semua solusi
    show_all = input("\nTampilkan SEMUA solusi? (y/n): ").strip().lower()
    if show_all == 'y':
        all_results = []
        knapsack_all_solutions(weights, target, 0, 0, [], all_results)
        if all_results:
            print(f"\nTotal solusi ditemukan: {len(all_results)}")
            for i, sol in enumerate(all_results, 1):
                print(f"  Solusi {i:>3}: {sol}  (total={sum(sol)})")
        else:
            print("Tidak ada solusi.")


# ==============================================================
# MENU UTAMA
# ==============================================================

def main():
    print("\n" + "#" * 50)
    print("#   TUGAS REKURSIF - ALGORITMA BACKTRACKING    #")
    print("#" * 50)

    while True:
        print("\nPilih soal yang ingin dijalankan:")
        print("  1. N-Queens (N-Ratu)")
        print("  2. Knight's Tour (Tur Kuda)")
        print("  3. Knapsack Problem (Masalah Knapsack)")
        print("  4. Jalankan Semua")
        print("  0. Keluar")

        pilihan = input("\nPilihan Anda: ").strip()

        if pilihan == '1':
            nqueens_main()
        elif pilihan == '2':
            knights_tour_main()
        elif pilihan == '3':
            knapsack_main()
        elif pilihan == '4':
            nqueens_main()
            knights_tour_main()
            knapsack_main()
        elif pilihan == '0':
            print("Terima kasih! Program selesai.")
            sys.exit(0)
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()