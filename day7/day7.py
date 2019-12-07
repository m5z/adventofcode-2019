import itertools


def main():
    with open('day7_input.txt') as f:
        ops = [int(x) for x in f.readline().rstrip().split(',')]

    part1(ops)


def part1(ops):
    max_output = 0
    for config in itertools.permutations(range(5)):
        input_value = 0
        for phase in config:
            output_list = run(ops, [phase, input_value])
            input_value = output_list[0]
        max_output = max(max_output, input_value)
    print(max_output)  # 67023


def run(ops, input_list):
    ops = list(ops)

    input_i = 0
    output_list = []

    i = 0
    while True:
        c = ops[i] % 100
        m = ops[i] // 100
        if c == 1:
            a, b = read_2_params(ops, i, m)
            ops[ops[i + 3]] = a + b
            i += 4
        elif c == 2:
            a, b = read_2_params(ops, i, m)
            ops[ops[i + 3]] = a * b
            i += 4
        elif c == 3:
            n = input_list[input_i]
            input_i += 1
            ops[ops[i + 1]] = n
            i += 2
        elif c == 4:
            a = read_1_param(ops, i, m)
            output_list.append(a)
            i += 2
        elif c == 5:
            a, b = read_2_params(ops, i, m)
            if a != 0:
                i = b
            else:
                i += 3
        elif c == 6:
            a, b = read_2_params(ops, i, m)
            if a == 0:
                i = b
            else:
                i += 3
        elif c == 7:
            a, b = read_2_params(ops, i, m)
            if a < b:
                ops[ops[i + 3]] = 1
            else:
                ops[ops[i + 3]] = 0
            i += 4
        elif c == 8:
            a, b = read_2_params(ops, i, m)
            if a == b:
                ops[ops[i + 3]] = 1
            else:
                ops[ops[i + 3]] = 0
            i += 4
        elif c == 99:
            return output_list
        else:
            raise Exception


def read_nth_param(ops, i, m, n):
    mode = (m // 10 ** (n - 1)) % 10
    if mode == 0:
        return ops[ops[i + n]]
    elif mode == 1:
        return ops[i + n]
    else:
        raise Exception


def read_1_param(ops, i, m):
    return read_nth_param(ops, i, m, 1)


def read_2_params(ops, i, m):
    return read_nth_param(ops, i, m, 1), read_nth_param(ops, i, m, 2)


if __name__ == '__main__':
    main()
