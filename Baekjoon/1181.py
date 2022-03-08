import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    words = []
    for i in range(N):
        words.append(input().strip())
    words = list(set(words))
    words.sort()
    words.sort(key=len)
    for word in words:
        print(word)
