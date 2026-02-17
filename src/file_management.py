from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = BASE_DIR / "test"

def parse_file(filename):
    path = TEST_DIR / filename
    if not path.exists():
        raise FileNotFoundError("File tidak ditemukan. Pastikan file terdapat dalam folder test.")
    if path.suffix != ".txt":
        raise ValueError("Format file harus .txt")
    lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    board = [list(line) for line in lines]
    size = len(board)
    if size == 0:
        raise ValueError("File kosong.")
    if any(len(row) != size for row in board):
        raise ValueError("File harus berdimensi N x N.")
    if size > 26:
        raise ValueError("Karena menggunakan huruf sebagai warna, maka ukuran maksimum yang diperbolehkan adalah 26 x 26.")
    colors = sorted({char for row in board for char in row}) #ini bakalan dipake buat validasi nanti apakah masing-masing warna udah punya queen atau belum
    if len(colors) != size:
        raise ValueError("Jumlah warna harus sama dengan ukuran papan atau jumlah baris ataupun kolom.")
    return board, colors

def save_solution_to_file(filename, board, positions):
    path = TEST_DIR / filename
    temp = [row[:] for row in board]
    for row, col in enumerate(positions):
        temp[row][col] = '#'
    with open(path, 'w') as f:
        for row in temp:
            f.write("".join(row) + "\n")