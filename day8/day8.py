def main():
    with open('day8_input.txt') as f:
        digits = [int(x) for x in list(f.readline().rstrip())]

    width, height = 25, 6

    layers = [digits[i:i + width * height] for i in range(0, len(digits), width * height)]

    the_layer = []
    min_zeroes = len(digits)
    for layer in layers:
        zeroes = count(layer, 0)
        if zeroes < min_zeroes:
            the_layer = layer
            min_zeroes = zeroes

    ones = count(the_layer, 1)
    twos = count(the_layer, 2)

    print(ones * twos)


def count(layer, n):
    total = 0
    for x in layer:
        if x == n:
            total += 1
    return total


if __name__ == '__main__':
    main()
