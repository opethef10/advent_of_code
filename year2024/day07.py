from operator import add, mul

OPS = add, mul


def solve(lines, text):
    total = 0
    for line in lines:
        test, rest = line.split(":")
        test = int(test)
        nums = list(map(int, rest.split()))
        n = len(nums) - 1
        num_combs = 2**n

        for comb in range(num_combs):
            binary = f"{bin(comb)[2:]:>0{n}}"
            indexes = list(map(int, binary))

            cumulation = nums[0]
            for i in range(n):
                b = nums[i + 1]
                op = OPS[indexes[i]]
                cumulation = op(cumulation, b)
            if cumulation == test:
                total += test
                break
    return total
