import numpy as np

# fmt: off
NONES_TBL = [
     0,  0,  0,  0,
     0,  0,  0,  0,
     0,  0,  0,  0,
     0,  0,  0,  0,
     0,  0,  0,  0,
     0,  0,  0,  0,
     0,  0,  0,  0,
     0,  0,  0,  0,
]
PAWNS_TBL = [
     0,  0,  0,  0,
    50, 50, 50, 50,
    10, 10, 20, 30,
     5,  5, 10, 25,
     0,  0,  0, 20,
     5, -5,-10,  0,
     5, 10, 10,-20,
     0,  0,  0,  0,
]
KNIGHTS_TBL = [
    -50,-40,-30,-30,
    -40,-20,  0,  0,
    -30,  0, 10, 15,
    -30,  5, 15, 20,
    -30,  0, 15, 20,
    -30,  5, 10, 15,
    -40,-20,  0,  5,
    -50,-40,-30,-30,
]
BISHOPS_TBL = [
    -20,-10,-10,-10,
    -10,  0,  0,  0,
    -10,  0,  5, 10,
    -10,  5,  5, 10,
    -10,  0, 10, 10,
    -10, 10, 10, 10,
    -10,  5,  0,  0,
    -20,-10,-10,-10,
]
ROOKS_TBL = [
      0,  0,  0,  0,
      5, 10, 10, 10,
     -5,  0,  0,  0,
     -5,  0,  0,  0,
     -5,  0,  0,  0,
     -5,  0,  0,  0,
     -5,  0,  0,  0,
      0,  0,  0,  5,
]
QUEENS_TBL = [
    -20,-10,-10, -5,
    -10,  0,  0,  0,
    -10,  0,  5,  5,
     -5,  0,  5,  5,
      0,  0,  5,  5,
    -10,  5,  5,  5,
    -10,  0,  5,  0,
    -20,-10,-10, -5,
]
KINGS_TBL = [
    -30,-40,-40,-50,
    -30,-40,-40,-50,
    -30,-40,-40,-50,
    -30,-40,-40,-50,
    -20,-30,-30,-40,
    -10,-20,-20,-20,
     20, 20,  0,  0,
     20, 30, 10,  0,
]
# fmt: on

PAWN_VAL = 100
KNIGHT_VAL = 320
BISHOP_VAL = 330
ROOK_VAL = 500
QUEEN_VAL = 900
KING_VAL = 20000


def compress(n: int | bytes | bytearray | list[int]):
    if not isinstance(n, int):
        n = int.from_bytes(n)
    nums = []
    i = 0
    for d in map(int, str(n)):
        j = 10 * i + d
        if 64 < j.bit_length():
            nums.append(i)
            j = d
        if j == 0:
            nums.append(0)
        i = j
    if i != 0:
        nums.append(i)
    return nums


def main():
    values = []
    for p in [
        NONES_TBL,
        PAWNS_TBL,
        KNIGHTS_TBL,
        BISHOPS_TBL,
        ROOKS_TBL,
        QUEENS_TBL,
        KINGS_TBL,
    ]:
        values.extend(map(lambda x: x, p))

    print(np.array(values))
    print(f'$"{"".join(map(lambda b: f"{{{b}}}" if b else "0", compress(values)))}"')


if __name__ == "__main__":
    main()
