def toplama(a: int | float, b: int | float) -> int | float:
    c = a + b
    return c


def listeyi_topla(sayi_listesi: list) -> list:
    bos_liste = []

    for i in range(0, len(sayi_listesi), 2):
        c = toplama(sayi_listesi[i], sayi_listesi[i + 1])
        bos_liste.append(c)

    return bos_liste
