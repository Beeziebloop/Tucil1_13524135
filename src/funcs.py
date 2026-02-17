def is_valid(positions, board, colors):
    n = len(positions)
    for i in range(n):
        for j in range(i + 1, n):
            #cek adjacency
            if abs(i - j) <= 1 and abs(positions[i] - positions[j]) <= 1:
                return False
    #cek apakah semua warna udah punya queen
    seen = set()
    for row, col in enumerate(positions):
        seen.add(board[row][col])
    return len(seen) == len(colors)

def visualize(board, positions, iteration):
    print(f"Iterasi ke-{iteration}:")
    temp = [row[:] for row in board]
    for row, col in enumerate(positions):
        temp[row][col] = '#'
    for row in temp:
        print("".join(row))

def print_solution(board, positions):
    temp = [row[:] for row in board]
    for row, col in enumerate(positions):
        temp[row][col] = '#'
    for row in temp:
        print("".join(row))