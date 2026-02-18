import time
from funcs import is_valid, visualize

# generate semua permutasi dari possible queen positions untuk tiap baris itu di kolom keberapa aja
def generate_permutations(array, idx=0):
    if idx == len(array):
        yield array.copy()
        return
    for i in range(idx, len(array)):
        array[idx], array[i] = array[i], array[idx]
        yield from generate_permutations(array, idx + 1)
        array[idx], array[i] = array[i], array[idx]
# Note: fungsi ini menggunakan rekursi dan teknik swap untuk menghasilkan seluruh permutasi. Walau secara implementasi mirip dengan backtracking ia tidak melakukan pruning sama sekali, dan juga hanya digunakan untuk generate permutasi sebagai pengganti library itertools.
# Referensinya: https://jrwalsh1.github.io/posts/permutations-and-the-n-queens-problem/

def solve_game(board, colors, visual_each = 100):
    n = len(board)
    iterations = 0
    start = time.time()

    cols = list(range(n))
    solution = None

    for p in generate_permutations(cols):
        iterations += 1
        if iterations % visual_each == 0:
            visualize(board, p, iterations) #disini terjadi visualisasi tiap 100 iterasi, 100 karena kalau 10 takut kebanyakan
        if is_valid(p, board, colors):
            solution = p
            break

    elapsed = (time.time() - start) * 1000 #ubah ke ms
    return solution, iterations, elapsed
# Alur dari algoritma ini
# - Generate dulu semua permutasi dari posisi queen yang mungkin untuk tiap baris (misal untuk board 3x3 itu berarti generate permutasi dari [0, 1, 2] yang berarti queen di baris pertama bisa di kolom 0, queen di baris kedua bisa di kolom 1, dan queen di baris ketiga bisa di kolom 2)
# - Tiap permutasi yang digenerate akan divalidasi menggunakan fungsi is_valid (apakah semua warna sudah ada queen, apakah ada yang adjacent, apakah ada yang bentrok secara kolom)
# - Kalau ketemu solusi yang valid, langsung berhenti dan ngasih solusinya
# - Selama program berjalan, tiap 100 iterasi akan nongol visualisasi board dengan posisi queen yang lagi diuji coba