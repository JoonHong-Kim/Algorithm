import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())

    users = []
    for _ in range(N):
        users.append(input().split())

    users.sort(key=lambda x: int(x[0]))
    users = [" ".join(i) for i in users]

    print("\n".join(users))