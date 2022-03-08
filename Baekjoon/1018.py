import sys


def count_paint(t: str, c1: str, c2: str,) -> int:
    count1 = 0
    count2 = 0
    for i in range(len(t)):
        if c1[i] != t[i]:
            count1 += 1
        if c2[i] != t[i]:
            count2 += 1
    return min(count1, count2)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())

    chess_layer = ["BW" * 4, "WB" * 4]
    chess1 = ""
    chess2 = ""
    for i in range(N):
        chess1 += chess_layer[i % 2]
        chess2 += chess_layer[(i + 1) % 2]

    jimin = []
    for i in range(N):
        jimin.append(input().strip())

    answer = 64
    for i in range(N - 8 + 1):
        cut = jimin[i : i + 8]
        for j in range(M - 8 + 1):
            board = ""
            for k in range(8):
                board += cut[k][j : j + 8]
            answer = min(answer, count_paint(board, chess1, chess2))

    print(answer)
