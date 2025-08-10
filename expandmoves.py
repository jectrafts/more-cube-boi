moves = [('U', 2), ('R', 2), ('F', 1), ('L', 1), ('F', 2), ('B', 2), ('L', 2), ('F', 3), ('L', 1), ('F', 1), ('B', 2), ('U', 2), ('B', 2), ('L', 2), ('B', 2), ('L', 2), ('D', 1), ('F', 2), ('U', 1), ('F', 2)]
print(moves)
expanded_moves = [(face, 1) for face, turns in moves for _ in range(turns)]
print(expanded_moves)
