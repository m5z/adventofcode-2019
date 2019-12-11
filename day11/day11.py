from collections import defaultdict, deque


def main():
    with open('day11_input.txt') as f:
        ops = [int(x) for x in f.readline().rstrip().split(',')]

    inputs = deque([0])

    comp = Intcode(ops)
    comp.run(inputs)


class Intcode:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

    def __init__(self, ops):
        self.ops = defaultdict(lambda: 0)
        for i, op in enumerate(ops):
            self.ops[i] = op

        self.relative_base = 0

    def run(self, inputs):
        i = 0
        inputs = iter(inputs)
        while True:
            c = self.ops[i] % 100
            m = self.ops[i] // 100
            if c == 1:
                a, b = self._read_2_params(i, m)
                self._write_nth_param(i, m, 3, a + b)
                i += 4
            elif c == 2:
                a, b = self._read_2_params(i, m)
                self._write_nth_param(i, m, 3, a * b)
                i += 4
            elif c == 3:
                n = inputs.pop()
                self._write_nth_param(i, m, 1, n)
                i += 2
            elif c == 4:
                a = self._read_1_param(i, m)
                yield a
                i += 2
            elif c == 5:
                a, b = self._read_2_params(i, m)
                if a != 0:
                    i = b
                else:
                    i += 3
            elif c == 6:
                a, b = self._read_2_params(i, m)
                if a == 0:
                    i = b
                else:
                    i += 3
            elif c == 7:
                a, b = self._read_2_params(i, m)
                if a < b:
                    self._write_nth_param(i, m, 3, 1)
                else:
                    self._write_nth_param(i, m, 3, 0)
                i += 4
            elif c == 8:
                a, b = self._read_2_params(i, m)
                if a == b:
                    self._write_nth_param(i, m, 3, 1)
                else:
                    self._write_nth_param(i, m, 3, 0)
                i += 4
            elif c == 9:
                a = self._read_1_param(i, m)
                self.relative_base += a
                i += 2
            elif c == 99:
                return self.ops[0]
            else:
                raise Exception

    def _read_nth_param(self, i, m, n):
        mode = self._get_mode(m, n)
        if mode == Intcode.POSITION:
            return self.ops[self.ops[i + n]]
        elif mode == Intcode.IMMEDIATE:
            return self.ops[i + n]
        elif mode == Intcode.RELATIVE:
            return self.ops[self.relative_base + self.ops[i + n]]
        else:
            raise Exception

    def _read_1_param(self, i, m):
        return self._read_nth_param(i, m, 1)

    def _read_2_params(self, i, m):
        return self._read_nth_param(i, m, 1), self._read_nth_param(i, m, 2)

    def _write_nth_param(self, i, m, n, value):
        mode = self._get_mode(m, n)
        if mode == Intcode.POSITION:
            self.ops[self.ops[i + n]] = value
        elif mode == Intcode.IMMEDIATE:
            raise Exception
        elif mode == Intcode.RELATIVE:
            self.ops[self.relative_base + self.ops[i + n]] = value
        else:
            raise Exception

    @staticmethod
    def _get_mode(m, n):
        return (m // 10 ** (n - 1)) % 10


if __name__ == '__main__':
    main()
