WORD = "XMAS"



def part1(lines, text):
    n = len(lines)
    m = len(lines[0])
    limit = n * m - 1

    def sequential(pos):
        return text[pos: pos + 4] == WORD

    def reverse_sequential(pos):
        return text[pos: pos - 4: -1] == WORD

    def vertical(pos):
        for i, c in enumerate(WORD):
            p = pos + i * m
            if not 0 <= p <= limit:
                return False
            if text[p] != c:
                return False
        return True

    def rvertical(pos):
        for i, c in enumerate(WORD):
            p = pos - i * m
            if not 0 <= p <= limit:
                return False
            if text[p] != c:
                return False
        return True

    def diagonal1(pos):
        r, _ = divmod(pos, m)
        for i, c in enumerate(WORD):
            p = pos + i * m + i
            rr, cc = divmod(p, m)
            if r + i != rr:
                return False
            if not 0 <= p <= limit:
                return False
            if text[p] != c:
                return False
        return True

    def diagonal2(pos):
        r, _ = divmod(pos, m)
        for i, c in enumerate(WORD):
            p = pos + i * m - i
            rr, cc = divmod(p, m)
            if r + i != rr:
                return False
            if not 0 <= p <= limit:
                return False
            if text[p] != c:
                return False
        return True

    def diagonal3(pos):
        r, _ = divmod(pos, m)
        for i, c in enumerate(WORD):
            p = pos - i * m - i
            rr, cc = divmod(p, m)
            if r - i != rr:
                return False
            if not 0 <= p <= limit:
                return False
            if text[p] != c:
                return False
        return True

    def diagonal4(pos):
        r, _ = divmod(pos, m)
        for i, c in enumerate(WORD):
            p = pos - i * m + i
            rr, cc = divmod(p, m)
            if r - i != rr:
                return False
            if not 0 <= p <= limit:
                return False
            if text[p] != c:
                return False
        return True

    total = 0
    for pos, char in enumerate(text):
        total += sum(
            func(pos)
            for func in (
                sequential,
                reverse_sequential,
                vertical,
                rvertical,
                diagonal1,
                diagonal2,
                diagonal3,
                diagonal4,
            )
        )
    return total


def part2(lines, text):
    return
