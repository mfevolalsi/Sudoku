Card = [[0, 8, 0, 4, 0, 7, 0, 0, 0],
        [7, 3, 0, 1, 2, 0, 0, 9, 0],
        [2, 0, 9, 0, 8, 0, 7, 6, 0],
        [0, 0, 0, 0, 3, 1, 0, 0, 0],
        [0, 0, 2, 0, 7, 8, 9, 1, 0],
        [1, 9, 0, 0, 0, 5, 0, 8, 3],
        [8, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 2, 0, 3, 0, 4, 8, 7, 1],
        [4, 0, 3, 0, 0, 9, 0, 5, 0]]


def find_empty(card):
    for i in range(len(card)):
        for j in range(len(card)):
            if not card[i][j]:
                return i, j
    return None


def is_valid(card, num, pos):

    num_row = list(enumerate(card))[pos[0]][1]
    num_col = list(enumerate(list(zip(*card))))[pos[1]][1]
    num_tile = []

    if num in num_row:
        return False

    if num in num_col:
        return False

    tile_pos = [pos[0]//3, pos[1]//3]

    for row in range(tile_pos[0]*3, tile_pos[0]*3+3, 1):
        for col in range(tile_pos[1]*3, tile_pos[1]*3+3, 1):
            num_tile.append(card[row][col])

    if num in num_tile:
        return False

    return True


def solve(card):
    if find_empty(card):
        i, j = find_empty(card)
        for num in range(1, 10):
            if is_valid(card, num, (i, j)):
                card[i][j] = num
                card = solve(card)

    return card


print(solve(Card))
