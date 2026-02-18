from file_management import parse_file, save_solution_to_file
from solver import solve_game
from funcs import print_solution

def main():
    filename = input("Input nama file (pastikan file berada di folder test): ")
    board, colors = parse_file(filename)
    solution, iterations, elapsed = solve_game(board, colors)
    if solution is not None:
        print("\nSolusi ditemukan!")
        print_solution(board, solution)
        print("\n")
        print(f"Posisi queen di setiap baris: {solution}")
        print(f"Jumlah solusi yang ditinjau: {iterations}")
        print(f"Waktu pencarian: {elapsed:.2f} ms")
        choice = input("Apakah anda ingin menyimpan solusi ke file? WARNING: akan overwrite file yang sudah ada! (y/n): ").strip().lower()
        if choice == 'y':
            save_solution_to_file(filename, board, solution)
            print(f"Solusi berhasil disimpan ke {filename}")
        else:
            print("Solusi tidak disimpan.")
    else:
        print("Tidak ada solusi yang valid ditemukan.")
        print(f"Total time elapsed: {elapsed:.2f} ms")
if __name__ == "__main__":    main()