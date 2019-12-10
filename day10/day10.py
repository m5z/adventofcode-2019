from collections import defaultdict


def main():
    with open('day10_input.txt') as f:
        m = [list(line.rstrip()) for line in f.readlines()]

    visibility_matrix = [[0] * len(m[0]) for _ in range(len(m))]

    max_count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '#':
                c = count(m, i, j)
                visibility_matrix[i][j] = c
                max_count = max(max_count, c)

    # for line in visibility_matrix:
    #     print(line)

    print(max_count)


def count(m, i, j):
    visible = set()
    for ii in range(len(m)):
        for jj in range(len(m[i])):
            if not (ii == i and jj == j) and m[ii][jj] == '#':
                relative = (ii - i, jj - j)
                if relative[0] == 0:
                    y = relative[1] // abs(relative[1])
                    visible.add((0, y))
                elif relative[1] == 0:
                    x = relative[0] // abs(relative[0])
                    visible.add((x, 0))
                else:
                    g = gcd(relative[0], relative[1])
                    x, y = relative[0] // g, relative[1] // g
                    visible.add((x, y))
    # print(i, j, visible)
    return len(visible)


def gcd(x, y):
    x, y = abs(x), abs(y)
    while y > 0:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    main()
