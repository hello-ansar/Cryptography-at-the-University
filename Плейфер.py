from itertools import chain, islice


def main():
    keytable = [
        ['М', 'А', 'Т', 'Е', 'Р', 'И'],
        ['Я', 'Б', 'В', 'Г', 'Д', 'Ж'],
        ['З', 'К', 'Л', 'Н', 'О', 'П'],
        ['С', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
        ['Ш', 'Щ', 'Ъ', 'Ы', 'Э', 'Ю']]

    ct = 'УЕНАЕЭМЧЗПФТКСЪИАРУЕПЕСЯЕХТИСЩГХМЖФЗЧБГЩКМЮАЕЪ'
    pt = playfair_decode(ct, keytable)
    print(pt)


def playfair_decode(ct, keytable):
    rows = len(keytable)
    cols = len(keytable[0])
    table = list(chain(*keytable))
    pt = []
    for pair in zip(islice(ct, 0, None, 2), islice(ct, 1, None, 2)):
        pt.append(playfair_decode_pair(pair, table, rows, cols))
    return "".join(chain(*pt))


def playfair_decode_pair(pair, table, rows, cols):
    x1, y1 = find_in_table(pair[0], table, rows, cols)
    x2, y2 = find_in_table(pair[1], table, rows, cols)
    x1, y1, x2, y2 = playfair_decode_transform(x1, y1, x2, y2, rows, cols)
    return table[y1 * cols + x1], table[y2 * cols + x2]


def find_in_table(c, table, rows, cols):
    idx = table.index(c)
    return idx % cols, idx // cols


def playfair_decode_transform(x1, y1, x2, y2, rows, cols):
    if x1 == x2:
        y1 = (y1 - 1) % rows
        y2 = (y2 - 1) % rows
    elif y1 == y2:
        x1 = (x1 - 1) % cols
        x2 = (x2 - 1) % cols
    else:
        x1, x2 = x2, x1
    return x1, y1, x2, y2


if __name__ == "__main__":
    main()